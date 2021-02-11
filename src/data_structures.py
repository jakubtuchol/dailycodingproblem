class ListNode:
    """
    Singly-linked list implementation
    """

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


class BinaryNode:
    """
    Binary tree implementation
    """

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
