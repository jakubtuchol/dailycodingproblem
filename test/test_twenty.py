from src.twenty import get_min_rooms


class TestGetMinRooms:
    """
    Problem #21
    """

    def test_provided_example(self):
        assert 2 == get_min_rooms([(30, 75), (0, 50), (60, 150)])
