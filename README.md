# Daily Coding Problem

Keeping up with the [Daily Coding Problem]()

* Completed: 29

* Problem #18
    * Given an array of integers and a number k, where 1 <= k <= length of the array, compute the
      maximum values of each subarray of length k.
      * For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8],
        since:
        * `10 = max(10, 5, 2)`
        * `7 = max(5, 2, 7)`
        * `8 = max(2, 7, 8)`
        * `8 = max(7, 8, 7)`
    * Do this in `O(n)` time and `O(k)` space. You can modify the input array in-place and you do
      not need to store the results. You can simply print them out as you compute them.
* Problem #19
    * A builder is looking to build a row of N houses that can be of K different colors. He has a
      goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
    * Given an N by K matrix where the nth row and kth column represents the cost to build the
      nth house with kth color, return the minimum cost which achieves this goal.
* Problem #28
    * Write an algorithm to justify text. Given a sequence of words and an integer line length `k`, return a
      list of strings which represents each line, fully justified.
    * More specifically, you should have as many words as possible in each line. There should be at least one
      space between each word. Pad extra spaces when necessary so that each line has exactly length `k`. Spaces
      should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.
    * If you can only fit one word on a line, then you should pad the right-hand side with spaces.
    * Each word is guaranteed not to be longer than k.
    * For example, given the list of words `["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]`
      and `k = 16`, you should return the following:
      * `["the  quick brown", # 1 extra space on the left`
      * `"fox  jumps  over", # 2 extra spaces distributed evenly`
      * `"the   lazy   dog"] # 4 extra spaces distributed evenly`
* Problem #29
    * Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated
      successive characters as a single count and character. For example, the string `"AAAABBBCCDAA"` would be encoded
      as `"4A3B2C1D2A"`.
    * Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists
      solely of alphabetic characters. You can assume the string to be decoded is valid.
* Problem #30
    * You are given an array of non-negative integers that represents a two-dimensional elevation map where each element
      is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.
    * Compute how many units of water remain trapped on the map in `O(N)` time and `O(1)` space.
    * For example, given the input `[2, 1, 2]`, we can hold 1 unit of water in the middle.
    * Given the input `[3, 0, 1, 3, 0, 5]`, we can hold 3 units in the first index, 2 in the second, and 3 in the fourth
      index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
* Problem #31
    * The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions
      required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three:
      substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
    * Given two strings, compute the edit distance between them.
* Problem #32
    * Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a
      possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of
      any currency, so that you can end up with some amount greater than A of that currency.
    * There are no transaction costs and you can trade fractional quantities.
