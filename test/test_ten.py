from src.ten import autocomplete
from src.ten import climb_stairs


class TestAutocomplete:
    """
    Problem #11
    """

    def test_provided(self):
        assert sorted(['deer', 'deal']) == sorted(
            autocomplete(['dog', 'deer', 'deal'], 'de'))

    def test_no_matches(self):
        assert not len(autocomplete(['dog', 'deer', 'deal'], 'matches'))

    def test_empty_matches(self):
        assert sorted(['dog', 'deer', 'deal']) == sorted(
            autocomplete(['dog', 'deer', 'deal'], ''))


class TestClimbStairs:
    """
    Problem #12
    """

    def test_provided_example(self):
        assert 5 == climb_stairs(4)

    def test_one_stair(self):
        assert 1 == climb_stairs(1)

    def test_two_stairs(self):
        assert 2 == climb_stairs(2)
