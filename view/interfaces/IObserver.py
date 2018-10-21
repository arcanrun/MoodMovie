import abc


class IObserver(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, msg):
        pass