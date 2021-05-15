def decodestring(input):
    temp1 = input.split("[")
    temp2 = ''.join(temp1).split("]")
    output = []
    for s in temp2:
        if s != '':
            output.append(s[1:] * int(s[0]))
    print(''.join(output))
    return ''.join(output)


assert decodestring("3[a]2[bc]") == "aaabcbc"