# Transcriptor Frontend

Frontend moderno en Next.js para transcribir audios usando el backend de Whisper.

## Características

- 🎙️ Interfaz intuitiva para subir archivos de audio
- ⚡ Soporte para audios de cualquier duración
- 📝 Visualización de transcripciones en tiempo real
- 📋 Copiar transcripción al portapapeles
- 🎨 Diseño responsive con Tailwind CSS
- 🔗 Conexión automática con backend Python

## Instalación

### Requisitos previos
- Node.js 18+
- npm o yarn

### Pasos

1. **Instalar dependencias**
```bash
cd frontend
npm install
# o
yarn install
```

2. **Configurar variables de entorno**

Crea un archivo `.env.local` en la carpeta `frontend`:
```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
```

3. **Iniciar el servidor de desarrollo**
```bash
npm run dev
# o
yarn dev
```

El frontend estará disponible en `http://localhost:3000`

## Uso

1. Asegúrate que el **backend en Python está corriendo**:
```bash
# En otra terminal, en D:\transcriptor
python main.py
```

2. **Abre el navegador** en `http://localhost:3000`

3. **Sube un archivo de audio** (MP3, WAV, OGG, FLAC, M4A)

4. **Haz clic en "Transcribir"** y espera el resultado

5. **Copia la transcripción** si lo necesitas

## Estructura del proyecto

```
frontend/
├── app/
│   ├── layout.tsx       # Layout principal
│   ├── page.tsx         # Página principal
│   └── globals.css      # Estilos globales
├── components/
│   └── AudioUploader.tsx # Componente principal
├── package.json
├── next.config.js
├── tailwind.config.js
└── tsconfig.json
```

## Scripts disponibles

- `npm run dev` - Inicia servidor de desarrollo
- `npm run build` - Construye la app para producción
- `npm run start` - Inicia servidor de producción
- `npm run lint` - Ejecuta ESLint

## Variables de entorno

| Variable | Descripción | Default |
|----------|-------------|---------|
| `NEXT_PUBLIC_API_URL` | URL del backend | `http://localhost:8000` |

## Troubleshooting

### "Cannot GET /"
Asegúrate que el servidor esté corriendo con `npm run dev`

### "Error: Failed to connect to API"
Verifica que:
1. El backend en Python está corriendo en `http://localhost:8000`
2. CORS está habilitado en el backend (debería estarlo por defecto)
3. La variable `NEXT_PUBLIC_API_URL` es correcta

### "Module not found"
```bash
rm -rf node_modules
npm install
```

## Build para producción

```bash
npm run build
npm run start
```

## Deployment

Este frontend puede desplegarse en:
- Vercel (recomendado)
- Netlify
- AWS Amplify
- Docker

### Con Vercel (más fácil)

```bash
npm i -g vercel
vercel
```

## Stack tecnológico

- **Next.js 14** - Framework React
- **React 18** - Librería UI
- **Tailwind CSS** - Estilos
- **Axios** - Cliente HTTP
- **TypeScript** - Type safety

## Próximos pasos

- [ ] Agregar descarga de transcripción como PDF/TXT
- [ ] Historial de transcripciones
- [ ] Soporte para múltiples idiomas
- [ ] Autenticación de usuarios
- [ ] Análisis de sentimientos
- [ ] Sincronización con cloud storage

## Notas

- El frontend se comunica con el backend a través de la URL en `NEXT_PUBLIC_API_URL`
- En desarrollo, ambos servidores corren en `localhost`
- En producción, cambiar la URL del backend según sea necesario
