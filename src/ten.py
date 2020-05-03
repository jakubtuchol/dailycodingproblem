from time import sleep


def schedule_call(f, n):
    """
    Call function `f` after `n` milliseconds
    """
    sleep(n)
    f()


def autocomplete(corpus, prefix):
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
