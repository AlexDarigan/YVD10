from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from card import Card

Builder.load_file('components/card_viewer.kv')

class CardViewer(BoxLayout):
    viewing = ObjectProperty(Card(art='images/basicback.jpg', effect=''), rebind=True)
