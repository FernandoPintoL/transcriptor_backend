# Quick Start - Backend Transcriptor

## 1️⃣ Instalación Rápida

```bash
# Crear ambiente virtual
python -m venv venv
venv\Scripts\activate  # En Windows
# source venv/bin/activate  # En Mac/Linux

# Instalar dependencias
pip install -r requirements.txt

# ⚠️ Importante: Instalar FFmpeg
# Windows (con Chocolatey): choco install ffmpeg
# Windows (manual): https://ffmpeg.org/download.html
# Mac: brew install ffmpeg
# Linux: sudo apt-get install ffmpeg
```

## 2️⃣ Iniciar el Servidor

```bash
python main.py
```

Verás algo como:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

## 3️⃣ Probar la API

### Opción A: Interfaz Swagger (más fácil)
- Abre: http://localhost:8000/docs
- Haz clic en "Try it out" en `/transcribe`
- Sube un archivo de audio
- ¡Listo!

### Opción B: Con el script de prueba
```bash
python test_api.py tu_audio.mp3
```

### Opción C: Con cURL
```bash
curl -X POST "http://localhost:8000/transcribe" \
  -F "file=@tu_audio.mp3"
```

## 4️⃣ Estructura creada

```
transcriptor/
├── main.py           # 🚀 La API
├── utils.py          # 🔧 Procesamiento
├── config.py         # ⚙️ Configuración
├── requirements.txt  # 📦 Dependencias
├── README.md         # 📖 Documentación completa
├── test_api.py       # 🧪 Tests
└── .env.example      # 📝 Variables de entorno
```

## 5️⃣ Endpoints Disponibles

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `/health` | GET | Verifica que esté corriendo |
| `/transcribe` | POST | Transcribe un audio |
| `/models` | GET | Lista modelos disponibles |
| `/docs` | GET | Documentación interactiva |

## 🆘 Troubleshooting

### "ModuleNotFoundError: No module named 'whisper'"
```bash
pip install -r requirements.txt
```

### "FFmpeg not found"
Instala FFmpeg según tu SO (ver paso 1)

### El servidor es muy lento
- Usa el modelo "tiny" para pruebas rápidas
- En `.env`: `WHISPER_MODEL=tiny`

### Primera ejecución tarda mucho
Es normal, está descargando el modelo Whisper (~1.4GB)

## ✅ Checklist

- [ ] Python 3.8+ instalado
- [ ] Ambiente virtual creado y activado
- [ ] Dependencias instaladas (`pip install -r requirements.txt`)
- [ ] FFmpeg instalado
- [ ] Servidor corriendo (`python main.py`)
- [ ] Probado en http://localhost:8000/docs

## 🎯 Próximo paso

Una vez que el backend esté funcionando, crearemos el frontend en React/Next.js para consumir esta API.

¿Dudas? Revisa `README.md` para documentación completa.
