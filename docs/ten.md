# Problems #10 - 19

* Problem #10 (Apple)
    * Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
* Problem #11 (Twitter) *DONE*
    * Implement an autocomplete system. That is, given a query string s and a dictionary of all possible query strings, return all strings in the dictionary that have s as a prefix.
* Problem #12 (Amazon) *DONE*
    * There exists a staircase with N steps, and you can climb up either 1 or 2
      steps at a time. Given N, write a function that returns the number of unique
      ways you can climb the staircase. The order of the steps matters.
    * For example, if N is 4, then there are 5 unique ways:
        * `1, 1, 1, 1`
        * `2, 1, 1`
        * `1, 2, 1`
        * `1, 1, 2`
        * `2, 2`
    * What if, instead of being able to climb 1 or 2 steps at a time, you could
      climb any number from a set of positive integers X? For example, if X = {1, 3, 5},
      you could climb 1, 3, or 5 steps at a time.
* Problem #13 (Amazon) *DONE*
    * Given an integer k and a string s, find the length of the longest substring
      that contains at most k distinct characters.
    * For example, given s = "abcba" and k = 2, the longest substring with k
      distinct characters is "bcb", so your function should return 3.
* Problem #14 (Google) *DONE*
    * The area of a circle is defined as πr^2. Estimate π to 3 decimal places using
      a Monte Carlo method.
    * Hint: The basic equation of a circle is x2 + y2 = r2.
* Problem #15 (Facebook) *DONE*
    * Given a stream of elements too large to store in memory, pick a random element
      from the stream with uniform probability.
* Problem #16 (Twitter) *DONE*
    * You run a sneaker website and want to record the last N order ids in a log.
      Implement a data structure to accomplish this, with the following API:
      * record(order_id): adds the order_id to the log
      * get_last(i): gets the ith last element from the log. i is guaranteed to
        be smaller than or equal to N.
