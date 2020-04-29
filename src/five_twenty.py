def find_sum_xor_pairs(m, n):
    """
    Find the number of int pairs that sum to m and xor to n
    """
    counter = 0
    upper_limit = m // 2 + 1

    for idx in range(1, upper_limit):
        jdx = m - idx
        if idx ^ jdx == n:
            counter += 1
    return counter


def max_sum_subarray(arr):
    """
    Find maximum the sum of any contiguous subarray
    """
    max_thus_far = 0
    max_ending_here = 0

    for elt in arr:
        max_ending_here += elt

        if max_ending_here < 0:
            max_ending_here = 0

        max_thus_far = max(max_ending_here, max_thus_far)

    return max_thus_far
