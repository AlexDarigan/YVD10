from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

Builder.load_file('database/components/database_search_input.kv')

class DataBaseSearchInput(BoxLayout):
    
    def search(self, **kwargs):
        for k in kwargs:
            if 'min' in k:
                if kwargs[k] == '':
                    kwargs[k] = 0
                else:
                    float(kwargs[k])
            elif 'max' in k:
                if kwargs[k] == '':
                    kwargs[k] = 9999
                else:
                    float(kwargs[k])
            elif 'max' not in k or 'min' not in k:
                kwargs[k] = '%' + kwargs[k] + '%'
            print(k, 'and', kwargs[k])

        database = App.get_running_app().root.ids.controller.get_screen('DATABASE')
        conn = database.connect_to_card_database()
        results = [result for result in (conn.execute('SELECT * FROM cards where title like ? and pack like ? and main_type like ? \
        and sub_type like ? and color_type like ? and attribute like ? and tribe like ? and special_type like ? and stars between ? and ? \
        and attack between ? and ? and defense between ? and ? and effect like ?', (kwargs['title'], kwargs['pack'], kwargs['main'], kwargs['sub'],
        kwargs['color'], kwargs['element'], kwargs['tribe'], kwargs['special'], (kwargs['min_level']), (kwargs['max_level']), kwargs['min_atk'], kwargs['max_atk'], 
        kwargs['min_def'], kwargs['max_def'], kwargs['desc'])))]

        conn.close()

        return results

    def search_and_send_to_output(self):
        display = App.get_running_app().root.ids.controller.get_screen('DATABASE').ids.database_searchoutput
        display.results = self.search(**{k: self.ids[k].text for k in self.ids if k != 'imageurl'})
        display.show_search_results()