* Problem #33
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
* Problem #34
    * Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible
      anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the
      lexicographically earliest one (the first one alphabetically).
    * For example, given the string "race", you should return "ecarace", since we can add three letters to it (which
      is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by
      adding three letters, but "ecarace" comes first alphabetically.
    * As another example, given the string "google", you should return "elgoogle".
* Problem #35
    * Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs
      come first, the Gs come second, and the Bs come last. You can only swap elements of the array.
    * Do this in linear time and in-place.
    * For example, given the array `['G', 'B', 'R', 'R', 'B', 'R', 'G']`, it should become
      `['R', 'R', 'R', 'G', 'G', 'B', 'B']`.
* Problem #36
    * Given the root to a binary search tree, find the second largest node in the tree.
* Problem #37
    * The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
    * For example, given the set `{1, 2, 3}`, it should return `{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}`.
    * You may also use a list or array to represent a set.
* Problem #38
    * You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board
      where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row,
      column, or diagonal.
* Problem #39
    * Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead
      or alive, and at each tick, the following rules apply:
      * Any live cell with less than two live neighbours dies.
      * Any live cell with two or three live neighbours remains living.
      * Any live cell with more than three live neighbours dies.
      * Any dead cell with exactly three live neighbours becomes a live cell.
    * A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.
    * Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates
      and the number of steps it should run for. Once initialized, it should print out the board state at each step.
      Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to
      bottom-rightmost live cell.
    * You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
* Problem #40
    * Given an array of integers where every integer occurs three times except for one integer, which only occurs once,
      find and return the non-duplicated integer.
    * For example, given `[6, 1, 3, 3, 3, 6, 6]`, return 1. Given `[13, 19, 13, 13]`, return 19.
    * Do this in O(N) time and O(1) space.
* Problem #41
    * Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting
      airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible
      itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.
    * For example, given the list of flights `[('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]` and starting
      airport 'YUL', you should return the list `['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']`.
    * Given the list of flights `[('SFO', 'COM'), ('COM', 'YYZ')]` and starting airport 'COM', you should return null.
    * Given the list of flights `[('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]` and starting airport 'A', you should return
      the list `['A', 'B', 'C', 'A', 'C']` even though `['A', 'C', 'A', 'B', 'C']` is also a valid itinerary. However, the first
      one is lexicographically smaller.
* Problem #42 (Google)
    * Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a
      subset cannot be made, then return null.
    * Integers can appear more than once in the list. You may assume all numbers in the list are positive.
    * For example, given `S = [12, 1, 61, 5, 9, 2]` and `k = 24`, return `[12, 9, 2, 1]` since it sums up to 24.
* Problem #43 (Amazon)
    * Implement a stack that has the following methods:
      * `push(val)`, which pushes an element onto the stack
      * `pop()`, which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it
        should throw an error or return null.
      * `max()`, which returns the maximum value in the stack currently. If there are no elements in the stack, then it should
        throw an error or return null.
* Problem #44 (Google)
    * We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j]
      form an inversion if `A[i] > A[j]` but `i < j`. That is, a smaller element appears after a larger element.
    * Given an array, count the number of inversions it has. Do this faster than `O(N^2)` time.
    * You may assume each element in the array is distinct.
    * For example, a sorted list has zero inversions. The array `[2, 4, 1, 3, 5]` has three inversions: (2, 1), (4, 1), and (4, 3).
      The array `[5, 4, 3, 2, 1]` has ten inversions: every distinct pair forms an inversion.
* Problem #45 (Two Sigma)
    * Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7()
      that returns an integer from 1 to 7 (inclusive).
* Problem #46 (Amazon)
    * Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.
    * For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".
* Problem #47 (Facebook)
    * Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the
      maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.
    * For example, given `[9, 11, 8, 5, 7, 10]`, you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
* Problem #48 (Google)
    * Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.
    * For example, given the following preorder traversal:
      - `[a, b, d, e, c, f, g]`
    * And the following inorder traversal:
      - `[d, b, e, a, f, c, g]`
    * You should return the following tree:
    ```
          a
         / \
        b   c
       / \ / \
      d  e f  g
    ```
* Problem #49 (Amazon)
    * Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
    * For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137,
      since we would take elements 42, 14, -5, and 86.
    * Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
    * Do this in O(N) time.
* Problem #50 (Microsoft)
    * Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each
      internal node is one of '+', '−', '∗', or '/'.
    * Given the root to such a tree, write a function to evaluate it.
    * For example, given the following tree:
    ```
          *
         / \
        +    +
       / \  / \
      3  2  4  5
    ```
    * You should return 45, as it is (3 + 2) * (4 + 5).
* Problem #51 (Facebook)
    * Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is
      an input, write a function that shuffles a deck of cards represented as an array using only swaps.
    * It should run in `O(N)` time.
    * Hint: Make sure each one of the 52! permutations of the deck is equally likely.
* Problem #52 (Google)
    * Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size
      `n`, and contain the following methods:
    * `set(key, value)`: sets key to value. If there are already n items in the cache and we are adding a
      new item, then it should also remove the least recently used item.
    * `get(key)`: gets the value at key. If no such key exists, return null.
    * Each operation should run in O(1) time.
* Problem #53 (Apple)
    * Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure
      with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes
      it.
* Problem #54 (Dropbox)
    * Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. The objective is
      to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain
      all of the digits from 1 to 9.
    * Implement an efficient sudoku solver.
