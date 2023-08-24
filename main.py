'''YVD10'''

__version__ = "0.1"

# Standard Imports
# from pickle import load
from json import load

# Kivy Imports
from kivy.config import Config
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import FadeTransition
from kivy.uix.progressbar import ProgressBar

# Config
Config.set('graphics', 'height', 720)
Config.set('graphics', 'width', 1280)
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

# My Modules
from playmat.playmat import PlayMat
from components.card_viewer import CardViewer
from session.session import Session
from database.database import DataBase
from deckbuilder.deckbuilder import DeckBuilder

class Master(FloatLayout):

    def update(self, gragh):
        session = App.get_running_app().session
        session.receive()
        if session.listening:
            session.listen()
            if session.ids.signal.value < 100:
                session.ids.signal.value += 10
                return
            session.ids.signal.value = 0

class YVD10(App):

    def build(self):
        MasterGame = Master()
        self.session = Session()
        MasterGame.ids.controller.transition = FadeTransition()

        try:

            decklists = MasterGame.ids.controller.get_screen('DECKBUILDER').ids.deck_options.ids.deck_list.values
            [decklists.append(card) for card in load(open('decks/decklist.json', 'r')).values()]

        except EOFError:
            pass

        except FileNotFoundError:
            pass

        Clock.schedule_interval(MasterGame.update, .05)
        return MasterGame

    def connect(self):
        self.session.open()

    def close(self):
        self.session.dismiss()

if __name__ == '__main__':
    YVD10().run()