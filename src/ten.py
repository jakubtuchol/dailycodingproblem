from collections import defaultdict
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
