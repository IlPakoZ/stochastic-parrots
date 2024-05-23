import pyttsx3


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

if __name__=='__main__':
    Speaking = SpeakNow()
    text = "4Chan is the best forum"
    voices = Speaking.tts_engine.getProperty('voices')
    
    for voice in voices: 
        print(f"Vice: {voice.name} ({voice.id})")    
        Speaking.handle_user_input(text)

