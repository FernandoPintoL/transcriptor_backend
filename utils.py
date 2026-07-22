import os
import whisper
from pydub import AudioSegment
from pydub.utils import mediainfo
from config import CHUNK_DURATION, TEMP_AUDIO_DIR, WHISPER_MODEL
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AudioProcessor:
    def __init__(self, model_name: str = WHISPER_MODEL):
        logger.info(f"Cargando modelo Whisper: {model_name}")
        self.model = whisper.load_model(model_name)
        self.model_name = model_name

    def split_audio(self, audio_path: str, chunk_duration: int = CHUNK_DURATION):
        """Divide un archivo de audio en chunks"""
        logger.info(f"Dividiendo audio: {audio_path}")

        audio = AudioSegment.from_file(audio_path)
        duration_ms = len(audio)
        chunk_ms = chunk_duration * 1000

        chunks = []
        for i in range(0, duration_ms, chunk_ms):
            chunk = audio[i:i + chunk_ms]
            chunk_path = os.path.join(TEMP_AUDIO_DIR, f"chunk_{i//chunk_ms:04d}.mp3")
            chunk.export(chunk_path, format="mp3", bitrate="192k")
            chunks.append(chunk_path)

        logger.info(f"Audio dividido en {len(chunks)} chunks")
        return chunks

    def transcribe_chunk(self, audio_path: str) -> str:
        """Transcribe un chunk de audio"""
        logger.info(f"Transcribiendo: {audio_path}")
        result = self.model.transcribe(audio_path, language="es")
        return result["text"]

    def transcribe_audio(self, audio_path: str) -> dict:
        """Transcribe un audio completo (dividiendo si es necesario)"""
        try:
            # Obtener duración del audio
            audio = AudioSegment.from_file(audio_path)
            duration_seconds = len(audio) / 1000

            logger.info(f"Duración del audio: {duration_seconds:.2f} segundos")

            # Si es menor a 10 minutos, transcribir directamente
            if duration_seconds < CHUNK_DURATION:
                logger.info("Audio pequeño, transcribiendo directamente")
                text = self.transcribe_chunk(audio_path)
                return {
                    "success": True,
                    "transcription": text,
                    "duration_seconds": duration_seconds,
                    "chunks_processed": 1
                }

            # Si es más largo, dividir y procesar
            chunks = self.split_audio(audio_path, CHUNK_DURATION)
            full_transcription = []

            for i, chunk_path in enumerate(chunks, 1):
                logger.info(f"Procesando chunk {i}/{len(chunks)}")
                text = self.transcribe_chunk(chunk_path)
                full_transcription.append(text)
                # Limpiar chunk temporal
                os.remove(chunk_path)

            return {
                "success": True,
                "transcription": " ".join(full_transcription),
                "duration_seconds": duration_seconds,
                "chunks_processed": len(chunks)
            }

        except Exception as e:
            logger.error(f"Error transcribiendo audio: {str(e)}")
            return {
                "success": False,
                "error": str(e)
            }

    def cleanup(self):
        """Limpia archivos temporales"""
        for file in os.listdir(TEMP_AUDIO_DIR):
            file_path = os.path.join(TEMP_AUDIO_DIR, file)
            try:
                os.remove(file_path)
            except Exception as e:
                logger.error(f"Error limpiando {file_path}: {str(e)}")
