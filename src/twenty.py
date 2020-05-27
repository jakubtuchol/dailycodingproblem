from collections import deque


def get_min_rooms(lectures):
    """
    Given an array of start and end times for lectures,
    find the minimum number of classrooms necessary.
    """
    starts = sorted(start for start, _ in lectures)
    ends = sorted(end for _, end in lectures)

    num_rooms = 0
    current_overlap = 0
    start_idx, end_idx = 0, 0

    while start_idx < len(starts) and end_idx < len(ends):
        if starts[start_idx] < ends[end_idx]:
            current_overlap += 1
            num_rooms = max(num_rooms, current_overlap)
            start_idx += 1
        else:
            current_overlap -= 1
            end_idx += 1

    return num_rooms


def construct_sentence(s, words):
    """
    Given a dictionary of words an a string with no spaces,
    find the original sentence in the provided string
    """

    starts = {0: ''}

    for idx in range(len(s) + 1):
        new_starts = starts.copy()
        for start_index in starts.keys():
            word = s[start_index:idx]
            if word in words:
                new_starts[idx] = word
        starts = new_starts.copy()

    result = []
    current_length = len(s)
    if current_length not in starts:
        return None

    while current_length > 0:
        word = starts[current_length]
        current_length -= len(word)
        result.append(word)

    return list(reversed(result))


def find_min_steps(board, start, end):
    """
    Find the minimum number of steps required to reach the end position
    index from the start position
    """

    """
    min path to given node is min(paths to adjacent nodes)
    """

    def walkable(board, row, col):
        # validate row
        if row < 0 or row >= len(board):
            return False

        # validate col
        if col < 0 or col >= len(board[0]):
            return False

        return not board[row][col]

    def get_walkable_neighbors(board, row, col):
        return [(r, c) for r, c in
                [
                (row, col-1),
                (row, col+1),
                (row-1, col),
                (row+1, col),
                ] if walkable(board, r, c)
                ]

    visited = set()
    to_visit = deque([(start, 0)])

    while to_visit:
        (row, col), distance = to_visit.popleft()
        visited.add((row, col))

        for neighbor in get_walkable_neighbors(board, row, col):
            if neighbor == end:
                return distance + 1
            if neighbor not in visited:
                to_visit.append((neighbor, distance+1))

    return 0


class LockableTreeNode:
    """
    Implement a binary tree where a node can be locked and unlocked
    only if all descendants or ancestors are not locked
    """

    def __init__(self, value):
        # node-specific info
        self.val = value
        self.left = None
        self.right = None
        self.parent = None

        # lock-specific info
        self.locked = False
        self.left_subtree_locked = False
        self.right_subtree_locked = False

    def add_left_child(self, child):
        self.left = child
        child.parent = self

    def add_right_child(self, child):
        self.right = child
        child.parent = self

    def is_locked(self):
        return self.locked

    def _ancestor_locked(self):
        """
        Check if any of parents are locked
        """
        parent = self.parent
        while parent:
            if parent.is_locked():
                return True
            parent = parent.parent
        return False

    def lock(self):
        # check if node or any of subtrees are locked
        if self.left_subtree_locked or self.right_subtree_locked:
            return False

        if self.locked:
            return False

        # iterate up parent chain to see if any of parents are locked
        if self._ancestor_locked():
            return False

        # iterate up tree, locking corresponding parental chains
        parent = self.parent
        cur = self
        while parent:
            if parent.left == cur:
                parent.left_subtree_locked = True
            else:
                parent.right_subtree_locked = True
            cur = parent
            parent = parent.parent
        self.locked = True

        return True

    def unlock(self):
        # check if any of subtrees is locked
        if self.left_subtree_locked or self.right_subtree_locked:
            return False

        if not self.locked:
            return False

        # iterate up
        if self._ancestor_locked():
            return False

        parent = self.parent
        cur = self
        while parent:
            if parent.left == cur:
                parent.left_subtree_locked = False
                # don't proceed to unlock ancestor subtrees
                # if other subtree still locked
                if parent.right_subtree_locked:
                    break
            else:
                parent.right_subtree_locked = False
                # don't proceed to unlock ancestor subtrees
                # if other subtree still locked
                if parent.left_subtree_locked:
                    break
            cur = parent
            parent = parent.parent
        self.locked = False

        return True


def regex_match(word, regex, repeat=None):
    """
    Given that '.' corresponds to any character, and '*'
    corresponds to 0 or more matches of the previous character,
    write a function that checks if the pattern matches the input.
    """
    if not word and not regex:
        return True

    if not word:
        if len(regex) == 2 and regex[-1]:
            return True
        return False

    if not regex:
        return False

    # check case where repeat expected
    if repeat:
        if word[0] == repeat or repeat == '.':
            return regex_match(
                word[1:], regex, repeat=repeat
            ) or regex_match(word, regex)

    has_repeat = len(regex) > 1 and regex[1] == '*'

    if regex[0] != '.' and regex[0] != word[0]:
        return False

    if has_repeat:
        return regex_match(word[1:], regex[2:], repeat=regex[0])

    return regex_match(word[1:], regex[1:])


def remove_kth_from_last(ls, k):
    """
    Remove the kth from last element from a singly-linked list
    """

    runner = ls
    while k > 0:
        runner = runner.next
        k -= 1

    cur = ls
    prev = None

    # iterate until runner runs out
    while runner:
        prev = cur
        cur = cur.next
        runner = runner.next

    # remove element from list
    if cur:
        prev.next = cur.next
    else:
        prev.next = None


def check_balanced_parens(parens):
    """
    Given that a string can be composed of parentheses, brackets,
    and curly braces, check whether an input string has balanced
    brackets.
    """
    matches = {
        '}': '{',
        ')': '(',
        ']': '[',
    }

    ls = []

    for paren in parens:
        if paren in matches:
            if not ls or ls[-1] != matches[paren]:
                return False
            ls.pop()
        else:
            ls.append(paren)

    return not ls
