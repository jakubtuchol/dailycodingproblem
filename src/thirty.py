def edit_distance(word_one, word_two):
    """
    Find the edit distance between two words
    """

    # short-circuit conditions
    if word_one == word_two:
        return 0

    shorter = min(word_one, word_two, key=len)
    longer = max(word_one, word_two, key=len)

    if not shorter and longer:
        return len(longer)

    edit_matrix = []

    for _ in range(len(word_one)):
        row = [0] * len(word_two)
        edit_matrix.append(row)

    for idx_one, char_one in enumerate(word_one):
        for idx_two, char_two in enumerate(word_two):
            edit = 0 if char_one == char_two else 1
            prev_edits = []
            # check above
            if idx_one > 0:
                prev_edits.append(edit_matrix[idx_one-1][idx_two])

            # check left
            if idx_two > 0:
                prev_edits.append(edit_matrix[idx_one][idx_two-1])

            # check diagonal
            if idx_one > 0 and idx_two > 0:
                prev_edits.append(edit_matrix[idx_one-1][idx_two-1])

            prev_edit_min = min(prev_edits) if prev_edits else 0
            edit_matrix[idx_one][idx_two] = prev_edit_min + edit

    return edit_matrix[-1][-1]


def make_palindrome(s):
    """
    Make a palindrome by adding a minimal number of letters
    """

    # TODO: make optimized version of algorithm
    if s == s[::-1]:
        return s

    if s[0] == s[-1]:
        return s[0] + make_palindrome(s[1:-1]) + s[0]

    first = s[0] + make_palindrome(s[1:]) + s[0]
    last = s[-1] + make_palindrome(s[:-1]) + s[-1]

    if len(first) == len(last):
        return min(first, last)

    return min(first, last, key=len)


def find_second_largest_node(root):
    """
    Find the second-largest node in a binary search tree
    """

    traversal = []

    def _inorder(node):
        # no element, return
        if not node:
            return

        _inorder(node.left)
        traversal.append(node)
        _inorder(node.right)

    _inorder(root)

    if len(traversal) < 2:
        return None

    return traversal[-2]
