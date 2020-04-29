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


def spiral_matrix(matrix):
    """
    Print a matrix in a clockwise spiral pattern
    """
    left = 0
    right = len(matrix[0]) - 1
    top = 0
    bottom = len(matrix) - 1
    res = []

    while left < right and top < bottom:
        # go along top
        for top_idx in range(left, right+1):
            res.append(matrix[top][top_idx])
        top += 1

        # go along right
        for right_idx in range(top, bottom+1):
            res.append(matrix[right_idx][right])
        right -= 1

        # go along bottom
        for bottom_idx in range(right, left-1, -1):
            res.append(matrix[bottom][bottom_idx])
        bottom -= 1

        # go along left
        for left_idx in range(bottom, top-1, -1):
            res.append(matrix[left_idx][left])
        left += 1

    return res
