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
