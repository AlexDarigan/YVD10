from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.properties import NumericProperty, DictProperty
from playmat.components.chat import Chat
from playmat.components.card_zone_layout import CardZone
from playmat.components.card_zone_layout import CardZoneLayout
from kivy.properties import ObjectProperty
from card import Card
from playmat.components.hand import Hand

Builder.load_file('playmat/playmat.kv')

class PlayMat(Screen):
    PlayerOne = ObjectProperty(rebind=True)
    PlayerTwo = None
    
    
  