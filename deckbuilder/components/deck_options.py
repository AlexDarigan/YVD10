import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout

from card import Card

Builder.load_file('deckbuilder/components/deck_options.kv')

class DeckOptions(BoxLayout):

    @property
    def decks(self):
        return App.get_running_app().root.ids.controller.get_screen('DECKBUILDER').ids.deck_displays

    def save_deck(self):
        name = self.ids.name_deck.text
        list_of_decks = self.ids.deck_list.values

        main = {k: card.get_card_dict() for k, card in enumerate(self.decks.ids.main_deck.children)}
        extra = {k: card.get_card_dict() for k, card in enumerate(self.decks.ids.extra_deck.children)}
        side = {k: card.get_card_dict() for k, card in enumerate(self.decks.ids.side_deck.children)}
        deck = {'Main': main, 'Extra': extra, 'Side': side}
        dict_of_decks = {k: v for k, v in enumerate(list_of_decks)}

        if name not in list_of_decks:
            list_of_decks.append(name)

        with open('decks/' + name + '.json', 'w') as decklist:
            json.dump(deck, decklist)

        with open('decks/decklist.json', 'w') as saved_list_of_decks:
            json.dump(dict_of_decks, saved_list_of_decks)
        
    def load_deck(self):
        name = self.ids.deck_list.text
        for display in self.decks.ids:
            self.decks.ids[display].clear_widgets()

        with open('decks/' + name + '.json', 'r') as decklist:
            deck = json.load(decklist)

            for card_dict in deck['Main'].values():
                self.decks.ids.main_deck.add_widget(Card(**card_dict))

            for card_dict in deck['Extra'].values():
                self.decks.ids.extra_deck.add_widget(Card(**card_dict))

            for card_dict in deck['Side'].values():
                self.decks.ids.side_deck.add_widget(Card(**card_dict))