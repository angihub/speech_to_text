from vosk import Model, KaldiRecognizer
import wave
import os

def speech_to_text(input_audio):
    # Путь к модели
    model_path = r"C:\Users\User\Desktop\vg\voice_messages\vosk-model-small-ru-0.22"

    # Проверка существования папки с моделью
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Папка модели не найдена: {model_path}")

    # Загрузка модели
    model = Model(model_path)
    if not model:
        raise ValueError("Не удалось загрузить модель. Проверьте содержимое папки.")

    # Конвертация аудио
    os.system(f"ffmpeg -i \"{input_audio}\" -ar 16000 -ac 1 input_audio.wav")

    # Распознавание
    with wave.open("input_audio.wav", "rb") as wf:
        rec = KaldiRecognizer(model, wf.getframerate())
        
        while True:
            data = wf.readframes(16000)
            if not data:
                break
            if rec.AcceptWaveform(data):
                print(rec.Result())

        # Получение финального результата
        print(rec.FinalResult())
    os.remove("input_audio.wav")


speech_to_text(r"C:\Users\User\Desktop\vg\voice_messages\example_voices\voice_30-05-2025_15-27-27.ogg")