* Problem #56 (Google)
    * Given an undirected graph represented as an adjacency matrix and an integer k, write a function to
      determine whether each vertex in the graph can be colored such that no two adjacent vertices share
      the same color using at most k colors.
* Problem #57 (Amazon)
    * Given a string s and an integer k, break up the string into multiple texts such that each text has
      a length of k or less. You must break it up so that words don't break across lines. If there's no
      way to break the text up, then return null.
    * You can assume that there are no spaces at the ends of the string and that there is exactly one
      space between each word.
    * For example, given the string `"the quick brown fox jumps over the lazy dog"` and `k = 10`, you
      should return: `["the quick", "brown fox", "jumps over", "the lazy", "dog"]`. No string in the
      list has a length of more than 10.
* Problem #58 (Amazon)
    * An sorted array of integers was rotated an unknown number of times.
    * Given such an array, find the index of the element in the array in faster than linear time. If
      the element doesn't exist in the array, return null.
    * For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8
      in the array).
    * You can assume all the integers in the array are unique.
* Problem #60 (Facebook)
    * Given a set of integers, return whether the set can be partitioned into two subsets whose sums
      are the same.
    * For example, given the set {15, 5, 20, 10, 35, 25, 10}, it would return true, since we can split
      the set up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.
    * Given the set {15, 5, 20, 10, 35}, it would return false, since we can't split the set up into two
      subsets that add up to the same sum.
* Problem #61 (Google)
    * Implement integer exponentiation. That is, implement the `pow(x, y)` function, where x and y are
      integers and returns `x^y`.
    * Do this faster than the naive method of repeated multiplication.
    * For example, pow(2, 10) should return 1024.
* Problem #62 (Facebook)
    * There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways
      of starting at the top-left corner and getting to the bottom-right corner. You can only move right
      or down.
    * For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the
      bottom-right:
      * Right, then down
      * Down, then right
    * Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
* Problem #63 (Microsoft)
    * Given a 2D matrix of characters and a target word, write a function that returns whether the word
      can be found in the matrix by going left-to-right, or up-to-down.
    * For example, given the following matrix:
      ```
      [
        ['F', 'A', 'C', 'I'],
        ['O', 'B', 'Q', 'P'],
        ['A', 'N', 'O', 'B'],
        ['M', 'A', 'S', 'S']
      ]
      ```
      and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given
      the target word 'MASS', you should return true, since it's the last row.
* Problem #64 (Google)
    * A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are
      visited once.
    * Given N, write a function to return the number of knight's tours on an N by N chessboard.
* Problem #65 (Amazon)
    * Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
    * For example, given the following matrix:
      ```
      [
        [1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
      ]
      ```
      You should return the following:
      ```
      [
        1, 2, 3, 4, 5,
        10, 15, 20, 19, 18,
        17, 16, 11, 6, 7,
        8, 9, 14, 13, 12,
      ]
      ```
* Problem #66 (Square)
    * Assume you have access to a function toss_biased() which returns 0 or 1 with a probability
      that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.
    * Write a function to simulate an unbiased coin toss.
* Problem #68 (Google)
    * On our special chessboard, two bishops attack each other if they share the same diagonal.
      This includes bishops that have another bishop located between them, i.e. bishops can attack
      through pieces.
    * You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a
      function to count the number of pairs of bishops that attack each other. The ordering of the
      pair doesn't matter: (1, 2) is considered the same as (2, 1).
    * For example, given M = 5 and the list of bishops:
      ```
      (0, 0)
      (1, 2)
      (2, 2)
      (4, 0)
      ```
      The board would look like this:
      ```
      [b 0 0 0 0]
      [0 0 b 0 0]
      [0 0 b 0 0]
      [0 0 0 0 0]
      [b 0 0 0 0]
      ```
    * You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.
* Problem #69 (Facebook)
    * Given a list of integers, return the largest product that can be made by multiplying any three
      integers.
    * For example, if the list is `[-10, -10, 5, 2]`, we should return 500, since that's `-10 * -10 * 5`.
