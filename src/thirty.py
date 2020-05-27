def edit_distance(word_one, word_two):
    # short-circuit conditions
    if word_one == word_two:
        return 0

    shorter = min(word_one, word_two, key=len)
    longer = max(word_one, word_two, key=len)

    if not shorter and longer:
        return len(longer)

    edit_matrix = []

    for _ in range(len(word_one)):
        row = [0] * len(word_two)
        edit_matrix.append(row)

    for idx_one, char_one in enumerate(word_one):
        for idx_two, char_two in enumerate(word_two):
            edit = 0 if char_one == char_two else 1
            prev_edits = []
            # check above
            if idx_one > 0:
                prev_edits.append(edit_matrix[idx_one-1][idx_two])

            if idx_two > 0:
                prev_edits.append(edit_matrix[idx_one][idx_two-1])

            if idx_one > 0 and idx_two > 0:
                prev_edits.append(edit_matrix[idx_one-1][idx_two-1])

            prev_edit_min = min(prev_edits) if prev_edits else 0
            edit_matrix[idx_one][idx_two] = prev_edit_min + edit

    return edit_matrix[-1][-1]
