from src.zero import find_missing_integer
from src.zero import largest_nonadjacent_sum
from src.zero import two_sum


class TestTwoSum:
    """
    Problem #1
    """

    def test_provided(self):
        assert two_sum([10, 15, 3, 7], 17)

    def test_false(self):
        assert not two_sum([10, 15, 3, 8], 17)

    def test_empty(self):
        assert not two_sum([], 17)


class TestFindMissingInteger:
    """
    Problem #4
    """

    def test_basic_example(self):
        assert 2 == find_missing_integer([3, 4, -1, 1])

    def test_continuous_case(self):
        assert 3 == find_missing_integer([1, 2, 0])

    def test_no_missing_case(self):
        assert 3 == find_missing_integer([1, 2, 3])

    def test_positive_gap_case(self):
        assert 3 == find_missing_integer([5, 1, 2])

    def test_almost_contiguous_case(self):
        assert 3 == find_missing_integer([5, 1, 2])


class TestLargestNonadjacentSum:
    """
    Problem #9
    """

    def test_alternating_case(self):
        assert 12 == largest_nonadjacent_sum([2, 4, 6, 8])

    def test_end_case(self):
        assert 10 == largest_nonadjacent_sum([5, 1, 1, 5])

    def test_empty_case(self):
        assert 0 == largest_nonadjacent_sum([])
