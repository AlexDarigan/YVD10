from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty

from deckbuilder.components.search_output import SearchOutput


Builder.load_file('deckbuilder/components/search_input.kv')

class SearchInput(FloatLayout):

    def get_search_results(self):
        database = App.get_running_app().root.ids.controller.get_screen('DATABASE').ids.database_searchinput
        display = App.get_running_app().root.ids.controller.get_screen('DECKBUILDER').ids.search_output
        display.search_results = database.search(**{k: self.ids[k].text for k in self.ids})
        display.show_search_results()
