def urliFy(s, l):
    output = []
    for i in range(0,len(s)):
        if i == l: break
        elif s[i] == ' ': output.append("%20")
        else: output.append(s[i])
    print(''.join(output))
    return ''.join(output)


assert urliFy("Mr John Smith   ",13) == "Mr%20John%20Smith"
assert urliFy("anil kumar John bayy av ar apuuuuuu uu uu uuuuuuuu",30) == "anil%20kumar%20John%20bayy%20av%20ar%20apu"