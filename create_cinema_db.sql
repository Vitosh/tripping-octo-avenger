DROP TABLE IF EXISTS Movies;

CREATE TABLE Movies(
  movie_id INTEGER PRIMARY KEY,
  movie_name TEXT,
  movie_rating REAL
);


INSERT INTO Movies(movie_name, movie_rating)
VALUES ("The Hunger Games: Catching Fire", 7.9),
       ("Wreck-It Ralph", 7.8),
       ("Her", 8.3);
