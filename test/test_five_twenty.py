from src.five_twenty import find_sum_xor_pairs


class TestSumXorPairs:
    """
    Problem #523
    """

    def test_base_case(self):
        assert 1 == find_sum_xor_pairs(10, 8)
