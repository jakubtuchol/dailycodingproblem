from math import pi

from pytest import mark

from src.ten import autocomplete
from src.ten import climb_stairs
from src.ten import estimate_pi
from src.ten import Log
from src.ten import longest_distinct_substring


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


class TestClimbStairs:
    """
    Problem #12
    """

    def test_provided_example(self):
        assert 5 == climb_stairs(4)

    def test_one_stair(self):
        assert 1 == climb_stairs(1)

    def test_two_stairs(self):
        assert 2 == climb_stairs(2)


class TestLongestDistinctSubstring:
    """
    Problem #13
    """

    def test_provided_example(self):
        assert 'bcb' == longest_distinct_substring('abcba', 2)

    def test_iterative(self):
        assert 'aa' == longest_distinct_substring('aabbcc', 1)
        assert 'aabb' == longest_distinct_substring('aabbcc', 2)
        assert 'aabbcc' == longest_distinct_substring('aabbcc', 3)
        assert 'aaabbb' == longest_distinct_substring('aaabbb', 3)


@mark.skip(reason='long execution that depends on randomness')
class TestEstimatePi:
    """
    Problem #14
    """

    def test_thousand_iterations(self):
        assert abs(pi - estimate_pi(10000000)) < 0.001


class TestLog:
    """
    Problem #16
    """

    def test_assert_basic_case(self):
        log = Log(2)
        log.record('one')
        log.record('two')
        assert 'two' == log.get_last(0)
        assert 'one' == log.get_last(1)

    def test_wrap_around(self):
        log = Log(3)
        log.record('one')
        log.record('two')
        log.record('three')
        assert 'three' == log.get_last(0)
        assert 'two' == log.get_last(1)
        assert 'one' == log.get_last(2)
        log.record('four')
        assert 'four' == log.get_last(0)
        assert 'three' == log.get_last(1)
        assert 'two' == log.get_last(2)
