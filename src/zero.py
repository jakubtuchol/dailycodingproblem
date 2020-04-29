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
