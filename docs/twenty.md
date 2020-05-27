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
* Problem #23 (Google) *DONE*
    * You are given an M by N matrix consisting of booleans that represents a board. Each `True` boolean
      represents a wall. Each `False` boolean represents a tile you can walk on.
    * Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps
      required to reach the end coordinate from the start. If there is no possible path, then return `null`.
      You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges
      of the board.
    * For example, given the following board:
      ```
      [[f, f, f, f],
      [t, t, f, t],
      [f, f, f, f],
      [f, f, f, f]]
      ```
      and `start = (3, 0)` (bottom left) and `end = (0, 0)` (top left), the minimum number of steps required
      to reach the end is 7, since we would need to go through `(1, 2)` because there is a wall everywhere else
      on the second row.
* Problem #24 (Google) *DONE*
    * Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its
      descendants or ancestors are not locked.
    * Design a binary tree node class with the following methods:
      * `is_locked`, which returns whether the node is locked
      * `lock`, which attempts to lock the node. If it cannot be locked, then it should return `false`.
        Otherwise, it should lock it and return `true`.
      * `unlock`, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise,
        it should unlock it and return true.
    * You may augment the node to add parent pointers or any other property you would like. You may assume
      the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each
      method should run in `O(h)`, where h is the height of the tree.
* Problem #25 (Facebook) *DONE*
    * Implement regular expression matching with the following special characters:
      * `.` (period) which matches any single character
      * `*` (asterisk) which matches zero or more of the preceding element
    * That is, implement a function that takes in a string and a valid regular expression and returns whether
      or not the string matches the regular expression.
    * For example, given the regular expression `"ra."` and the string `"ray"`, your function should return `true`.
      The same regular expression on the string `"raymond"` should return `false`.
    * Given the regular expression `".*at"` and the string `"chat"`, your function should return `true`. The same
      regular expression on the string `"chats"` should return `false`.
* Problem #26 (Google) *DONE*
    * Given a singly linked list and an integer `k`, remove the kth last element from the list. `k` is guaranteed
      to be smaller than the length of the list.
    * The list is very long, so making more than one pass is prohibitively expensive.
    * Do this in constant space and in one pass.
