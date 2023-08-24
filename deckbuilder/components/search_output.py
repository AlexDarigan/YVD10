from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty, ListProperty

from card import Card

Builder.load_file('deckbuilder/components/search_output.kv')

class SearchOutput(FloatLayout):
    search_results = ListProperty()
    page_count = NumericProperty()
    card_index = NumericProperty(0)

    def show_search_results(self):
        self.page_count = len(self.search_results) // 9
        self.show_page()

    def show_page(self):
        self.ids.results_display.clear_widgets()
        for index in range(self.card_index, self.card_index + 9):
            try:
                self.ids.results_display.add_widget(Card(**self.search_results[index]))
            except IndexError:
                return

    def show_next_page(self):
        if self.card_index + 9 > len(self.search_results):
            return
        self.card_index += 9
        self.show_page()

    def show_previous_page(self):
        if self.card_index - 9 < 0:
            return
        self.card_index -= 9
        self.show_page()