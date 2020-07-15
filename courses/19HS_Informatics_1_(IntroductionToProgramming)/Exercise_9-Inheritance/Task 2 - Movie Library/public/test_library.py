from unittest import TestCase
from movie import Movie
from moviebox import MovieBox
from library import Library

class LibraryTest(TestCase):

    def test_repr_movie(self):
        actual = repr(Movie("T", ["A", "B"], 123))
        expected = 'Movie("T", ["A", "B"], 123)'
        self.assertEqual(expected, actual)

    def test_repr_moviebox(self):
        actual = repr(MovieBox("T", [Movie("T2", ["A", "B"], 234)]))
        expected = 'MovieBox("T", [Movie("T2", ["A", "B"], 234)])'
        self.assertEqual(expected, actual)

    def test_equal_movie(self):
        movie1 = Movie("T", ["A", "B"], 123)
        movie2 = Movie("T", ["B", "A"], 123)
        self.assertEqual(movie1, movie2)

    def test_equal_moviebox(self):
        movie1 = Movie("T", ["A", "B"], 123)
        movie2 = Movie("T", ["B", "A"], 123)
        movie3 = Movie("S", ["A", "B"], 123)
        movie4 = Movie("S", ["B", "A"], 123)
        self.assertEqual(MovieBox('1', [movie1, movie3]), MovieBox('1', [movie2, movie4]))

    def test_hashable(self):
        movie1 = Movie("T", ["A", "B"], 123)
        box1 = MovieBox('1', [movie1])
        d = {movie1: 1, box1: 2}

    def test_warning1(self):
        with self.assertRaises(Warning):
            movie1 = Movie("", ["A", "B"], 123)

    def test_warning2(self):
        with self.assertRaises(Warning):
            movie1 = Movie("T", [], 123)

    def test_warning3(self):
        with self.assertRaises(Warning):
            movie1 = Movie("T", ['A'], 0)

    def test_warning4(self):
        with self.assertRaises(Warning):
            box1 = MovieBox('3', Movie("T", ['A'], 0))

    def test_warning5(self):
        with self.assertRaises(Warning):
            box1 = MovieBox('3', ("T", ['A'], 9))

    def test_box1(self):
        movie1 = Movie("T", ["A", "B"], 123)
        movie2 = Movie("T", ["B", "A"], 123)
        movie3 = Movie("S", ["A", "B"], 123)
        movie4 = Movie("S", ["B", "A"], 123)
        box = MovieBox('Box', [movie1, movie2, movie3, movie4])
        self.assertEqual(box.get_duration(), 4 * 123)

    def test_box2(self):
        movie1 = Movie("T", ["A", "B"], 123)
        movie2 = Movie("T", ["B", "A"], 123)
        movie3 = Movie("S", ["A", "B"], 123)
        movie4 = Movie("S", ["B", "A"], 123)
        box = MovieBox('Box', [movie1, movie2, movie3, movie4])
        self.assertEqual(box.get_actors(), ["A", "B"])

    def test_library(self):
        a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        b = Movie("The Godfather", ["Brando", "Pacino"], 175)
        c = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
        d = MovieBox("Top Movies", [b, c])

        l = Library()
        l.add_movie(a)
        l.add_movie(c)
        movies = [a,c]
        self.assertEqual(238, l.get_total_duration())
        self.assertEqual(movies, l.get_movies())

    # This current test suite only contains very basic test cases. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
