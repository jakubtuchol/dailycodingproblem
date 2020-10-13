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
* Problem #32 (Jane Street)
    * Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a
      possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of
      any currency, so that you can end up with some amount greater than A of that currency.
    * There are no transaction costs and you can trade fractional quantities.
* Problem #33 (Microsoft)
    * Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of
      the list so far on each new element.
    * Recall that the median of an even-numbered list is the average of the two middle numbers.
    * For example, given the sequence `[2, 1, 5, 7, 2, 0, 5]`, your algorithm should print out:
      ```
      2
      1.5
      2
      3.5
      2
      2
      2
      ```
* Problem #34 (Quora) *DONE*
    * Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible
      anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the
      lexicographically earliest one (the first one alphabetically).
    * For example, given the string "race", you should return "ecarace", since we can add three letters to it (which
      is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by
      adding three letters, but "ecarace" comes first alphabetically.
    * As another example, given the string "google", you should return "elgoogle".
* Problem #35 (Google)
    * Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs
      come first, the Gs come second, and the Bs come last. You can only swap elements of the array.
    * Do this in linear time and in-place.
    * For example, given the array `['G', 'B', 'R', 'R', 'B', 'R', 'G']`, it should become
      `['R', 'R', 'R', 'G', 'G', 'B', 'B']`.
