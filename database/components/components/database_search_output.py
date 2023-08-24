from kivy.lang.builder import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty, NumericProperty
from card import Card
from kivy.uix.stacklayout import StackLayout

Builder.load_file('database/components/database_search_output.kv')

class DataBaseSearchOutput(StackLayout):
    results = ListProperty()
    page_count = NumericProperty()
    card_index = NumericProperty(0)

    def show_search_results(self):
        self.page_count = len(self.results) // 50
        self.show_page()

    def show_page(self):
        self.ids.content.clear_widgets()
        for index in range(self.card_index, self.card_index + 50):
            try:
                self.ids.content.add_widget(Card(**self.results[index]))
            except IndexError:
                self.page_count - 1
                return

    def show_previous_page(self):
        if self.card_index - 50 < 0:
            return
        elif self.card_index -50 >= 0:
            self.card_index -= 50
            self.show_page()

    def show_next_page(self):
        if self.card_index + 50 > len(self.results):
            return
        else:
            self.card_index += 50
            self.show_page()
