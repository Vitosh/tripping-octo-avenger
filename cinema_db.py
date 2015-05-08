class CinemaDatabaseManager:
    
    GET_ALL_MOVIES_QUERY = """
        SELECT movie_id, movie_name, movie_rating
        FROM Movies
    """

    GET_MOVIE_BY_ID_QUERY = """
        SELECT movie_id, movie_name, movie_rating
        FROM Movies
        WHERE movie_id = ?
    """

    def __init__(self, conn):
        self.__conn = conn

    def get_movie_by_id(self, movie_id):
        cursor = self.__conn.cursor()
        result = cursor.execute(self.__class__.GET_MOVIE_BY_ID_QUERY, (movie_id, ))

        return result.fetchone()

    def get_all_movies(self):
        cursor = self.__conn.cursor()

        result = cursor.execute(self.__class__.GET_ALL_MOVIES_QUERY)

        return result.fetchall()    
