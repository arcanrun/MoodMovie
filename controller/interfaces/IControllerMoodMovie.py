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