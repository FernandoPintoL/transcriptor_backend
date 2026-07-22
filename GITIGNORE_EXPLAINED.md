# .gitignore Explicado

Este archivo asegura que **NO subes archivos innecesarios o peligrosos** a GitHub.

## 🔒 SECRETOS (MUY IMPORTANTE)

```
.env
.env.local
```

**Estos archivos contienen:**
- Claves de API
- Contraseñas
- Tokens de autenticación
- URLs privadas

**NUNCA los subas a GitHub** - Si lo haces, borra el historio de git.

---

## 📦 Ambiente Virtual Python

```
venv/
.venv/
env/
```

**Por qué se ignora:**
- Son carpetas GRANDES (~100MB+)
- Se regeneran con `pip install -r requirements.txt`
- Cada máquina tiene su propio ambiente

---

## 🎵 Archivos de Audio

```
*.mp3
*.wav
*.ogg
*.flac
*.m4a
temp_audio/
uploads/
```

**Por qué se ignora:**
- **Son MUY grandes** (problemas de tamaño en GitHub)
- Son archivos de prueba, no código
- Se generan en runtime

---

## 🤖 Modelos Whisper

```
*.pt
*.pth
model_cache/
whisper_models/
```

**Por qué se ignora:**
- El modelo base de Whisper = **1.4GB**
- Se descarga automáticamente en el primer run
- No debe estar en el repo

---

## 🐍 Python Compilado

```
__pycache__/
*.pyc
*.pyo
*.egg-info/
```

**Por qué se ignora:**
- Son archivos compilados de Python
- Se generan automáticamente
- Específicos de cada máquina

---

## 📝 Logs

```
*.log
logs/
```

**Por qué se ignora:**
- Pueden contener información sensible
- Son archivos de ejecución, no código
- Pueden crecer sin límite

---

## 💻 IDE y Editores

```
.vscode/
.idea/
```

**Por qué se ignora:**
- Configuraciones personales de cada desarrollador
- No son código de la aplicación
- Cada uno usa el editor que prefiere

---

## ✅ QUÉ SÍ se sube a GitHub

```
✅ main.py
✅ utils.py
✅ config.py
✅ requirements.txt
✅ Procfile
✅ railway.json
✅ README.md
✅ .gitignore
✅ .env.example
✅ DEPLOY.md
```

---

## 🔍 Antes de hacer push

Verifica que **NO hayas subido**:

```powershell
# Ver qué se va a subir
git status

# Ver archivos antes de confirmar
git diff --cached

# Si subes algo por error:
git reset HEAD archivo.txt
```

---

## ⚠️ Si accidentalmente subes .env

```powershell
# Quitar del repositorio (pero no del disco)
git rm --cached .env

# Agregar a .gitignore
echo ".env" >> .gitignore

# Confirmar cambios
git add .gitignore
git commit -m "Remove .env from tracking"
git push origin main

# EN PRODUCCIÓN: Cambiar todas las claves/tokens
```

---

## 📋 Checklist antes de push

- [ ] ✅ No hay `.env` en staging (`git status`)
- [ ] ✅ No hay carpetas grandes (`temp_audio/`, `uploads/`)
- [ ] ✅ No hay `venv/` o ambiente virtual
- [ ] ✅ Solo código Python limpio
- [ ] ✅ Incluye `requirements.txt`
- [ ] ✅ Incluye `README.md`

---

**¡Ahora seguro puedes hacer push a GitHub! 🚀**
