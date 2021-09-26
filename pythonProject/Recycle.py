from kivy.app import App
from kivy.uix.recycleview import RecycleView

class RV(RecycleView):
    def __init__(self):
        super().__init__()
        content=['hello','button 2','button 3']
        self.data = [{'text':item} for item in content]

class RecApp(App):
    def build(self):
        return RV()
RecApp().run()