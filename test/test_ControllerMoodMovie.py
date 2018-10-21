import unittest
from model.MoodMovieModel import MoodMovieModel
from model.facade.FacadeMoodMovie import FacadeMoodMovie
from model.facade.subsystem.MovieSelectorTheMovieDborg import MovieSelectorTheMovieDborg
from model.facade.subsystem.DBShelve import DBShelve

from controller.ControllerMoodMovie import ControllerMoodMovie


class ControllerMoodMovieTest(unittest.TestCase):
    def setUp(self):
        self.db = DBShelve()
        self.movie_selector = MovieSelectorTheMovieDborg()
        self.facade = FacadeMoodMovie(self.movie_selector, self.db)
        self.model = MoodMovieModel(self.facade)

        self.controler = ControllerMoodMovie(self.model)

    def test_on_adding_bookmark_and_deleteing_all_db(self):
        test_movie = {
            'vote_count': 12,
            'id': 217008,
            'video': False,
            'vote_average': 5.3,
            'title': 'Madly in Love',
            'popularity': 1.015,
            'poster_path': '/owODdPSAhriSG5mXMAUlma5QPP4.jpg',
            'original_language': 'nl',
            'original_title': 'Smoorverliefd',
            'genre_ids': [35, 10749],
            'backdrop_path': '/gCOYVoavGlWxFgO64tvHBvmMVKH.jpg',
            'adult': False,
            'overview': "The film focuses on the tumultuous romance in the lives of four women in The Hague. Teenage daughter Eva, her mother Judith, aunt Barbara and older sister Anna make it under one roof Hague together a nice game of. They are beautiful, courageous and sensible, but sometimes they just do not know in a world full of tender love, serial dating, slaked lust, affairs, children's desires and indestructible old loves.",
            'release_date': '2013-09-12',
            'url_movie': 'https://www.themoviedb.org/movie/217008'
        }

        test_movie_2 = {
            'vote_count': 12,
            'id': 217008,
            'video': False,
            'vote_average': 5.3,
            'title': 'TEST_2',
            'popularity': 1.015,
            'poster_path': '/owODdPSAhriSG5mXMAUlma5QPP4.jpg',
            'original_language': 'nl',
            'original_title': 'Smoorverliefd',
            'genre_ids': [35, 10749],
            'backdrop_path': '/gCOYVoavGlWxFgO64tvHBvmMVKH.jpg',
            'adult': False,
            'overview': "The film focuses on the tumultuous romance in the lives of four women in The Hague. Teenage daughter Eva, her mother Judith, aunt Barbara and older sister Anna make it under one roof Hague together a nice game of. They are beautiful, courageous and sensible, but sometimes they just do not know in a world full of tender love, serial dating, slaked lust, affairs, children's desires and indestructible old loves.",
            'release_date': '2013-09-12',
            'url_movie': 'https://www.themoviedb.org/movie/217008'
        }

        self.controler.add_to_bookmarks(test_movie)
        self.controler.add_to_bookmarks(test_movie_2)
        arr_moives = self.model.get_all_movies_from_bookmarks()

        self.assertEqual(arr_moives[0][1]['title'], test_movie['title'])
        self.assertEqual(arr_moives[1][1]['title'], test_movie_2['title'])

        self.controler.clear_all_bookmarks()