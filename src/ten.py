from collections import defaultdict
from math import pow
from random import randint
from random import uniform
from time import sleep


def schedule_call(f, n):
    """
    Call function `f` after `n` milliseconds
    """
    sleep(n)
    f()


def autocomplete(corpus, prefix):
    """
    Given a text corpus and a prefix, return a list
    of all words that start with that prefix
    """
    class Trie:
        def __init__(self, value):
            self.value = value
            self.children = {}
            # allows for quick access of resulting words,
            # rather than having cumbersome traversal
            self.words = []

    if not len(prefix):
        return corpus

    # construct trie
    root = Trie('')
    for word in corpus:
        cur = root
        cur.words.append(word)
        for char in word:
            if char not in cur.children:
                cur.children[char] = Trie(char)
            cur = cur.children[char]
            cur.words.append(word)

    for char in prefix:
        if char in root.children:
            root = root.children[char]
        else:
            return []

    return root.words


def climb_stairs(k):
    """
    Return the number of ways that `k` stairs can be climbed
    given that you can climb either 1 or 2 stairs at a time
    """
    num_ways = [1]

    for idx in range(1, k+1):
        one_step = num_ways[idx-1]
        two_step = num_ways[idx-2] if idx > 1 else 0
        num_ways.append(one_step + two_step)

    return num_ways[-1]


def longest_distinct_substring(s, k):
    """
    Return longest distinct substring with at most `k`
    characters
    """

    seen = defaultdict(int)
    cur = []
    longest = ''

    for c in s:
        # add new character to seen and cur
        seen[c] += 1
        cur.append(c)

        # if have too many letters, iterate first index of cur and
        # decrement seen accordingly
        while len(seen) > k:
            remove = cur.pop(0)
            seen[remove] -= 1
            if not seen[remove]:
                del seen[remove]

        # compare lengths of cur and longest
        if len(cur) > len(longest):
            longest = ''.join(cur)

    return longest


def estimate_pi(iterations):
    """
    Estimate pi using the monte-carlo method with a specified number
    of iterations
    """
    upper = 2
    lower = -2
    in_circle = 0

    for _ in range(iterations):
        x, y = uniform(lower, upper), uniform(lower, upper)
        if pow(x, 2) + pow(y, 2) <= 4:
            in_circle += 1

    # ratio of numbers that fall within circle * 4 should be close to pi
    return in_circle / iterations * 4


def select_stream(stream):
    """
    Select a random element from an infinite stream with uniform probability
    """
    cur = 0
    for idx, elt in enumerate(stream):
        if randint(0, idx) == idx:
            cur = elt
    return cur


class Log:
    """
    Data structure to record at most `n` logs and retrieve i'th log from
    end in constant time
    """

    def __init__(self, n):
        self._logs = [None] * n
        self._cur = 0

    def record(self, val):
        self._logs[self._cur] = val
        self._cur = (self._cur + 1) % len(self._logs)

    def get_last(self, idx):
        return self._logs[(self._cur - 1 - idx) % len(self._logs)]


def find_longest_path(filesystem):
    """
    Given a string representation of a filesystem, find the longest
    path in that filesystem
    """
    cur_path = []
    max_length = 0

    for node in filesystem.split('\n'):
        depth = len(node) - len(node.lstrip('\t'))
        name = node[depth:]
        while len(cur_path) and cur_path[-1][0] >= depth:
            cur_path.pop()

        length = cur_path[-1][1] + 1 if cur_path else 0
        new_length = length + len(name)
        max_length = max(max_length, new_length)

        cur_path.append((depth, new_length))

    return max_length
