def cat_dog(str):
    return str.count('cat') == str.count('dog')



def cat_dog(str):
    c1 = 0
    c2 = 0

    for i in range(len(str) - 2):

        if str[i:i + 3] == 'cat':
            c1 += 1
        if str[i:i + 3] == 'dog':
            c2 += 1

    return c1 == c2

def cat_dog(str):
    c1 = 0
    c2 = 0

    for i in range(len(str) - 2):

        if str[i:i + 3] == 'cat':
            c1 += 1
        if str[i:i + 3] == 'dog':
            c2 += 1

    return c1 == c2


assert cat_dog('catxxdogxxxdog') == False
assert cat_dog('dogogcat') == True
