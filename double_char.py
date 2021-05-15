def double_char(str):
    op = ''
    for i in str:
        op += i * 2
    return op

assert double_char('AAbb') == 'AAAAbbbb'
assert double_char('Hi-There') == 'HHii--TThheerree'