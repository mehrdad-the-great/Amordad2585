# Review3
my_student = {
    'Full name': 'Helena SasanNejad',
    'Age': 21,
    'National ID': '1270851423',
    
    'Marks': [
        {'title': 'Math', 'mark': 20},
        {'title': 'Basic Programming', 'mark': 19.5},
    ],

    'Intrests': {
        'Mountaineer': 'Very Intrested', 
        'Biking': 'Intrested', 
        'Reading': 'Loving',
    },
    
    'Family': {
        'parents': {
            'father': 'Bahram',
            'mother': 'Taraneh',
        },

        'ciblings': {
            'brothers': ['Saman', 'Reza', 'Ahoora',],
            'sisters': ['Helia', ],
        },
    },
}

# How much is your student intrested in Biking?
print(my_student['Intrests']['Biking'])

# What is your student's score in Basic Programming?
print(my_student['Marks'][1]['mark'])

# How many brothers does your student have? And what are their names?
print('-------')
brothers = my_student['Family']['ciblings']['brothers']
print(f'{my_student['Full name']} has {len(brothers)} brother(s):')
for brother in brothers:
    print(brother)
print('-------')

# What is the name of your student's mother?
print(my_student['Family']['parents']['mother'])

# Item assignment
mark_dict = {'title': 'Chemistry', 'mark': 18}
my_student['Marks'].append(mark_dict)

my_student['Family']['ciblings']['sisters'].append('Elaheh')

print(my_student)

# Calculate your student's average of marks
marks = []
for item in my_student['Marks']:
    marks.append(item['mark'])

print(sum(marks)/len(marks))
