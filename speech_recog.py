import pyttsx3
import speech_recognition as sr
import numpy as np
import sounddevice as sd

class SpeakNow: 
    def __init__(self):
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('rate', 150)
        self.tts_engine.setProperty('volume', 1)

    def speak(self, text):
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

    def handle_user_input(self, user_input):
        response = self.generate_response(user_input)
        print("Rantbot", response)

        self.speak(response)                          

    def generate_response(self, user_input): 
        return user_input + ". What a stupid thing to say"

class UnderstandMe: 
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.sample_rate = 16000
        self.duration = 5

    def record_audio(self):
        print("recording")
        audio_data = sd.rec(int(self.duration * self.sample_rate), samplerate=self.sample_rate, channels=1, dtype='int16')
        sd.wait()
        print("recording complete")
        return audio_data
    
    def audio_to_text(self, audio_data):
        # Flatten the audio data and ensure it is in the correct format
        audio_data = audio_data.flatten()
        audio_bytes = audio_data.tobytes()
        audio = sr.AudioData(audio_bytes, self.sample_rate, 2)
        try:
            text = self.recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand the audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

## This is how you can use the two

#if __name__=='__main__':
    #Speaking = SpeakNow()
    #text = "4Chan is the best forum"
    #voices = Speaking.tts_engine.getProperty('voices')
    
    #for voice in voices: 
    #    print(f"Vice: {voice.name} ({voice.id})")    
    #    Speaking.handle_user_input(text)
    #recognize = UnderstandMe()
    #recording = recognize.record_audio()
    #text = recognize.audio_to_text(recording)
    #print(text)
