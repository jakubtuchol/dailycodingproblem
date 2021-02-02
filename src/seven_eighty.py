def is_palindrome(num):
    temp_num = num

    # get highest integer
    hi_place = 10
    while temp_num:
        temp_num -= (temp_num % hi_place)
        if temp_num:
            hi_place *= 10

    hi_place /= 10
    lo_place = 10

    while lo_place < hi_place:
        hi_digit = int(num / hi_place)
        lo_digit = num % lo_place

        if lo_digit != hi_digit:
            return False

        num -= lo_digit
        num -= hi_digit * hi_place

        lo_place *= 10
        hi_place /= 10

    return True
