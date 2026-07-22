# Transcriptor API

API backend en Python para transcribir audios largos usando OpenAI Whisper.

## Instalación

### Requisitos previos
- Python 3.8+
- FFmpeg (necesario para pydub)

### Pasos

1. **Clonar o navegar al proyecto**
```bash
cd transcriptor
```

2. **Crear ambiente virtual**
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Instalar FFmpeg**
   - **Windows**: `choco install ffmpeg` (si tienes Chocolatey) o descargar de https://ffmpeg.org/download.html
   - **Mac**: `brew install ffmpeg`
   - **Linux**: `sudo apt-get install ffmpeg`

5. **Crear archivo .env (opcional)**
```bash
WHISPER_MODEL=base
TEMP_AUDIO_DIR=./temp_audio
UPLOAD_DIR=./uploads
```

## Uso

### Iniciar el servidor
```bash
python main.py
```

El servidor estará disponible en `http://localhost:8000`

### Documentación interactiva
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Endpoints

### 1. Health Check
```
GET /health
```
Verifica que el servidor esté funcionando.

**Respuesta:**
```json
{
  "status": "ok",
  "service": "transcriptor-api"
}
```

### 2. Transcribe (Principal)
```
POST /transcribe
```
Sube y transcribe un archivo de audio.

**Parámetros:**
- `file`: Archivo de audio (MP3, WAV, OGG, FLAC, M4A)

**Respuesta:**
```json
{
  "success": true,
  "filename": "audio.mp3",
  "transcription": "Texto transcrito...",
  "duration_seconds": 7200.5,
  "chunks_processed": 12,
  "model": "whisper-base"
}
```

### 3. Modelos disponibles
```
GET /models
```
Lista los modelos Whisper disponibles.

**Respuesta:**
```json
{
  "available_models": ["tiny", "base", "small", "medium", "large"],
  "current_model": "base",
  "description": {...}
}
```

## Modelos Whisper

| Modelo | Tamaño | Velocidad | Precisión | Uso ideal |
|--------|--------|-----------|-----------|-----------|
| tiny | 39M | ⚡⚡⚡⚡⚡ | ⭐⭐ | Pruebas rápidas |
| base | 74M | ⚡⚡⚡⚡ | ⭐⭐⭐ | Balance |
| small | 244M | ⚡⚡⚡ | ⭐⭐⭐⭐ | Producción |
| medium | 769M | ⚡⚡ | ⭐⭐⭐⭐⭐ | Alta calidad |
| large | 1.5B | ⚡ | ⭐⭐⭐⭐⭐ | Máxima precisión |

## Características

- ✅ Manejo automático de audios largos (> 2 horas)
- ✅ División inteligente en chunks de 10 minutos
- ✅ Soporte para múltiples formatos de audio
- ✅ CORS habilitado para React/Next.js
- ✅ Logs detallados
- ✅ Limpieza automática de archivos temporales
- ✅ Documentación automática con Swagger

## Ejemplos

### Con cURL
```bash
curl -X POST "http://localhost:8000/transcribe" \
  -F "file=@/path/to/audio.mp3"
```

### Con Python
```python
import requests

with open("audio.mp3", "rb") as f:
    files = {"file": f}
    response = requests.post("http://localhost:8000/transcribe", files=files)
    print(response.json())
```

### Con JavaScript/Fetch
```javascript
const formData = new FormData();
formData.append("file", audioFile);

const response = await fetch("http://localhost:8000/transcribe", {
  method: "POST",
  body: formData
});

const data = await response.json();
console.log(data.transcription);
```

## Estructura del proyecto

```
transcriptor/
├── main.py           # Aplicación FastAPI
├── utils.py          # Lógica de procesamiento
├── config.py         # Configuraciones
├── requirements.txt  # Dependencias Python
├── README.md         # Este archivo
└── .gitignore
```

## Notas

- La primera ejecución descargará el modelo Whisper (~1.4GB para "base")
- Los archivos subidos se procesan y eliminan después de la transcripción
- Los chunks temporales se limpian automáticamente
- En producción, cambiar `allow_origins=["*"]` a dominios específicos

## Troubleshooting

### "FFmpeg not found"
Instala FFmpeg según tu sistema operativo (ver sección Instalación)

### "CUDA not available"
Whisper usará CPU. Para GPU, instala CUDA y `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118`

### El servidor es lento
- Usa un modelo más pequeño (tiny, base)
- Aumenta `CHUNK_DURATION` en config.py
- Usa una máquina con GPU

## Deployment

### Railway (Recomendado)

Ver [DEPLOY.md](DEPLOY.md) para instrucciones detalladas de deployment.

**Pasos rápidos:**
1. Sube a GitHub: ver [GITHUB_SETUP.md](GITHUB_SETUP.md)
2. Conecta Railway a tu repositorio GitHub
3. Railway detectará automáticamente que es Python
4. Configura variables de entorno en el dashboard de Railway
5. ¡Listo! Tu API estará en línea

**URL en Railway:** `https://tu-proyecto.railway.app`

### Localmente

Para desarrollo local, el servidor corre en `http://localhost:8000`

### Otros servicios

- **Heroku**: Requiere `Procfile` (incluido)
- **Docker**: Crear `Dockerfile` si lo necesitas
- **AWS**: Usar Elastic Beanstalk o Lambda
- **Google Cloud**: Cloud Run
- **Azure**: App Service

## Estructura del proyecto

```
transcriptor/
├── main.py              # Aplicación FastAPI
├── utils.py             # Lógica de procesamiento
├── config.py            # Configuraciones
├── requirements.txt     # Dependencias Python
├── Procfile             # Para Heroku/Railway
├── railway.json         # Configuración Railway
├── .env.example         # Variables de ejemplo
├── .gitignore
├── README.md
├── DEPLOY.md            # Guía deployment
└── GITHUB_SETUP.md      # Guía GitHub
```

## Próximos pasos

- ✅ Backend funcionando
- ⏳ Frontend conectado
- Agregar autenticación
- Implementar cola de tareas (Celery)
- Base de datos para guardar transcripciones
- Barra de progreso en tiempo real
