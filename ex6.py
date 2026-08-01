# Input
user_age = input('Enter your age:\t')
print(type(user_age))

if int(user_age) >= 18:
    print("You can apply for this university")
else:
    print("You are under the legal age to enter this university")
