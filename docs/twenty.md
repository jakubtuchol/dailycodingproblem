# Problems #20 - 29

* Problem #20 (Google)
    * Given two singly linked lists that intersect at some point, find the intersecting node.
      The lists are non-cyclical.
      * For example, given `A = 3 -> 7 -> 8 -> 10` and `B = 99 -> 1 -> 8 -> 10`, return the node
        with value 8.
      * In this example, assume nodes with the same value are the exact same node objects.
    * Do this in `O(M + N)` time (where M and N are the lengths of the lists) and constant space.
* Problem #21 (Snapchat) *DONE*
    * Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
      find the minimum number of rooms required.
    * For example, given `[(30, 75), (0, 50), (60, 150)]`, you should return 2.
* Problem #22 (Microsoft) *DONE*
    * Given a dictionary of words and a string made up of those words (no spaces), return the original
      sentence in a list. If there is more than one possible reconstruction, return any of them. If
      there is no possible reconstruction, then return null.
    * For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
      you should return ['the', 'quick', 'brown', 'fox'].
    * Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
      return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
