from src.thirty import edit_distance
from src.thirty import make_palindrome


class TestEditDistance:
    """
    Problem #31
    """

    def test_provided_example(self):
        assert 3 == edit_distance('kitten', 'sitting')

    def test_empty_examples(self):
        assert 7 == edit_distance('', 'sitting')
        assert 6 == edit_distance('kitten', '')

    def test_equal_examples(self):
        assert 0 == edit_distance('', '')
        assert 0 == edit_distance('kitten', 'kitten')

    def test_none_in_common(self):
        assert 3 == edit_distance('abc', 'xyz')


class TestMakePalindrome:
    """
    Problem #34
    """

    def test_provided_example(self):
        assert 'ecarace' == make_palindrome('race')

    def test_another_example(self):
        assert 'elgoogle' == make_palindrome('google')
