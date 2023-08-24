from time import sleep
import socket

from kivy.lang.builder import Builder
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.progressbar import ProgressBar

from player.player import Player
from card import Card

Builder.load_file('session/session.kv')

class Session(Popup):
    socket = socket.socket()
    client = None
    is_server = False
    listening = False

    def create_player(self):
        playmat = App.get_running_app().root.ids.controller.get_screen('PLAYMAT')
        deckbuilder = App.get_running_app().root.ids.controller.get_screen('DECKBUILDER').ids.deck_displays
        main = [card.copy_self() for card in deckbuilder.ids.main_deck.children]
        side = [card.copy_self() for card in deckbuilder.ids.side_deck.children]
        extra = [card.copy_self() for card in deckbuilder.ids.extra_deck.children]
        player_one = Player('PlayerOne', None, main, side, extra)
        playmat.PlayerOne = player_one

    def bind_host(self):
        self.listening = True
        self.socket.setblocking(0)
        self.socket.bind((self.ids.ip.text, int(self.ids.port.text)))
        self.socket.listen(1)
        self.ids.log.text = 'Listening for Connection'

    def listen(self):

        try:
            connection, address = self.socket.accept()
            self.ids.log.text = '\nConnection from:\n ' + str(address)
            self.ids.signal.value = 0
            confirmation = 'Thank you for connecting'
            connection.send(confirmation.encode())
            self.client = connection
            self.listening = False
            self.is_server = True

        except socket.error:
            return None

        self.create_player()
        print('player connected')

    def connect(self):
        self.is_server = False
        self.socket.connect((self.ids.ip.text, int(self.ids.port.text)))
        self.ids.log.text = str(self.socket.recv(1024).decode())
        self.socket.setblocking(0)
        self.create_player()

    def send(self):
        playmat = App.get_running_app().root.ids.controller.get_screen('PLAYMAT')
        message_input = playmat.ids.chat.ids.message_input
        message_output = playmat.ids.chat.ids.message_output

        mail = message_input.text
        message_output.text += '\nYou: ' + mail
        message_input.text = ''

        if self.is_server:
            self.client.send(mail.encode())

        elif not self.is_server:
            self.socket.send(mail.encode())

    def receive(self):
        playmat = App.get_running_app().root.ids.controller.get_screen('PLAYMAT')
        message_output = playmat.ids.chat.ids.message_output

        try:
            if self.is_server:
                message_output.text += '\nOpp: ' + str(self.client.recv(1024).decode())

            elif not self.is_server:
                message_output.text += '\nOpp: ' + str(self.socket.recv(1024).decode())

        except socket.error:
            pass
