# Archivos que se subirán a GitHub

Esta es la lista de archivos/carpetas que se subirán cuando hagas `git push`:

## ✅ SERÁN SUBIDOS (Código y configuración)

```
transcriptor/
├── main.py                    ✅ Aplicación principal
├── utils.py                   ✅ Lógica de procesamiento
├── config.py                  ✅ Configuraciones
├── requirements.txt           ✅ Dependencias Python
├── Procfile                   ✅ Configuración para Railway
├── railway.json               ✅ Configuración Railway
├── .gitignore                 ✅ Archivo de exclusiones
├── .env.example               ✅ Ejemplo de variables
├── README.md                  ✅ Documentación principal
├── DEPLOY.md                  ✅ Guía de deployment
├── GITHUB_SETUP.md            ✅ Guía GitHub
├── GITIGNORE_EXPLAINED.md     ✅ Explicación .gitignore
└── FILES_TO_UPLOAD.md         ✅ Este archivo
```

**Total:** ~50KB de código y documentación

---

## ❌ NO SERÁN SUBIDOS (Ignorados por .gitignore)

### Directorios

```
venv/                  ❌ Ambiente virtual Python (100MB+)
__pycache__/           ❌ Archivos compilados de Python
temp_audio/            ❌ Audios temporales (pueden ser gigantescos)
uploads/               ❌ Archivos subidos por usuarios
.vscode/               ❌ Configuración de VS Code
.idea/                 ❌ Configuración de PyCharm
node_modules/          ❌ Dependencias Node.js (si hay)
model_cache/           ❌ Modelos descargados de Whisper (1.4GB)
logs/                  ❌ Archivos de logs
```

### Archivos

```
.env                   ❌ Variables de entorno con SECRETOS
.env.local             ❌ Configuración local
*.pyc                  ❌ Archivos compilados Python
*.mp3, *.wav, *.ogg    ❌ Archivos de audio
*.pth, *.pt            ❌ Modelos de IA
*.log                  ❌ Archivos de log
.DS_Store              ❌ Archivo del sistema macOS
Thumbs.db              ❌ Archivo del sistema Windows
```

---

## 📊 Comparación de tamaños

```
                    Tamaño          ¿GitHub lo toma?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Código Python       ~50 KB           ✅ Sí
requirements.txt    ~500 bytes       ✅ Sí
venv/ (ignorado)    ~100 MB          ❌ No
temp_audio/         ~500 MB          ❌ No
Whisper model       ~1.4 GB          ❌ No
Total subido        ~50 KB           ✅ Perfecto
```

---

## 🔒 Información Sensible

**JAMÁS se subirán:**
- 🔑 `.env` con claves de API
- 🔓 Contraseñas o tokens
- 📧 Emails privados
- 🔓 URLs internas

Usa `.env.example` para mostrar qué variables son necesarias.

---

## ✔️ Antes de hacer push

Verifica qué se va a subir:

```powershell
# Ver qué se va a confirmar
git status

# Ver archivos en staging
git add .
git status

# Si algo no debería subirse:
git restore --staged archivo.txt
```

---

## 🚀 Comando final para subir

```powershell
# Una sola vez:
git remote add origin https://github.com/TU_USUARIO/transcriptor.git

# Siempre:
git add .
git commit -m "Descripción del cambio"
git push origin main
```

---

**¿Todo bien? ¡Adelante con el push! 🚀**
