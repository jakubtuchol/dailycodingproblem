from src.ten import autocomplete
from src.ten import climb_stairs
from src.ten import longest_distinct_substring


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


class TestLongestDistinctSubstring:
    """
    Problem #13
    """

    def test_provided_example(self):
        assert 'bcb' == longest_distinct_substring('abcba', 2)

    def test_iterative(self):
        assert 'aa' == longest_distinct_substring('aabbcc', 1)
        assert 'aabb' == longest_distinct_substring('aabbcc', 2)
        assert 'aabbcc' == longest_distinct_substring('aabbcc', 3)
        assert 'aaabbb' == longest_distinct_substring('aaabbb', 3)
