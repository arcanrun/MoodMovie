import unittest
from model.MoodMovieModel import MoodMovieModel
from model.facade.FacadeMoodMovie import FacadeMoodMovie
from model.facade.subsystem.MovieSelectorTheMovieDborg import MovieSelectorTheMovieDborg
from model.facade.subsystem.DBShelve import DBShelve


class ModelMoodMovieTest(unittest.TestCase):
    def setUp(self):
        self.db = DBShelve()
        self.movie_selector = MovieSelectorTheMovieDborg()
        self.facade = FacadeMoodMovie(self.movie_selector, self.db)
        self.model = MoodMovieModel(self.facade)

    def test_facade_through_model_on_showing_the_movie_by_mood_ids(self):
        ids_genres = [80, 27, 53]

        res = self.model.get_movie_from_api(ids_genres)

        self.assertIn('title', res)
        self.assertIn('vote_count', res)
        self.assertIn('id', res)
        self.assertIn('vote_average', res)
        self.assertIn('poster_path', res)
        self.assertIn('url_movie', res)

    def test_add_to_db_and_get_movie_from_db_and_clear_all_data(self):
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

        self.model.add_to_bookmarks(test_movie)
        movie_from_db = self.model.get_movie_from_bookmarks(0)

        self.assertEqual(movie_from_db['title'], test_movie['title'])

        self.model.clear_all_bookmarks()

    def test_adding_mark_for_movie_shown_from_api(self):
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

        self.model.add_mark_scratch(test_movie, 10)
        movie_from_db = self.model.get_movie_from_bookmarks(0)

        self.assertEqual(movie_from_db['your_mark'], 10)

        self.model.clear_all_bookmarks()



        self.model.add_mark_scratch(test_movie, 3)
        movie_from_db = self.model.get_movie_from_bookmarks(0)

        self.assertEqual(movie_from_db['your_mark'], 3)

        self.model.clear_all_bookmarks()

    def test_adding_mark_for_movie_which_we_got_from_db(self):
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

        self.model.add_to_bookmarks(test_movie)
        self.model.add_mark_db(0, 7)
        movie_from_db = self.model.get_movie_from_bookmarks(0)
        self.assertEqual(movie_from_db['your_mark'], 7)



        self.model.add_mark_db(0, 2)
        movie_from_db = self.model.get_movie_from_bookmarks(0)
        self.assertEqual(movie_from_db['your_mark'], 2)

        self.model.clear_all_bookmarks()

    def test_checking_if_the_movie_in_db_and_if_it_has_mark(self):
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
        movie_id_api = test_movie['id']

        res = self.model.has_bookmark(movie_id_api)

        self.assertEqual(res, False)

        self.model.add_to_bookmarks(test_movie)
        res2 = self.model.has_bookmark(movie_id_api)

        self.assertEqual(res2, True)

        self.model.clear_all_bookmarks()

        self.model.add_mark_scratch(test_movie, 10)
        res3 = self.model.has_bookmark(movie_id_api)

        self.assertEqual(res2, True)

        self.model.clear_all_bookmarks()

    def test_if_movie_has_mark(self):
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
        movie_id_api = test_movie['id']
        res = self.model.has_marks(movie_id_api)

        self.assertEqual(res, False)

        self.model.add_to_bookmarks(test_movie)
        res2 = self.model.has_marks(movie_id_api)

        self.assertEqual(res2, False)

        self.model.add_mark_db(0, 3)
        movie_from_db = self.model.get_movie_from_bookmarks(0)
        self.assertEqual(movie_from_db['your_mark'], 3)

        res3 = self.model.has_marks(movie_id_api)

        self.assertEqual(res3, True)

        self.model.clear_all_bookmarks()

    def test_on_getting_all_movies_from_bookmarks_and_deleting_movie_separately(self):
        test_movie_1 = {
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
        test_movie_3 = {
            'vote_count': 12,
            'id': 217008,
            'video': False,
            'vote_average': 5.3,
            'title': 'TEST_3',
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
        self.model.add_to_bookmarks(test_movie_1)
        self.model.add_to_bookmarks(test_movie_2)
        self.model.add_to_bookmarks(test_movie_3)
        res = self.model.get_all_movies_from_bookmarks()

        self.assertEqual(res[0][1]['title'], test_movie_1['title'])
        self.assertEqual(res[1][1]['title'], test_movie_2['title'])
        self.assertEqual(res[2][1]['title'], test_movie_3['title'])

        self.model.delete_bookmark(2)
        res_2 = self.model.get_all_movies_from_bookmarks()
        wrong_key_on_deleting = self.model.facade.delete_bookmark(10)

        self.assertEqual(len(res_2), 2)
        self.assertEqual(res_2[0][1]['title'], test_movie_1['title'])
        self.assertEqual(res_2[1][1]['title'], test_movie_2['title'])
        self.assertEqual(wrong_key_on_deleting, False)

        self.model.clear_all_bookmarks()

