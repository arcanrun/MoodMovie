import abc


class IControllerMoodMovie(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_to_bookmarks(self, movie):
        pass

    @abc.abstractmethod
    def add_mark_scratch(self, movie, mark):
        pass

    @abc.abstractmethod
    def clear_all_bookmarks(self):
        pass

    @abc.abstractmethod
    def delete_bookmark(self, id):
        pass

    @abc.abstractmethod
    def add_mark_db(self, id, mark):
        pass
