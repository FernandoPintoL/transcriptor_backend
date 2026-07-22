"""
Script para probar la API de transcripción
Uso: python test_api.py <ruta_a_archivo_audio>
"""

import requests
import sys
import os

API_URL = "http://localhost:8000"

def test_health():
    """Prueba que el servidor esté funcionando"""
    print("🔍 Probando health check...")
    try:
        response = requests.get(f"{API_URL}/health")
        print(f"✅ Servidor está funcionando: {response.json()}")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_models():
    """Obtiene los modelos disponibles"""
    print("\n📋 Modelos disponibles:")
    try:
        response = requests.get(f"{API_URL}/models")
        data = response.json()
        print(f"Modelo actual: {data['current_model']}")
        print(f"Modelos: {', '.join(data['available_models'])}")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_transcribe(file_path):
    """Transcribe un archivo de audio"""
    if not os.path.exists(file_path):
        print(f"❌ Archivo no encontrado: {file_path}")
        return False

    print(f"\n🎵 Transcribiendo: {file_path}")
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            response = requests.post(f"{API_URL}/transcribe", files=files)

        if response.status_code == 200:
            data = response.json()
            print(f"✅ Transcripción completada")
            print(f"Duración: {data['duration_seconds']:.2f} segundos")
            print(f"Chunks procesados: {data['chunks_processed']}")
            print(f"\n📝 Transcripción:\n{data['transcription']}")
            return True
        else:
            print(f"❌ Error: {response.json()}")
            return False

    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("TRANSCRIPTOR API - TESTING")
    print("=" * 50)

    # Test health
    if not test_health():
        print("\n⚠️  Asegúrate que el servidor esté corriendo: python main.py")
        sys.exit(1)

    # Test models
    test_models()

    # Test transcribe
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        test_transcribe(file_path)
    else:
        print("\n💡 Uso: python test_api.py <archivo_audio>")
        print("   python test_api.py audio.mp3")
