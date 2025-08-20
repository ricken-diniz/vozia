import whisper
import time

def transcritor(audio_path):
    start_time = time.time()

    model = whisper.load_model("small", 'cpu')  
    result = model.transcribe(audio_path)

    print(f'Audio transcrito: {result["text"]}\n Tempo de execução: {time.time() - start_time:.2f} segundos.')

    return result["text"]
