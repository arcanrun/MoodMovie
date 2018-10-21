import sys
from view.interfaces.IObserver import IObserver


class CLIView(IObserver):
    def __init__(self, model, controller):
        self.model = model
        self.controller = controller

    def update(self):
        pass

    def main_menu(self):
        print(
"""
1. Choose movie
2. Bookmarks
3. Exit
"""
        )
        n = input()
        dict = {
            '1': self.mood_movie_menu,
            '2': self.duty_menu,
            '3': self.exit_app

        }
        dict.get(n, self.main_menu)()

    def mood_movie_menu(self):
        print("HELLO! WHAT EMOTIONS DO YOU WANT TO FEEL?")

        print(
"""
1. Laugh 
2. Sad
3. Fear, horror
4. Joy, fun
5. Dive into the world of fantasy
6. Family evening
7. Evening with girlfriend \ boyfriend
8. Excitement, drive, save the world, breathtaking
9. Western 
10.Tension
11. Back to main menu
	
"""
        )
        n = input()
        dict = {
            '1': [35],  # comedy
            '2': [18, 10752],  # drama, war
            '3': [80, 27, 53, 9648],  # Crime Horror Thriller Mystery
            '4': [16, 35],  # Animation Comedy
            '5': [14, 878],  # Fantasy, Science Fiction
            '6': [10751, 16],  # Family Animation[adult = FALSE]!!!!!
            '7': [10749],  # Romance
            '8': [28, 12],  # Action, Adventure
            '9': [37],  # Western"
            '10':[10752]  # War


        }

        try:
            chosen_movie = dict[n]
            movie = self.model.get_movie_from_api(chosen_movie)
            self.template_view_movie(movie)
            self.mood_movie_menu()
        except KeyError:
            self.main_menu()

    def duty_menu(self):
        self.main_menu()

    def exit_app(self):
        sys.exit('See Ya!')

    def template_view_movie(self, movie):
        border = '.'
        upper_border = border * 40
        footer_border = len(upper_border) * border
        print(upper_border)
        print('==TITLE==')
        print(movie['title'])
        print('==overview'.upper() + '==')
        text = movie['overview']
        for i in range(0, len(text), len(upper_border)):
            if i % len(upper_border) == 0:
                text = text[:i] + '\n' + text[i:]
        print(text)
        print('==URL==')
        print(movie['url_movie'])
        print(footer_border)