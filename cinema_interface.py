class CliInterface:

    def __init__(self, cinema_manager):
        self.__cinema = cinema_manager

    def __command_dispatcher(self, command):
        if command == "show_movies":
            self.show_movies()

    def start(self):
        while True:
            command = input("Enter command:")
            self.__command_dispatcher(command)
     
    def show_movies(self):
        all_movies = self.__cinema.get_all_movies()


        print("\n".join([movie["movie_name"] for movie in all_movies]))
