from .interfaces.IMoodMovieModel import IMoodMovieModel


class MoodMovieModel(IMoodMovieModel):
    def __init__(self, facade):
        self.facade = facade
        self.subscribers = []

    def subscribe(self):
        pass

    def unsubscribe(self):
        pass

    def get_movie_from_api(self, ids_genres):
        return self.facade.get_movie_from_api(ids_genres)

    def add_to_bookmarks(self, movie):
        self.facade.add_to_db(movie)

    def get_movie_from_bookmarks(self, id):
        return self.facade.get_movie_from_bd(id)

    def clear_all_bookmarks(self):
        self.facade.clear_db()

    def add_mark_scratch(self, movie, mark):
        self.facade.add_mark_scratch(movie, mark)

    def add_mark_db(self, id, mark):
        self.facade.add_mark_db(id, mark)

    def has_bookmark(self, movie_id_api):
        return self.facade.has_bookmark(movie_id_api)

    def has_marks(self, movie_id_api):
        return self.facade.has_mark(movie_id_api)