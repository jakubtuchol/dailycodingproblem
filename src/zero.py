def two_sum(arr, k):
    """
    Return whether or two elements in an array sum to k
    """
    seen = set()

    for elt in arr:
        if elt in seen:
            return True
        seen.add(k - elt)

    return False


def find_missing_integer(arr):
    """
    Find the first missing integer in unsorted array of integers
    """
    # segregate integers, with negative (including zero) on right and positives
    # on left
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] > 0:
            left += 1
        elif arr[right] <= 0:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    # mark indexes of positive integers as negative
    for idx in arr[:left+1]:
        pos_idx = abs(idx)
        if pos_idx < len(arr):
            arr[pos_idx-1] = -abs(arr[pos_idx-1])

    # find first positive integer
    for idx, elt in enumerate(arr[:left+1]):
        if elt > 0:
            return idx + 1

    return left + 1


def largest_nonadjacent_sum(arr):
    """
    Find the largest sum of non-adjacent numbers
    """
    before_last = 0
    last = 0

    for elt in arr:
        cur = before_last + elt
        before_last = max(before_last, last)
        last = max(cur, last)
    return last
