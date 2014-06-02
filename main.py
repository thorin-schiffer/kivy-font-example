from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty, ObjectProperty
from glob import glob 
from os.path import dirname, join, basename
from kivy.core.text import Label
from kivy.core.text import LabelBase


from kivy.core.text import LabelBase
KIVY_FONTS = [
    {
        "name": "RobotoCondensed",
        "fn_regular": "data/fonts/RobotoCondensed-Light.ttf",
        "fn_bold": "data/fonts/RobotoCondensed-Regular.ttf",
        "fn_italic": "data/fonts/RobotoCondensed-LightItalic.ttf",
        "fn_bolditalic": "data/fonts/RobotoCondensed-Italic.ttf"
    }
]
    
for font in KIVY_FONTS:
    LabelBase.register(**font)


class Phone(FloatLayout):
        pass

class TestApp(App):
    def build(self):
        return Phone()

if __name__ == '__main__':
    TestApp().run() 
