def end_other(a, b):
  if  a.lower().endswith(b.lower())  or b.lower().endswith(a.lower()):
    return True
  return False


assert end_other('Hiabc', 'abc') == True
assert end_other('Hiabc', 'abcd') == False