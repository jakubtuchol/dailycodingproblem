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


def construct_sentence(string, words):
    """
    Given a dictionary of words an a string with no spaces,
    find the original sentence in the provided string
    """

    def _construct_helper(s, seen_words):
        if not s:
            return seen_words
        if s in words:
            return seen_words + [s]

        for idx in range(len(s)):
            if s[:idx] in words:
                res = _construct_helper(s[idx:], seen_words + [s[:idx]])
                if res:
                    return res
        return None

    return _construct_helper(string, [])
