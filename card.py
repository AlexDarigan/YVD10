from kivy.app import App
from kivy.lang.builder import Builder
from kivy.properties import NumericProperty, StringProperty, DictProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

Builder.load_file('card.kv')

class Card(ButtonBehavior, Image):
    title = StringProperty()
    pack = StringProperty()
    art = StringProperty()
    main_type = StringProperty()
    sub_type = StringProperty()
    color_type = StringProperty()
    special_type = StringProperty()
    tribe = StringProperty()
    attribute = StringProperty()
    stars = NumericProperty()
    attack = NumericProperty()
    defense = NumericProperty()
    effect = StringProperty()


    def get_card_dict(self):
        return {
            'title': self.title,
            'pack': self.pack,
            'art': self.art,
            'main_type': self.main_type,
            'sub_type': self.sub_type,
            'color_type': self.color_type,
            'special_type': self.special_type,
            'tribe': self.tribe,
            'attribute': self.attribute,
            'stars': self.stars,
            'attack': self.attack,
            'defense': self.defense,
            'effect': self.effect}

    def copy_self(self):
        return Card(**self.get_card_dict())

    @property
    def deckbuilder(self):
        deckbuilder = App.get_running_app().root.ids.controller.get_screen('DECKBUILDER')
        return deckbuilder
        
    def main_deck(self):
        main_deck = self.deckbuilder.ids.deck_displays.ids.main_deck
        return main_deck

    def side_deck(self):
        side_deck = self.deckbuilder.ids.deck_displays.ids.side_deck
        return side_deck

    def extra_deck(self):
        extra_deck = self.deckbuilder.ids.deck_displays.ids.extra_deck
        return extra_deck

    def card_commands(self):
        player_one = App.get_running_app().root.ids.controller.get_screen('PLAYMAT').PlayerOne
        current_screen = App.get_running_app().root.ids.controller.current_screen
        current_screen.ids.card_viewer.viewing = self
        x = self.copy_self()
        print(self.last_touch.button)
        print(self.pos)
        print(self.size)

        if current_screen.name == 'DECKBUILDER':
            if self not in current_screen.ids.search_output.ids.results_display.children:
                self.parent.remove_widget(self)

            elif self.player_left_clicked() and self.is_extra():
                    self.extra_deck().add_widget(x)

            elif self.player_left_clicked():
                self.main_deck().add_widget(x)

            elif self.player_right_clicked():
                self.side_deck().add_widget(x)

            else:
                pass

        elif current_screen.name == 'PLAYMAT' and self.player_right_clicked:
            player_one.active_card = self
            player_one.ContextMenu.art = self.art
            player_one.open_context_menu()

    def player_right_clicked(self):
        if self.last_touch.button == 'right': return True

    def player_left_clicked(self):
        if self.last_touch.button == 'left': return True

    def is_monster(self):
        if self.main_type == 'Monster': return True

    def is_spell(self):
        if self.main_type == 'Spell': return True

    def is_trap(self):
        if self.main_type == 'Trap': return True

    def is_extra(self):
        if self.color_type != 'Nil': return True

    def is_field(self):
        if self.sub_type == 'Field': return True

    def is_xyz(self):
        if self.color_type == 'Xyz': return True

    # Implement Properties
    # Implement Evaluation Checks
    # Create Player Class to use checks
    # Implement on press set to active card / pop ups?
    # active_card is a player property
    # Have two players in game
    # One Player is created from sockets on connection, might take a while, use a loading screen?
