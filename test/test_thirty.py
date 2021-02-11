from src.thirty import edit_distance
from src.thirty import find_second_largest_node
from src.thirty import make_palindrome
from src.thirty import powerset
from src.data_structures import BinaryNode


class TestEditDistance:
    """
    Problem #31
    """

    def test_provided_example(self):
        assert 3 == edit_distance('kitten', 'sitting')

    def test_empty_examples(self):
        assert 7 == edit_distance('', 'sitting')
        assert 6 == edit_distance('kitten', '')

    def test_equal_examples(self):
        assert 0 == edit_distance('', '')
        assert 0 == edit_distance('kitten', 'kitten')

    def test_none_in_common(self):
        assert 3 == edit_distance('abc', 'xyz')


class TestMakePalindrome:
    """
    Problem #34
    """

    def test_provided_example(self):
        assert 'ecarace' == make_palindrome('race')

    def test_another_example(self):
        assert 'elgoogle' == make_palindrome('google')


class TestFindSecondLargestNode:
    """
    Problem #36
    """

    def test_on_left(self):
        root = BinaryNode(5)
        root.left = BinaryNode(3)

        assert 3 == find_second_largest_node(root).val

    def test_on_right(self):
        root = BinaryNode(2)
        root.right = BinaryNode(4)

        assert 2 == find_second_largest_node(root).val

    def test_balanced(self):
        root = BinaryNode(2)
        root.left = BinaryNode(1)
        root.right = BinaryNode(3)

        assert 2 == find_second_largest_node(root).val

    def test_less_than_two_elements(self):
        root = BinaryNode(2)

        assert not find_second_largest_node(root)


class TestPowerset:
    """
    Problem #37
    """

    def test_three(self):
        expected_set = [
            [],
            [1], [2], [3],
            [1, 2], [1, 3], [2, 3],
            [1, 2, 3],
        ]

        calculated_set = powerset([1, 2, 3])
        assert len(calculated_set) == len(expected_set)

        for elt in calculated_set:
            assert elt in expected_set

    def test_empty(self):
        assert [[]] == powerset([])
