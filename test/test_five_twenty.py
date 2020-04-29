from src.five_twenty import find_sum_xor_pairs
from src.five_twenty import max_sum_subarray
from src.five_twenty import spiral_matrix


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


class TestSpiralMatrix:
    """
    Problem #525
    """

    def test_four_by_five_case(self):
        matrix = [
            [1,  2,  3,  4,  5],
            [6,  7,  8,  9,  10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
        ]
        expected = [
            1, 2, 3, 4, 5,
            10, 15, 20, 19, 18,
            17, 16, 11, 6, 7,
            8, 9, 14, 13, 12,
        ]

        assert expected == spiral_matrix(matrix)
