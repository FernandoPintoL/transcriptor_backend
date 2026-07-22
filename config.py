import os
from dotenv import load_dotenv

load_dotenv()

# Configuración de Whisper
WHISPER_MODEL = os.getenv("WHISPER_MODEL", "base")  # tiny, base, small, medium, large
CHUNK_DURATION = 600  # 10 minutos en segundos
TEMP_AUDIO_DIR = os.getenv("TEMP_AUDIO_DIR", "./temp_audio")
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./uploads")

# Crear directorios si no existen
os.makedirs(TEMP_AUDIO_DIR, exist_ok=True)
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Configuración de API
API_TITLE = "Transcriptor API"
API_VERSION = "1.0.0"
API_DESCRIPTION = "API para transcribir audios largos usando OpenAI Whisper"
