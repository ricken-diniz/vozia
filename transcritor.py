import whisper
import time

def transcritor(audio_path):
    model = whisper.load_model("small")  # pode ser 'base', 'small', 'medium', 'large'
    result = model.transcribe(audio_path)
    print(f'Audio transcrito: {result['text']}')
    return result["text"]

def main():
    # Carrega o modelo (por padrão ele busca em ~/.cache/whisper)
    model = whisper.load_model("small")  # pode ser 'base', 'small', 'medium', 'large'

    # Caminho do arquivo de áudio
    audio_path = "WhatsApp Ptt 2025-07-17 at 10.40.31.mp3"


    start_time = time.time()
    # Transcreve o áudio
    result = model.transcribe(audio_path)

    elapsed_time = time.time() - start_time

    # Mostra o texto transcrito
    print("Transcrição:")
    print(result["text"]+'\n')
    print(f'Tempo de execução: {elapsed_time:.2f} segundos.')

if __name__ == '__main__':
    main()