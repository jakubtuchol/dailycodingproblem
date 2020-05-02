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


def num_decodings(code):
    """
    Given an alphanumeric mapping and an encoded message, count
    the number of ways it can be decoded
    """
    decodings = []

    for idx in range(len(code)):
        # check one letter before
        if code[idx] == '0':
            # zero is special case that maps only to being part of
            # 10 or 20, so it doesn't have a place in the one-letter
            # mapping
            one_letter = 0
        else:
            one_letter = decodings[idx-1] if idx > 0 else 1
        # check two letter code
        if idx >= 1 and 10 <= int(code[idx-1:idx+1]) <= 26:
            two_letter = decodings[idx-2] if idx > 1 else 1
        else:
            two_letter = 0
        decodings.append(one_letter + two_letter)

    return decodings[-1]


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
