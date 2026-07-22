'use client'

import { useState, useRef } from 'react'
import axios from 'axios'
import { Document, Packer, Paragraph } from 'docx'
import { saveAs } from 'file-saver'

interface TranscriptionResult {
  success: boolean
  filename: string
  transcription: string
  duration_seconds: number
  chunks_processed: number
  model: string
}

export default function AudioUploader() {
  const [file, setFile] = useState<File | null>(null)
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState<TranscriptionResult | null>(null)
  const [error, setError] = useState<string | null>(null)
  const fileInputRef = useRef<HTMLInputElement>(null)
  const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files?.[0]) {
      setFile(e.target.files[0])
      setError(null)
    }
  }

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()

    if (!file) {
      setError('Por favor selecciona un archivo de audio')
      return
    }

    setLoading(true)
    setError(null)
    setResult(null)

    try {
      const formData = new FormData()
      formData.append('file', file)

      const response = await axios.post<TranscriptionResult>(
        `${API_URL}/transcribe`,
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        }
      )

      setResult(response.data)
      setFile(null)
      if (fileInputRef.current) {
        fileInputRef.current.value = ''
      }
    } catch (err) {
      const errorMessage = axios.isAxiosError(err)
        ? err.response?.data?.detail || err.message
        : 'Error desconocido'
      setError(`Error: ${errorMessage}`)
    } finally {
      setLoading(false)
    }
  }

  const formatDuration = (seconds: number) => {
    const mins = Math.floor(seconds / 60)
    const secs = Math.round(seconds % 60)
    return `${mins}m ${secs}s`
  }

  const downloadAsTxt = () => {
    if (!result) return
    const element = document.createElement('a')
    const file = new Blob([result.transcription], { type: 'text/plain' })
    element.href = URL.createObjectURL(file)
    element.download = `${result.filename.replace(/\.[^/.]+$/, '')}_transcription.txt`
    document.body.appendChild(element)
    element.click()
    document.body.removeChild(element)
  }

  const downloadAsDocx = async () => {
    if (!result) return

    const paragraphs = result.transcription.split('\n').map(
      (text) => new Paragraph(text || ' ')
    )

    const doc = new Document({
      sections: [
        {
          children: [
            new Paragraph({
              text: 'Transcripción de audio',
              bold: true,
              size: 32,
            }),
            new Paragraph(''),
            new Paragraph({
              text: `Archivo: ${result.filename}`,
              italics: true,
              size: 20,
            }),
            new Paragraph({
              text: `Duración: ${formatDuration(result.duration_seconds)}`,
              italics: true,
              size: 20,
            }),
            new Paragraph({
              text: `Modelo: ${result.model}`,
              italics: true,
              size: 20,
            }),
            new Paragraph(''),
            new Paragraph(''),
            ...paragraphs,
          ],
        },
      ],
    })

    const blob = await Packer.toBlob(doc)
    saveAs(blob, `${result.filename.replace(/\.[^/.]+$/, '')}_transcription.docx`)
  }

  return (
    <div className="w-full max-w-4xl mx-auto px-4 py-8">
      <div className="bg-white rounded-lg shadow-xl p-8">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">🎙️ Transcriptor</h1>
          <p className="text-gray-600">
            Convierte tus audios a texto usando IA. Soporta audios de cualquier duración.
          </p>
        </div>

        {/* Upload Form */}
        <form onSubmit={handleSubmit} className="mb-8">
          <div className="border-2 border-dashed border-blue-300 rounded-lg p-8 text-center hover:border-blue-500 transition mb-6">
            <input
              ref={fileInputRef}
              type="file"
              accept="audio/*"
              onChange={handleFileChange}
              className="hidden"
              id="audio-input"
            />
            <label htmlFor="audio-input" className="cursor-pointer block">
              <div className="text-5xl mb-4">🎵</div>
              <p className="text-lg font-semibold text-gray-900 mb-2">
                {file ? file.name : 'Selecciona o arrastra un archivo de audio'}
              </p>
              <p className="text-sm text-gray-500">
                Soporta MP3, WAV, OGG, FLAC, M4A
              </p>
            </label>
          </div>

          {file && (
            <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 mb-6">
              <p className="text-sm text-gray-700">
                <span className="font-semibold">Archivo seleccionado:</span> {file.name}
              </p>
              <p className="text-sm text-gray-600">
                Tamaño: {(file.size / 1024 / 1024).toFixed(2)} MB
              </p>
            </div>
          )}

          <button
            type="submit"
            disabled={!file || loading}
            className="w-full bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white font-bold py-3 px-6 rounded-lg transition"
          >
            {loading ? (
              <span className="flex items-center justify-center gap-2">
                <span className="inline-block w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></span>
                Transcribiendo...
              </span>
            ) : (
              'Transcribir'
            )}
          </button>
        </form>

        {/* Error Message */}
        {error && (
          <div className="bg-red-50 border border-red-200 rounded-lg p-4 mb-6">
            <p className="text-red-800">{error}</p>
          </div>
        )}

        {/* Results */}
        {result && (
          <div className="bg-green-50 border border-green-200 rounded-lg p-6">
            <div className="mb-6">
              <h2 className="text-2xl font-bold text-gray-900 mb-4">✅ Transcripción completada</h2>

              <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
                <div className="bg-white p-3 rounded border border-green-200">
                  <p className="text-sm text-gray-600">Modelo</p>
                  <p className="font-semibold text-gray-900">{result.model}</p>
                </div>
                <div className="bg-white p-3 rounded border border-green-200">
                  <p className="text-sm text-gray-600">Duración</p>
                  <p className="font-semibold text-gray-900">{formatDuration(result.duration_seconds)}</p>
                </div>
                <div className="bg-white p-3 rounded border border-green-200">
                  <p className="text-sm text-gray-600">Chunks</p>
                  <p className="font-semibold text-gray-900">{result.chunks_processed}</p>
                </div>
                <div className="bg-white p-3 rounded border border-green-200">
                  <p className="text-sm text-gray-600">Archivo</p>
                  <p className="font-semibold text-gray-900 truncate">{result.filename}</p>
                </div>
              </div>

              <div className="bg-white p-4 rounded border border-green-200">
                <h3 className="font-bold text-gray-900 mb-3">📝 Texto transcrito:</h3>
                <p className="text-gray-800 leading-relaxed whitespace-pre-wrap">
                  {result.transcription}
                </p>
              </div>

              <div className="mt-4 flex flex-wrap gap-3">
                <button
                  onClick={() => {
                    const text = result.transcription
                    navigator.clipboard.writeText(text)
                    alert('Transcripción copiada al portapapeles')
                  }}
                  className="bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded transition"
                >
                  📋 Copiar
                </button>
                <button
                  onClick={downloadAsTxt}
                  className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded transition"
                >
                  📄 Descargar como TXT
                </button>
                <button
                  onClick={downloadAsDocx}
                  className="bg-purple-600 hover:bg-purple-700 text-white font-bold py-2 px-4 rounded transition"
                >
                  📋 Descargar como DOCX
                </button>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}
