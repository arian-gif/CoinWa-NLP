from transformers import pipeline

class TextToSpeech:
    def __init__(self):
        self.pipe = pipeline("text-to-speech", model="suno/bark-small", device=0)

    def speak(self, text: str):
        audio = self.pipe(text)
        return audio
