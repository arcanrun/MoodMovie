from .interfaces.IMoodMovieModel import IMoodMovieModel


class MoodMovieModel(IMoodMovieModel):
    def __init__(self, facade):
        self.facade = facade
        self.subscribers = []

    def subscribe(self, observer):
        self.subscribers.append(observer)

    def unsubscribe(self, movie):
        self.subscribers.remove(movie)

    def notify_subscribers(self, msg):
        for i in self.subscribers:
            i.update(msg)

    def get_movie_from_api(self, ids_genres):
        return self.facade.get_movie_from_api(ids_genres)

    def get_movie_from_bookmarks(self, id):
        return self.facade.get_movie_from_bd(id)

    def add_to_bookmarks(self, movie):
        self.facade.add_to_db(movie)

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

    def get_all_movies_from_bookmarks(self):
        return self.facade.get_all_movies_from_bookmarks()

    def delete_bookmark(self, id):
        msg = self.facade.delete_bookmark(id)
        self.notify_subscribers(msg)