from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ListProperty
from card import Card
import sqlite3
import csv
from database.components.database_search_input import DataBaseSearchInput
from kivy.uix.image import Image
from database.components.database_search_output import DataBaseSearchOutput
from components.card_viewer import CardViewer


Builder.load_file('database/database.kv')

class DataBase(Screen):

    def connect_to_card_database(self):

        try:
            conn = sqlite3.connect('database/CardLibrarySQL.db')
            conn.row_factory = sqlite3.Row
            return conn

        except sqlite3.Error as error:
            print(error)

    def add_from_csv(self):
        conn = self.connect_to_card_database()

        
        try:
            card_data = [row for row in csv.reader(open('database/' + self.ids.csv_address.text, 'r'))]
            print(card_data)
        except FileNotFoundError:
            self.ids.csv_address.text = 'Error: File Not Found'
            return
        
        for col in card_data:
            if col[9] == 'Nil':
                col[9] = 0.0
            if col[10] == 'Nil':
                col[10] = 0.0
            if col[11] == 'Nil':
                col[11] = 0.0

        conn.execute("INSERT INTO cards VALUES (:title, :pack, :art, :main_type, :sub_type, :color_type, :special_type, :attribute, :tribe, :stars, :attack, :defense, :effect)", 
        {'title': col[0], 'pack': col[1], 'art': col[2],  'main_type': col[3], 'sub_type': col[4], 'color_type': col[5], 'special_type': col[6], 'attribute': col[7], 'tribe': col[8], 'stars': float(col[9]), 'attack': float(col[10]), 'defense': float(col[11]), 'effect': col[12]})

        conn.commit()
        conn.close()