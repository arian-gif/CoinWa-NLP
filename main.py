from speech_to_text import SpeechToText
import time
from text_to_speech import TextToSpeech
import sounddevice as sd

# STT = SpeechToText()
#
# while True:
#     text = STT.recognize_speech_from_mic()
#     if text:
#         print("You said:", text)
#     time.sleep(1)


TTS=TextToSpeech()
output = TTS.speak("Testing 123456")

waveform = output["audio"]
sample_rate = output["sampling_rate"]

sd.play(waveform, samplerate=sample_rate)
sd.wait()




