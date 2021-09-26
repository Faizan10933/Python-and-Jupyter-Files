from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader

class SoundPlayer(BoxLayout):
    def play_sound(self):
        sound = SoundLoader.load('audio.mp3')
        if sound:
            sound.play()

class SndApp(App):
    def build(self):
        return SoundPlayer()
SndApp().run()