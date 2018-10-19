from .interfaces.IFacadeMoodMovie import IFacadeMoodMovie


class FacadeMoodMovie(IFacadeMoodMovie):
    def __init__(self, movie_selector, db):
        self.movie_selector = movie_selector
        self.db = db

    def get_movie_from_api(self, ids_genres):
        return self.movie_selector.get_movie(ids_genres)

    def add_to_db(self, movie):
        self.db.add_item(movie)

    def change_movie(self, movie, id):
        self.db.change_item(movie, id)

    def get_movie_from_bd(self, id):
        return self.db.get_item(id)

    def clear_db(self):
        self.db.clear_db()

    def add_mark_scratch(self, movie, mark):
        movie['your_mark'] = int(mark)
        self.add_to_db(movie)

    def add_mark_db(self, id, mark):
        movie = self.get_movie_from_bd(id)
        movie['your_mark'] = int(mark)

        self.change_movie(movie, id)

    def has_bookmark(self, movie_id_api):
        return self.db.has_item(movie_id_api)

    def has_mark(self, movie_id_api):
        return self.db.has_mark(movie_id_api)
