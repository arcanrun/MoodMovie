import abc


class IMoodMovieModel(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def subscribe(self):
        pass

    @abc.abstractmethod
    def unsubscribe(self):
        pass

    @abc.abstractmethod
    def get_movie_from_api(self, ids_genres):
        pass

    @abc.abstractmethod
    def add_to_bookmarks(self, moive):
        pass

    @abc.abstractmethod
    def get_movie_from_bookmarks(self, id):
        pass

    @abc.abstractmethod
    def clear_all_bookmarks(self):
        pass

    @abc.abstractmethod
    def add_mark_scratch(self, movie, scratch):
        pass

    @abc.abstractmethod
    def add_mark_db(self, id, mark):
        pass

    @abc.abstractmethod
    def has_bookmark(self, movie_id_api):
        pass

    @abc.abstractmethod
    def has_marks(self, movie_id_api):
        pass

