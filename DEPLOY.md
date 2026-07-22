# Deployment - Backend Transcriptor

Guía para desplegar el backend en Railway.

## Prerequisitos

- Cuenta en [GitHub](https://github.com)
- Cuenta en [Railway](https://railway.app)
- Git instalado
- Acceso al repositorio

## Paso 1: Preparar el código local

### Inicializar Git (si no lo has hecho)

```bash
cd D:\transcriptor
git init
git add .
git commit -m "Initial commit: Transcriptor API backend"
```

### Verificar archivos importantes

Asegúrate que existan:
- ✅ `requirements.txt` - Dependencias Python
- ✅ `Procfile` - Comando para ejecutar la app
- ✅ `railway.json` - Configuración de Railway
- ✅ `.env.example` - Variables de entorno de ejemplo
- ✅ `.gitignore` - Para no subir archivos innecesarios

## Paso 2: Subir a GitHub

### Crear repositorio en GitHub

1. Ve a [github.com](https://github.com)
2. Haz clic en "New repository"
3. Nombre: `transcriptor` (o el que prefieras)
4. Copia el comando para agregar remote:

```bash
git remote add origin https://github.com/TU_USUARIO/transcriptor.git
git branch -M main
git push -u origin main
```

## Paso 3: Desplegar en Railway

### Opción A: Con Railway CLI (Recomendado)

```bash
# Instalar Railway CLI
npm install -g railway

# Iniciar sesión
railway login

# Inicializar proyecto en Railway
railway init

# Selecciona "create new project"
# Selecciona "existing repo"

# Desplegar
railway up
```

### Opción B: Con la web de Railway

1. Ve a [railway.app](https://railway.app)
2. Haz clic en "Create New Project"
3. Selecciona "Deploy from GitHub"
4. Autentica con GitHub
5. Selecciona tu repositorio `transcriptor`
6. Railway detectará automáticamente que es Python
7. Haz clic en "Deploy"

## Paso 4: Configurar variables de entorno

En el dashboard de Railway:

1. Ve a tu proyecto
2. Haz clic en "Variables"
3. Agregar variables:

```
WHISPER_MODEL=small
TEMP_AUDIO_DIR=/tmp/temp_audio
UPLOAD_DIR=/tmp/uploads
```

**Nota:** En Railway no puedes usar paths relativos, usa `/tmp/` para archivos temporales.

## Paso 5: Obtener la URL de tu API

Una vez desplegado:

1. En Railway, ve a tu servicio
2. Haz clic en "Settings"
3. Busca "Public URL"
4. Copia la URL (será algo como: `https://transcriptor-prod.up.railway.app`)

## Paso 6: Actualizar el frontend

En `D:\transcriptor\frontend\.env.local`:

```
NEXT_PUBLIC_API_URL=https://transcriptor-prod.up.railway.app
```

Luego despliega el frontend (en Vercel, Netlify, etc.)

---

## Troubleshooting

### "Build failed"

Verifica que:
- ✅ `requirements.txt` existe y está bien formado
- ✅ `Procfile` o `railway.json` existe
- ✅ Python es compatible (3.8+)

### "Modelo Whisper no descargar"

El modelo se descarga en el primer run. Si es muy lento:
- Usa `WHISPER_MODEL=tiny` en variables de entorno
- Aumenta el timeout en Railway a 10+ minutos

### "Archivos temporales no se guardan"

Railway usa sistemas de archivos efímeros. Usa rutas en `/tmp/`:
```
TEMP_AUDIO_DIR=/tmp/temp_audio
UPLOAD_DIR=/tmp/uploads
```

### "Puerto en uso"

Railway asigna el puerto automáticamente a través de la variable `$PORT`. El código ya lo soporta.

---

## Monitoreo

Una vez desplegado, puedes:

1. Ver logs: `railway logs`
2. Monitorear: Dashboard de Railway
3. Testear API: `https://tu-url.railway.app/docs`

## Costos

Railway tiene:
- **Tier Gratuito:** $5 créditos/mes (suficiente para pequeños usos)
- **Pay as you go:** Después de usar los créditos

Transforma de audio requiere CPU, calcula según uso esperado.

---

## Actualizar después de cambios

```bash
git add .
git commit -m "Update: descripción del cambio"
git push origin main
```

Railway redesplegará automáticamente.

---

¿Preguntas? Revisa la documentación de [Railway](https://docs.railway.app)
