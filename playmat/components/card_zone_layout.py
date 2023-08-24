from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder
from kivy.uix.image import Image

Builder.load_file('playmat/components/card_zone_layout.kv')

class CardZone(FloatLayout, Image):
    pass

class CardZoneLayout(FloatLayout):
    pass
