from kivy.app import App
from kivy.uix.image import Image

class MyImage(Image):
    pass

class MyApp(App):
    def build(self):
        return MyImage()

MyApp().run()