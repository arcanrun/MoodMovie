from model.facade.subsystem.interfaces.IMovieSelector import IMovieSelector
import http.client
import random
import json


class MovieSelectorTheMovieDborg(IMovieSelector):
    def __init__(self, ):
        self.conn = http.client.HTTPSConnection('api.themoviedb.org')

    def get_movie(self, ids_genres, include_adult=False):
        all_movies_in_page = []
        diapason = 1001 # thedbmovie api provides to parse only 1000 pages
        random_page = random.randint(0, diapason)

        try:
            data = self.request_genre_random(ids_genres, page=str(random_page))
        except Exception:
            raise SyntaxError

        data = data['results']

        for i in range(0, len(data)):
            all_movies_in_page.append( data[i] )

        movie = all_movies_in_page[random.randint(0, len(all_movies_in_page) - 1)]

        url_movie = self.create_url_movive(movie['id'])
        movie['url_movie'] = url_movie

        return movie

    def request_genre_random(self, ids_genres, page='1', method='GET', api_key = 'a6bd92f5e397e4a9362de86cdcc170fe', include_adult = 'false'):

        id_category = str(ids_genres[random.randint(0, len(ids_genres) - 1)]) # random id from ids_movie


        url = '/3/discover/movie?with_genres=' + id_category + '&page=' + page + '&include_video=false&include_adult=' + include_adult + '&sort_by=popularity.desc&language=en-US&api_key=' + api_key
        self.conn.request(method, url)
        res = self.conn.getresponse()
        data = res.read()
        data_encoded = json.loads(data)
        real_diaposon = int(data_encoded['total_pages'])

        if int(page) > real_diaposon:
            page = str(random.randint(0, real_diaposon))
            return self.request_genre_random(ids_genres, page)

        return data_encoded




    def create_url_movive(self, id):
        url = 'https://www.themoviedb.org/movie/' + str(id)
        return url

    def set_diaposon(self):
        pass



if __name__ == '__main__':
    api = MovieSelectorTheMovieDborg()
    print(api.get_movie([35]))
