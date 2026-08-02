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


username = input('Please choose a username (5-15 chars): ')
password = input('Please enter a strong password(8-30 chars): ')

username_condition = (5 <= len(username) <= 15)
password_condition = (8 <= len(password) <= 30)

if username_condition and password_condition:
    print('Succesfully saved! thumbs up :)')

else:
    print('Failed to save. See troubleshooting below: ')
    if not username_condition:
        print(f'Username-length ({len(username)}) invalid.')
    if not password_condition:
        print(f'Password-length ({len(password)}) invalid.')
