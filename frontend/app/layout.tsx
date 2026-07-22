import type { Metadata } from "next"
import "./globals.css"

export const metadata: Metadata = {
  title: "Transcriptor - Convierte audios a texto",
  description: "Transcribe audios largos usando IA con Whisper",
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="es">
      <body className="bg-gradient-to-br from-slate-900 to-slate-800 min-h-screen">
        {children}
      </body>
    </html>
  )
}
