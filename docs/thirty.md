# Problems #30 - 39

* Problem #30 (Facebook)
    * You are given an array of non-negative integers that represents a two-dimensional elevation map where each element
      is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.
    * Compute how many units of water remain trapped on the map in `O(N)` time and `O(1)` space.
    * For example, given the input `[2, 1, 2]`, we can hold 1 unit of water in the middle.
    * Given the input `[3, 0, 1, 3, 0, 5]`, we can hold 3 units in the first index, 2 in the second, and 3 in the fourth
      index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
* Problem #31 (Google) *DONE*
    * The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions
      required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three:
      substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
    * Given two strings, compute the edit distance between them.
