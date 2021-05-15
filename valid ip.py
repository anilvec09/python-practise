import re
def validIPAddress( IP: str) -> str:
    reg_v6 = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    r_v4 = r'(([2][0-5][0-5])|([1][0-9][0-9])|([1-9][0-9])|([0-9]))'
    reg_v4 = re.compile(r'^(' + r_v4 + r'\.){3}' + r_v4 + r'$')
    if re.search(reg_v6, IP): return 'IPv6'
    if re.search(reg_v4, IP): return 'IPv4'
    return 'Neither'

assert validIPAddress("172.16.254.1") == 'IPv4'
assert validIPAddress("172.16.258.1") == 'Neither'

assert validIPAddress("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == 'IPv6'

def validip(s):
    if not s:
        return
    if s.count('.') != 3:
        return False
    for i in s.split('.'):
        if not i.isdigit() or int(i) > 255 or len(i) > 3 or i[0] == '0':
            return False
    return True


assert validip("172.16.254.abc") == True
assert validip("172.16.258.1") == False


# def validip(s):
#
#     if not s:
#         return
#
#     patterip = r'(([0-9])|([1-9][0-9])|(2[0-5][0-5])|(1[0-9][0-9]))'
#     patternipcomplete = re.compile(r'^('+ patterip + r'\.){3}' + patterip + r'$')
#                         # re.compile(r'^(' + patterip + r'\.){3}' + patterip + r'$')
#
#     if re.match(patternipcomplete , s):
#         return True
#     else:
#         return False
#
# assert validip("172.16.254.1") == True
# assert validip("172.16.258.1") == False