* Problem #70 (Microsoft)
    * A number is considered perfect if its digits sum up to exactly 10.
    * Given a positive integer n, return the n-th perfect number.
    * For example, given 1, you should return 19. Given 2, you should return 28.
* Problem #73 (Google)
    * Given the head of a singly linked list, reverse it in-place.
* Problem #74 (Apple)
    * Suppose you have a multiplication table that is N by N. That is, a 2D array where the value at the
      i-th row and j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).
    * Given integers N and X, write a function that returns the number of times X appears as a value in
      an N by N multiplication table.
    * For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like
      this:
      ```
      | 1 | 2  | 3  | 4  | 5  | 6  |
      | 2 | 4  | 6  | 8  | 10 | 12 |
      | 3 | 6  | 9  | 12 | 15 | 18 |
      | 4 | 8  | 12 | 16 | 20 | 24 |
      | 5 | 10 | 15 | 20 | 25 | 30 |
      | 6 | 12 | 18 | 24 | 30 | 36 |
      ```
      And there are 4 12's in the table.
* Problem #75 (Microsoft)
    * Given an array of numbers, find the length of the longest increasing subsequence in the array. The
      subsequence does not necessarily have to be contiguous.
    * For example, given the array `[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]`, the longest
      increasing subsequence has length 6: it is `0, 2, 6, 9, 11, 15`.
* Problem #76 (Google)
    * You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns
      that can be removed to ensure that each row is ordered from top to bottom lexicographically. That
      is, the letter at each column is lexicographically later as you go down each row. It does not matter
      whether each row itself is ordered lexicographically.
    * For example, given the following table:
      ```
      cba
      daf
      ghi
      ```
      This is not ordered because of the a in the center. We can remove the second column to make it ordered:
      ```
      ca
      df
      gi
      ```
      So your function should return 1, since we only needed to remove 1 column.
    * As another example, given the following table:
      ```
      abcdef
      ```
      Your function should return 0, since the rows are already ordered (there's only one row).
    * As another example, given the following table:
      ```
      zyx
      wvu
      tsr
      ```
    * Your function should return 3, since we would need to remove all the columns to order it.
* Problem #77 (Snapchat)
    * Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping
      intervals have been merged.
    * The input list is not necessarily ordered in any way.
    * For example, given `[(1, 3), (5, 8), (4, 10), (20, 25)]`, you should return `[(1, 3), (4, 10), (20, 25)]`.
* Problem #78 (Google)
    * Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly
      linked list.
* Problem #79 (Facebook)
    * Given an array of integers, write a function to determine whether the array could become non-decreasing
      by modifying at most 1 element.
    * For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to
      make the array non-decreasing.
    * Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-
      decreasing array.
* Problem #80 (Google)
    * Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.
      ```
          a
         / \
        b   c
       /
      d
      ```
* Problem #81 (Yelp)
    * Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters
      the number could represent. You can assume each valid number in the mapping is a single digit.
    * For example if `{“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …}` then “23” should return
      `[“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"]`.
* Problem #83 (Google)
    * Invert a binary tree.
    * For example, given the following tree:
      ```
          a
         / \
        b   c
       / \  /
      d   e f
      ```
      should become:
      ```
        a
       / \
      c   b
       \  / \
        f e  d
      ```
* Problem #131 (Snapchat)
    * Given the head to a singly linked list, where each node also has a “random” pointer that points
      to anywhere in the linked list, deep clone the list.
* Problem #134 (Facebook)
    * You have a large array with most of the elements as zero.
    * Use a more space-efficient data structure, `SparseArray`, that implements the same interface:
      * `init(arr, size)`: initialize with the original large array and size.
      * `set(i, val)`: updates index at i with val.
      * `get(i)`: gets the value at index i.
* Problem #135 (Apple)
    * Given a binary tree, find a minimum path sum from root to a leaf.
    * For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.
    ```
        10
       /  \
      5    5
       \     \
        2    1
            /
          -1
    ```
* Problem #138 (Google)
    * Find the minimum number of coins required to make n cents.
    * You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.
    * For example, given `n = 16`, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
