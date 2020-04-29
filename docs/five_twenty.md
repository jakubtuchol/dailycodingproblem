# Problems 520 - 529

* Problem #523 (Jane Street) *DONE*
    * Given integers `M` and `N`, write a program that counts how many positive integer pairs `(a, b)` satisfy the following conditions:
        * `a + b = M`
        * `a XOR b = N`
* Problem #524 (Amazon) *DONE*
    * Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
    * For example, given the array `[34, -50, 42, 14, -5, 86]`, the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.
    * Given the array `[-5, -1, -8, -9]`, the maximum sum would be 0, since we would not take any elements.
* Problem #525 (Amazon)
    * Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
    * For example, given the following matrix:
```
[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
```
    * You should print out the following:
        * `1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12`