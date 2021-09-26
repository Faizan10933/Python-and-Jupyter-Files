from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
import pygame

class MyApp(App):
    def build(self):
        layout= BoxLayout(orientation='vertical')
        label1 = Label(text="Hello Faizan", size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        label2 = Label(text="Welcome to Kiwi", size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        button =Button(text="press me", size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5, 'center_y':0.5})
        layout.add_widget(label1)
        layout.add_widget(label2)
        layout.add_widget(button)

        return layout
if __name__=='__main__':
    MyApp().run()