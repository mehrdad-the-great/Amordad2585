# Comparison: not
a = 400
print(not (a > 0))
# not(True) -> False

print(not (a > 300 and 'Hello' == 'hi'))
# not(True and False) -> not(False) -> True

print(a > 300 and not (a == 100))
# True and not(False) -> True and True -> True

print(not(a == 400 or 'Hello' == 'Hi'))
# not(True or False) -> not(True) -> False

print(a == 400 and (a < 0 or 'Hello' == 'Hello'))
# True and (False or True) -> True and True -> True
