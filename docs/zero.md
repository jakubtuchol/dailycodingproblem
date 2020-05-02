# Problems 1 - 9

* Problem #1 (Google) *DONE*
    * Given an array of numbers, return whether any two sums to K.
* Problem #2
    * Given an array of integers, return a new array such that each element
      at index i of the new array is the product of all the numbers in the
      original array except the one at i. Solve it without using division
      and in O(n) time.
* Problem #3
    * Given the root to a binary tree, implement serialize(root), which
      serializes the tree into a string, and deserialize(s), which
      deserializes the string back into the tree.
* Problem #4 (Stripe) *DONE*
    * Given an array of integers, find the first missing positive integer
      in linear time and constant space. In other words, find the lowest
      positive integer that does not exist in the array. The array can
      contain duplicates and negative numbers as well.
* Problem #5
    * cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns
      the first and last element of that pair. For example, car(cons(3, 4))
      returns 3, and cdr(cons(3, 4)) returns 4. Implement car and cdr.
* Problem #6
    * An XOR linked list is a more memory efficient doubly linked list. Instead
      of each node holding next and prev fields, it holds a field named both,
      which is a XOR of the next node and the previous node. Implement a XOR
      linked list; it has an add(element) which adds the element to the end,
      and a get(index) which returns the node at index.
    * If using a language that has no pointers (such as Python), assume you
      have access to get_pointer and dereference_pointer functions that converts
      between nodes and memory addresses.
* Problem #7 (Facebook) *DONE*
    * Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
      count the number of ways it can be decoded. For example, the message
      '111' would give 3, since it could be decoded as 'aaa, 'ka', and 'ak'.
* Problem #8
    * A unival tree (which stands for "universal value") is a tree where all
      nodes have the same value.
    * Given the root to a binary tree, count the number of unival subtrees.
* Problem #9 (Airbnb) *DONE*
    * Given a list of integers, write a function that returns the largest sum
      of non-adjacent numbers. Numbers can be 0 or negative.
    * For example, `[2, 4, 6, 8]` should return 12, since we pick 4 and 8.
      `[5, 1, 1, 5]` should return 10, since we pick 5 and 5.
