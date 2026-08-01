# Practice 40
my_tuple = (1, 2, 3)
print(my_tuple[:1], my_tuple[::-1], my_tuple[-1])

# Practice 41
user_age = 17
minimum_age_required = 25

is_user_allowed_to_access_media = (user_age >= minimum_age_required)
print(is_user_allowed_to_access_media)


middle_east_countries = ['Iran', 'Syria', 'Egypt', 'Saudi Arabia', 'Iraq', 'Lebonan', 'Israel', 'Kuwait']
user_country = input("Enter your region's name: ")
is_user_from_middle_east_countries = (user_country in middle_east_countries)
if is_user_from_middle_east_countries:
    print('You are from Middle East')
else:
    print('You are not from Middle East')
