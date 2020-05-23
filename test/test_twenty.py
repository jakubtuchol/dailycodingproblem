from src.twenty import construct_sentence
from src.twenty import get_min_rooms


class TestGetMinRooms:
    """
    Problem #21
    """

    def test_provided_example(self):
        assert 2 == get_min_rooms([(30, 75), (0, 50), (60, 150)])


class TestConstructSentence:
    """
    Problem #22
    """

    def test_provided_example(self):
        dictionary = {'quick', 'brown', 'the', 'fox'}
        expected = ['the', 'quick', 'brown', 'fox']
        assert expected == construct_sentence(
            'thequickbrownfox', dictionary
        )

    def test_bed_bath_beyond_example(self):
        dictionary = {'be', 'bed', 'bath', 'bedbath', 'and', 'beyond'}
        expected_one = ['bed', 'bath', 'and', 'beyond']
        expected_two = ['bedbath', 'and', 'beyond']
        res = construct_sentence('bedbathandbeyond', dictionary)
        assert (expected_one == res or expected_two == res)
