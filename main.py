from view.CLIView import CLIView
from model.MoodMovieModel import MoodMovieModel
from model.facade.FacadeMoodMovie import FacadeMoodMovie
from model.facade.subsystem.DBShelve import DBShelve
from model.facade.subsystem.MovieSelectorTheMovieDborg import MovieSelectorTheMovieDborg
from controller.ControllerMoodMovie import ControllerMoodMovie


"""
The progarm is made for educational purposes (TDD, SOLID, DesignPatterns, MVC pattern)
"""
def app(view):
    view.main_menu()
    app(view)
if __name__ == '__main__':
    db = DBShelve()
    movie_selector = MovieSelectorTheMovieDborg()
    facade = FacadeMoodMovie(movie_selector, db)
    model = MoodMovieModel(facade)
    controller = ControllerMoodMovie(model)
    view = CLIView(model, controller)


    app(view)
