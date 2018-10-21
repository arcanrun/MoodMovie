from controller.interfaces.IControllerMoodMovie import IControllerMoodMovie


class ControllerMoodMovie(IControllerMoodMovie):
    def __init__(self, model):
        self.model = model

    def add_mark_scratch(self, movie, mark):
        self.model.add_mark_scratch(movie, mark)

    def add_to_bookmarks(self, movie):
        self.model.add_to_bookmarks(movie)

    def clear_all_bookmarks(self):
        self.model.clear_all_bookmarks()

    def delete_bookmark(self, id):
        self.model.delete_bookmark(id)