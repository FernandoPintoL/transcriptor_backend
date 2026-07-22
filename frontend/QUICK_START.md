# Quick Start - Frontend

## ⚡ Inicio rápido (2 minutos)

### 1️⃣ Instalar dependencias
```bash
cd frontend
npm install
```

### 2️⃣ Configurar backend
En `.env.local` (copia de `.env.example`):
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### 3️⃣ Iniciar servidor

**Terminal 1 - Backend:**
```bash
# En D:\transcriptor
python main.py
```

**Terminal 2 - Frontend:**
```bash
# En D:\transcriptor\frontend
npm run dev
```

### 4️⃣ Abrir en navegador
```
http://localhost:3000
```

## 🎯 ¡Listo!

Ahora puedes:
- ✅ Subir archivos de audio
- ✅ Transcribir automáticamente
- ✅ Copiar la transcripción

## 📚 Estructura

```
D:\transcriptor\
├── main.py           ← Backend Python
├── config.py
├── utils.py
└── frontend/         ← Frontend Next.js
    ├── app/
    ├── components/
    ├── package.json
    └── npm run dev
```

## 🆘 Troubleshooting

| Problema | Solución |
|----------|----------|
| "Cannot connect to API" | ¿Backend corriendo en puerto 8000? |
| "Module not found" | `rm -rf node_modules && npm install` |
| Puerto 3000 ya en uso | `npm run dev -- -p 3001` |

## 📖 Documentación completa

Ver `README.md` en esta carpeta.
