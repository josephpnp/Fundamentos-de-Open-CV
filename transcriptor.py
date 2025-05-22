from vosk import KaldiRecognizer
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import json

# Initialize Vosk model
model = Model(lang="es")
recognizer = KaldiRecognizer(model, 16000)  # 16kHz sample rate

# Queue for audio data
q = queue.Queue()

def callback(indata, frames, time, status):
    """Sounddevice callback to handle real-time audio chunks."""
    q.put(bytes(indata))


def transcribes():
    """Listen to audio in real-time, process with VAD, and transcribe."""
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype="int16",
                           channels=1, callback=callback):
        print("Escuchando...")
        
        while True:
            data = q.get()
            
            # Perform voice activity detection
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())['text']

            else:
                partial = json.loads(recognizer.PartialResult())['partial']
                print(partial)
        