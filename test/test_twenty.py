from src.data_structures import ListNode
from src.twenty import check_balanced_parens
from src.twenty import construct_sentence
from src.twenty import decode_word
from src.twenty import encode_word
from src.twenty import find_min_steps
from src.twenty import get_min_rooms
from src.twenty import justify_text
from src.twenty import LockableTreeNode
from src.twenty import regex_match
from src.twenty import remove_kth_from_last


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


class TestRegexMatch:
    """
    Problem #25
    """

    def test_simple_case(self):
        assert regex_match('ray', 'ra.')

    def test_simple_false_case(self):
        assert not regex_match('raymond', 'ra.')

    def test_combined_true_case(self):
        assert regex_match('chat', '.*at')

    def test_combined_false_case(self):
        assert not regex_match('chats', '*.at')

    def test_splat_match(self):
        assert not regex_match('raymond', '.*')


class TestCompareToArray:
    """
    Testing utility function
    """

    def test_simple_case(self):
        ls = ListNode.from_list(range(11))
        assert ls.compare_to_array(list(range(11)))


class TestRemoveKthFromLast:
    """
    Problem #26
    """

    def test_basic_case(self):
        root = ListNode.from_list(range(11))
        remove_kth_from_last(root, 2)
        assert root.compare_to_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 10])

    def test_zero_case(self):
        root = ListNode.from_list(range(11))
        remove_kth_from_last(root, 0)
        assert root.compare_to_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_last_case(self):
        root = ListNode.from_list(range(11))
        remove_kth_from_last(root, 1)
        assert root.compare_to_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


class TestCheckBalancedParens:
    """
    Problem #27
    """

    def test_basic_case(self):
        assert check_balanced_parens('([])[]({})')

    def test_negative_cases(self):
        assert not check_balanced_parens('([)]')
        assert not check_balanced_parens('((()')

    def test_edge_case(self):
        assert not check_balanced_parens(')(')


class TestJustifyText:
    """
    Problem #28
    """

    def test_fox_example(self):
        words = [
            'the', 'quick', 'brown',
            'fox', 'jumps', 'over',
            'the', 'lazy', 'dog'
        ]
        expected = [
            'the  quick brown',
            'fox  jumps  over',
            'the   lazy   dog',
        ]
        assert expected == justify_text(words, 16)


class TestRunLengthEncodingDecoding:
    """
    Problem #29
    """

    def test_run_length_encoding(self):
        assert '4A3B2C1D2A' == encode_word('AAAABBBCCDAA')

    def test_single_letter_encoding(self):
        assert '1A' == encode_word('A')

    def test_empty_string_encoding(self):
        assert '' == encode_word('')

    def test_run_length_decoding(self):
        assert 'AAAABBBCCDAA' == decode_word('4A3B2C1D2A')

    def test_single_letter_decoding(self):
        assert 'A' == decode_word('1A')

    def test_empty_string_decoding(self):
        assert '' == decode_word('')
