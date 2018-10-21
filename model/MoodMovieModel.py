from .interfaces.IMoodMovieModel import IMoodMovieModel


class MoodMovieModel(IMoodMovieModel):
    def __init__(self, facade):
        self.facade = facade
        self.subscribers = []

    def subscribe(self, observer):
        self.subscribers.append(observer)

    def unsubscribe(self, movie):
        self.subscribers.remove(movie)

    def notify_subscribers(self, msg):
        for i in self.subscribers:
            i.update(msg)

    def get_movie_from_api(self, ids_genres):
        return self.facade.get_movie_from_api(ids_genres)

    def get_movie_from_bookmarks(self, id):
        return self.facade.get_movie_from_bd(id)

    def add_to_bookmarks(self, movie):
        try:
            self.facade.add_to_db(movie)
            msg = self.create_msg('COUNT ALL BOOKMARKS: {} \n'.format(len(self.get_all_movies_from_bookmarks())), '', 'THE MOVIE BY TITLE {} HAS BEEN ADDED TO BOOKMARKS'.format(movie['title']))
            self.notify_subscribers(msg)
        except:
            msg = self.create_msg(movie['title'], 'FAIL')
            self.notify_subscribers(msg)

    def clear_all_bookmarks(self):
        try:
            self.facade.clear_db()
            count_bookmarks = len(self.get_all_movies_from_bookmarks())
            if count_bookmarks == 0:
                msg = self.create_msg('','','ALL BOOKMARKS WAS DELETED')
                self.notify_subscribers(msg)
            else:
                return SyntaxError
        except:
            msg = self.create_msg('ERROR WHILE CLEAR DB', 'FAIL')
            self.notify_subscribers(msg)


    def add_mark_scratch(self, movie, mark):
        try:
            self.facade.add_mark_scratch(movie, mark)
            msg = self.create_msg('','', 'THE MOVIE BY ID: {} HAS BEEN ADD TO BOOKMARKS WITH MARK: {}'.format(len(self.get_all_movies_from_bookmarks()) -1 , mark))
            self.notify_subscribers(msg)
        except:
            msg = self.create_msg('ERROR WHILE ADDING MARKS',self.facade.add_mark_scratch(movie, mark),'')
            self.notify_subscribers(msg)
    def add_mark_db(self, id, mark):
        self.facade.add_mark_db(id, mark)

    def has_bookmark(self, movie_id_api):
        return self.facade.has_bookmark(movie_id_api)

    def has_marks(self, movie_id_api):
        return self.facade.has_mark(movie_id_api)

    def get_all_movies_from_bookmarks(self):
        return self.facade.get_all_movies_from_bookmarks()

    def delete_bookmark(self, id):
        msg = self.facade.delete_bookmark(id)
        if msg:
            msg = self.create_msg('','','THE MOVIE WITH ID: {} WAS DELETED'.format(id))
        else:
            msg = self.create_msg('DELETEING STATUS', 'ERROR', '')
        self.notify_subscribers(msg)

    def create_msg(self, header, status, repr = None):
        return {
            'header': header,
            'status': status,
            'repr': repr
        }