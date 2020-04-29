def find_sum_xor_pairs(m, n):
    """
    Find the number of int pairs that sum to m
    and xor to n
    """
    counter = 0
    upper_limit = m // 2 + 1

    for idx in range(1, upper_limit):
        jdx = m - idx
        if idx ^ jdx == n:
            counter += 1
    return counter
