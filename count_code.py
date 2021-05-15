def count_code(str):
    count = 0

    for i in range(len(str) - 3):
        if str[i:i + 2] + str[i + 3] == 'coe':
            count += 1
    return count

assert count_code('aaacodebbb') == 1
assert count_code('xxcozeyycop') == 1
assert count_code('AAcodeBBcoleCCccoreDD') == 3