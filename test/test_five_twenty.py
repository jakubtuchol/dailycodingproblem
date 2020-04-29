from src.five_twenty import find_sum_xor_pairs
from src.five_twenty import max_sum_subarray


class TestSumXorPairs:
    """
    Problem #523
    """

    def test_base_case(self):
        assert 1 == find_sum_xor_pairs(10, 8)


class TestMaxSumSubarray:
    """
    Problem #524
    """

    def test_nonzero_case(self):
        assert 137 == max_sum_subarray([34, -50, 42, 14, -5, 86])

    def test_zero_case(self):
        assert 0 == max_sum_subarray([-5, -1, -8, -9])
