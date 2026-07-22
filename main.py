from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import logging
from config import API_TITLE, API_VERSION, API_DESCRIPTION, UPLOAD_DIR
from utils import AudioProcessor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=API_TITLE,
    version=API_VERSION,
    description=API_DESCRIPTION
)

# CORS para conectar con React/Next.js
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambiar a dominio específico en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializar procesador de audio
processor = None

@app.on_event("startup")
async def startup_event():
    global processor
    logger.info("Iniciando servidor...")
    processor = AudioProcessor()
    logger.info("Servidor listo")

@app.get("/health")
async def health_check():
    """Verifica que el servidor esté funcionando"""
    return {"status": "ok", "service": "transcriptor-api"}

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    """
    Transcribe un archivo de audio
    Soporta: MP3, WAV, OGG, FLAC, M4A
    Tamaño máximo: 500MB
    """
    try:
        # Validar tipo de archivo
        allowed_formats = {"audio/mpeg", "audio/wav", "audio/ogg", "audio/flac", "audio/mp4"}
        if file.content_type not in allowed_formats:
            raise HTTPException(
                status_code=400,
                detail=f"Formato no soportado. Usa: MP3, WAV, OGG, FLAC, M4A"
            )

        # Guardar archivo
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as f:
            contents = await file.read()
            f.write(contents)

        logger.info(f"Archivo guardado: {file_path}")

        # Transcribir
        result = processor.transcribe_audio(file_path)

        # Limpiar archivo original
        os.remove(file_path)

        if not result["success"]:
            raise HTTPException(status_code=500, detail=result["error"])

        return JSONResponse({
            "success": True,
            "filename": file.filename,
            "transcription": result["transcription"],
            "duration_seconds": result["duration_seconds"],
            "chunks_processed": result["chunks_processed"],
            "model": f"whisper-{processor.model_name}"
        })

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error en /transcribe: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error procesando archivo: {str(e)}")

@app.get("/models")
async def get_available_models():
    """Lista los modelos Whisper disponibles"""
    return {
        "available_models": ["tiny", "base", "small", "medium", "large"],
        "current_model": processor.model_name,
        "description": {
            "tiny": "Más rápido, menos preciso (~39M parámetros)",
            "base": "Balance velocidad-precisión (~74M parámetros)",
            "small": "Más preciso que base (~244M parámetros)",
            "medium": "Alta precisión (~769M parámetros)",
            "large": "Máxima precisión (~1.5B parámetros)"
        }
    }

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
