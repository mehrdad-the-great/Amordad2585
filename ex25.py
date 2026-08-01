# Practice39
student = {
    'name': 'Arash',
    'mark': 17,
    'rank': 9,
    'classes': ['math', 'gym', 'chemistry', 'history'],
    
    'family': {

        'ciblings': {
            'brothers': [
                {'name': 'Saman', 'age':27},
                {'name': 'Dara', 'age':14},
            ],
            'sisters': [
                {'name': 'Anita', 'age':40},
                {'name': 'Armita', 'age':30},
                {'name': 'Helia', 'age':12},
            ],
        },

        'parents': {
            'father': {
                'name': 'Ali',
                'age': 49
            },
            'mother': {
                'name': 'Sara',
                'age': 46
            }
        }
    }
}

# classes list: add 'programming'
student['classes'].append('programming')
print(student['classes'])
# what is the name of the student's father?
print(student['family']['parents']['father']['name'])
# How old is the second sister of the student?
print(student['family']['ciblings']['sisters'][1]['age'])

# Give me the names of the student's brothers and tell me how many they are
print('-' * 10)
brothers = student['family']['ciblings']['brothers'] # list of dicts
print(f'This student has {len(brothers)} brothers:')
for brother in brothers:
    print(brother['name'])
print('-' * 10)

# What is the first item in the student's classes list?
print(student['classes'][0])
# What is the name of student's second brother?
print(student['family']['ciblings']['brothers'][1]['name'])
# Add a sister with the name 'Helena', age 10
student['family']['ciblings']['sisters'].append({'name': 'Helena', 'age': 10})
print(student['family']['ciblings']['sisters'])
