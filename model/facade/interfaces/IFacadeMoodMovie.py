import abc


class IFacadeMoodMovie(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_movie_from_api(self, ids_genres):
        pass

    @abc.abstractmethod
    def add_to_db(self, movie):
        pass

    @abc.abstractmethod
    def change_movie(self, movie, id):
        pass

    @abc.abstractmethod
    def get_movie_from_bd(self, id):
        pass

    @abc.abstractmethod
    def clear_db(self):
        pass

    @abc.abstractmethod
    def add_mark_scratch(self, movie, mark):
        pass

    @abc.abstractmethod
    def add_mark_db(self, id, mark):
        pass

    @abc.abstractmethod
    def has_bookmark(self, movie_id_api):
        pass

    @abc.abstractmethod
    def has_mark(self, movie_id_api):
        pass

    @abc.abstractmethod
    def get_all_movies_from_bookmarks(self):
        pass

    @abc.abstractmethod
    def delete_bookmark(self, id):
        pass