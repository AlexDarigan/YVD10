from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder
from kivy.properties import NumericProperty
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('playmat/components/hand.kv')

class Hand(BoxLayout):
    hand_x = NumericProperty(0.55, rebind=True)
    hand_move_left = False
    big_hand = False
    card_spacing = NumericProperty(-35, rebind=True)

    # def draw_test(self):
    #     print('old', self.spacing)
    #     self.cols += 1
    #     self.size_hint_x += 0.08
    #     if self.hand_move_left:
    #         self.hand_move_left = False
    #         self.pos_hint['center_x'] += 0.05
    #     else:
    #         self.hand_move_left = True
    #         self.pos_hint['center_x'] -= 0.05
    #     self.card_spacing -= .05
    #     self.add_widget(self.parent.PlayerOne.main_deck.pop(0))
    #     print('new', self.spacing)

    def draw(self):
        self.size_hint_x += .1
        self.add_widget(self.parent.PlayerOne.main_deck.pop(0))