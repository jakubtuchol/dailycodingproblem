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
