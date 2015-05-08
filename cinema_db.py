class CinemaDatabaseManager:
    
    GET_ALL_MOVIES_QUERY = """
        SELECT movie_id, movie_name, rating
        FROM Movies
    """


    @classmethod
    def get_all_movies(cls, conn):
        cursor = conn.cursor()

        result = cursor.execute(cls.GET_ALL_MOVIES_QUERY)

        return result.fetchall()

        
