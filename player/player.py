from kivy.lang.builder import Builder
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import StringProperty

Builder.load_file('player/player.kv')

class ContextMenu(Popup):
    art = StringProperty('images/basicback.jpg', rebind=True)

class ZoneMenu(Popup):
    pass

class Player:
    def __init__(self, name, avatar, main_deck, extra_deck, side_deck):
        self.name = name
        self.avatar = avatar
        self.main_deck = main_deck
        self.extra_deck = extra_deck
        self.side_deck = side_deck
        self.graveyard = []
        self.banished = []
        self.active_card = None
        self.ContextMenu = ContextMenu()
        self.ZoneMenu = ZoneMenu()

    @property
    def playmat(self):
        return App.get_running_app().root.ids.controller.get_screen('PLAYMAT')
        
    @property
    def monster_zones(self):
        return self.playmat.ids.my_monster_zones
        
    @property
    def support_zones(self):
        return self.playmat.ids.my_support_zone
    
    @property
    def active_card_in_array(self):
        if any(self.active_card for deck in [self.main_deck, self.graveyard, self.extra_deck]):
            return False
        return True

    def open_context_menu(self):
        self.ContextMenu.source = self.active_card.art
        self.ContextMenu.open()

    def summon_or_play_card(self):
        i = 1
        for child in self.monster_zones.children:
            Zone = Button(text=(str(i)))
            Zone.bind(on_release=self.summon)
            self.ZoneMenu.ids.choices.add_widget(Zone)
            i += 1
        self.ContextMenu.dismiss()
        self.ZoneMenu.open()

    def remove_from_parent(self): 
        try:
            self.active_card.parent.remove_widget(self.active_card)
        except: # Catch explicit errors
            pass
        invisble_zones = [self.main_deck, self.graveyard, self.extra_deck]
        for zone in invisble_zones:
            if self.active_card in zone:
                zone.remove(self.active_card)
                return

    def summon(self, Button):
        self.ZoneMenu.dismiss()
        self.remove_from_parent()
        self.active_card.pos_hint = {'x': 0, 'y': 0}
        self.monster_zones.ids[Button.text].add_widget(self.active_card)
        self.ZoneMenu.ids.choices.clear_widgets()

    def set_card(self):
        pass

    def send_to_area(self, area):
        self.remove_from_parent()
        if area == 'graveyard':
            self.graveyard.append(self.active_card)
            self.playmat.ids.my_discard.background_normal = self.active_card.art
        elif area == 'banish':
            self.banished.append(self.active_card)
        elif area == 'topdeck':
            if self.active_card.is_extra():
                self.extra_deck.append(self.active_card)
            else:
                self.main_deck.insert(0, self.active_card)
        elif area == 'bottomdeck':
            self.main_deck.append(self.active_card)
        self.ContextMenu.dismiss()

    def search_area(self, area):
        pass
        # NOTE: SEARCH FUNCTIONS CAN BE ONE WITH PARAMETERS
        # open pop up
        # pop up contains gridlayout inside scrollview with a bunch of cards
        # cards open a context menu inside here

    def shuffle_deck(self):
        pass
        # Fisher Yates algorithim

    