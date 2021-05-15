def count_hi(str):
    return str.count('hi')



def count_hi(str):
    count = 0
    for i in range(len(str) - 1):
        if str[i:i + 2] == 'hi':
            count += 1

    return count