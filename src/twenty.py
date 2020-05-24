from collections import deque


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    @staticmethod
    def from_list(ls):
        fake_head = ListNode(None)
        head = fake_head
        for elt in ls:
            head.next = ListNode(elt)
            head = head.next

        return fake_head.next

    def compare_to_array(self, ls):
        if not ls:
            return False

        if ls[0] != self.val:
            return False

        if len(ls) == 1 and self.next is None:
            return True
        return self.next.compare_to_array(ls[1:])


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
