from src.twenty import construct_sentence
from src.twenty import find_min_steps
from src.twenty import get_min_rooms
from src.twenty import LockableTreeNode


class TestGetMinRooms:
    """
    Problem #21
    """

    def test_provided_example(self):
        assert 2 == get_min_rooms([(30, 75), (0, 50), (60, 150)])


class TestConstructSentence:
    """
    Problem #22
    """

    def test_provided_example(self):
        dictionary = {'quick', 'brown', 'the', 'fox'}
        expected = ['the', 'quick', 'brown', 'fox']
        assert expected == construct_sentence(
            'thequickbrownfox', dictionary
        )

    def test_bed_bath_beyond_example(self):
        dictionary = {'be', 'bed', 'bath', 'bedbath', 'and', 'beyond'}
        expected_one = ['bed', 'bath', 'and', 'beyond']
        expected_two = ['bedbath', 'and', 'beyond']
        res = construct_sentence('bedbathandbeyond', dictionary)
        assert (expected_one == res or expected_two == res)


class TestFindMinSteps:
    """
    Problem #23
    """

    def test_provided_example(self):
        maze = [
            [False, False, False, False],
            [True,  True,  False, True],
            [False, False, False, False],
            [False, False, False, False],
        ]
        assert 7 == find_min_steps(maze, (3, 0), (0, 0))


class TestLockableTreeNode:
    """
    Problem #24
    """

    def test_balanced_example(self):
        root = LockableTreeNode(1)
        root.add_left_child(LockableTreeNode(2))
        root.add_right_child(LockableTreeNode(3))

        assert root.lock()
        assert not root.lock()
        assert root.is_locked()
        assert not root.left.lock()
        assert not root.left.is_locked()
        assert not root.right.lock()
        assert not root.right.is_locked()

        assert root.unlock()
        assert not root.is_locked()
        assert root.left.lock()
        assert root.left.is_locked()
        assert root.right.lock()
        assert root.right.is_locked()
        assert not root.lock()
        assert not root.is_locked()

        assert root.right.unlock()
        assert not root.lock()
