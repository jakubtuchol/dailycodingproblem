from src.ten import autocomplete


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
