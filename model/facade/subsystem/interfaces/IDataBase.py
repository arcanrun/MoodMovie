import abc


class IDataBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_item(self, item):
        pass

    @abc.abstractmethod
    def get_item(self, id):
        pass

    @abc.abstractmethod
    def clear_db(self):
        pass

    @abc.abstractmethod
    def change_item(self, item, id):
        pass

    @abc.abstractmethod
    def has_item(self, sign):
        pass

    @abc.abstractmethod
    def has_mark(self, sign):
        pass