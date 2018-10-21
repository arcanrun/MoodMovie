import sys
from view.interfaces.IObserver import IObserver


class CLIView(IObserver):
    def __init__(self, model, controller):
        self.model = model
        self.controller = controller
        self.model.subscribe(self)

    def update(self, msg):
        print('{} {} {}'.format(msg['header'], msg['status'], msg['repr']))

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
        choose_1 = input()
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
            chosen_movie = dict[choose_1]
            movie = self.get_movie_api(chosen_movie)
            self.template_view_movie(movie)
            self.template_view_movie_control_btns(chosen_movie, movie)


        except KeyError:
            self.main_menu()

    def duty_menu(self):
        print(
"""
1. Show my bookmarks 
2. Remove bookmark
3. Change marks
4. Delete all bookmarks
5. Back
"""
        )
        choose_1 = input()
        dict = {
            '1': self.get_all_movies_from_bookmarks,
            '4': self.clear_all_bookmarks,
            # '3': self.add_mark_db
        }

        try:
            dict[choose_1]()
        except KeyError:
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

    def template_view_movie_control_btns(self, id_cataegories, movie):
        action = {
            '1': self.template_view_movie,
            '2': self.add_to_bookmarks,
            '3': self.add_mark_scratch
        }

        print('1.More | 2.Book | 3.Add mark | 4. Back')
        print('\n')
        choose_2 = input()
        try:
            if choose_2 == '1':
                inner_movie = self.get_movie_api(id_cataegories)
                action[choose_2](inner_movie)
                self.template_view_movie_control_btns(id_cataegories, inner_movie)
            else:
                action[choose_2](movie)
        except KeyError:
            self.mood_movie_menu()

    def add_to_bookmarks(self, movie):
        self.controller.add_to_bookmarks(movie)

    def add_mark_scratch(self, movie):
        print('ENTER THE MARK FOR MOVIE: {}'.format(movie['title']))
        mark = input()
        self.controller.add_mark_scratch(movie, mark)

    def get_movie_api(self, movie_category):
        return self.model.get_movie_from_api(movie_category)

    def get_all_movies_from_bookmarks(self):
        all_movies = self.model.get_all_movies_from_bookmarks()
        if len(all_movies) == 0:
            print('YOU BOOKMARKED NOTHING YET')
        else:
            for movie in all_movies:
                print()

                print('==ID: {}=='.format(movie[0]))
                self.template_view_movie(movie[1])

    def clear_all_bookmarks(self):
        print("DO YOU REALLY WANT TO DELETE ALL BOOKMARKS? [y/n]")
        n = input()
        if not n.lower() == 'y':
            self.main_menu()
        else:
            self.controller.clear_all_bookmarks()

