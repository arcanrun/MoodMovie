import abc


class IMovieSelector(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_movie(self, ids_movie, *args):
        pass