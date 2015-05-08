class CinemaDatabaseManager:
    
    GET_ALL_MOVIES_QUERY = """
        SELECT movie_id, movie_name, rating
        FROM Movies
    """

    GET_MOVIE_BY_ID_QUERY = """
        SELECT movie_id, movie_name, rating
        FROM Movies
        WHERE movie_id = ?
    """

    @classmethod
    def get_movie_by_id(cls, conn, movie_id):
        cursor = conn.cursor()
        result = cursor.execute(cls.GET_MOVIE_BY_ID_QUERY, (movie_id, ))

        return result.fetchone()


    @classmethod
    def get_all_movies(cls, conn):
        cursor = conn.cursor()

        result = cursor.execute(cls.GET_ALL_MOVIES_QUERY)

        return result.fetchall()

        
