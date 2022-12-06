def get_pos_from_string(input_string, as_ints, *args):
    result = []
    for pos in args:
        if as_ints:
            result.append(int(input_string[pos]))
        else:
            result.append(input_string[pos])
    return result


test_string = "abcdefghij"
test_numbers = "123456789"

test_char = get_pos_from_string(test_string, False, 4, 6, 7)
print(f"test_char: {test_char}")

test_char = get_pos_from_string(test_numbers, True, 4, 6, 7, 8)
print(f"test_char: {test_char}")
