# Setup GitHub - Pasos rápidos

## 1️⃣ Crear repositorio en GitHub

1. Ve a https://github.com/new
2. Nombre del repo: `transcriptor`
3. Descripción: `API para transcribir audios largos con Whisper`
4. Elige: Public o Private
5. Haz clic en "Create repository"

## 2️⃣ Subir el código (Windows PowerShell)

En la carpeta `D:\transcriptor`:

```powershell
# Inicializar Git
git init

# Agregar todos los archivos
git add .

# Primer commit
git commit -m "Initial commit: Transcriptor API backend"

# Agregar el remote de GitHub (reemplaza con tu usuario)
git remote add origin https://github.com/TU_USUARIO/transcriptor.git

# Cambiar rama a main
git branch -M main

# Subir al servidor
git push -u origin main
```

## 3️⃣ Verificar

Abre https://github.com/TU_USUARIO/transcriptor y verifica que esté todo ahí.

## ⚠️ Nota importante

**NO SUBAS estos archivos a GitHub:**
- `.env` (contiene secretos)
- `venv/` (ambiente virtual)
- `temp_audio/` (archivos temporales)
- `uploads/` (archivos subidos)
- `__pycache__/` (archivos compilados)

El `.gitignore` ya maneja esto automáticamente ✅

---

## 🔄 Después de hacer cambios

```powershell
# Ver cambios
git status

# Agregar archivos
git add .

# Hacer commit
git commit -m "Descripción del cambio"

# Subir a GitHub
git push origin main
```

---

## 💡 Comandos útiles

```powershell
# Ver historial
git log

# Ver estado
git status

# Ver cambios no confirmados
git diff

# Deshacer cambios
git restore .
```

¡Listo! Ya puedes subir a Railway desde aquí.
