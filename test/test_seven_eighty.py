from src.seven_eighty import is_palindrome


class TestIsPalindrome:
    """
    Problem #789
    """

    def test_provided_true(self):
        assert is_palindrome(888)
        assert is_palindrome(121)
        assert is_palindrome(2)

    def test_provided_false(self):
        assert not is_palindrome(678)
