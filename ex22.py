# Practice34
my_dict = {
    "key1": 100,
    "key2": 200,
    "key3": 300
}
print(my_dict['key1'])

my_dict = {
    "mylist": [1,2,45,100],
    "strings": ["hello", "hi"],
    "num": 7,
}
print(my_dict['mylist'][-1])

my_dict = {
    "mydict": {
        "values": [1, 5, 'hi', 100]
    },
    "strings": ["hello", "hi"],
    "num": 7,
}
print(my_dict['mydict']['values'][3])
my_dict['mydict']['values'][2:] = []
print(my_dict)

my_dict = {
    "mydict": {
        "inner": {
            "key1": 'hi',
            "key2": [1, 'day', 100, 'bye']
        },
        "inner2": {
            "key1": 8,
            "second": 1
        }
    },

    "strings": [
        "hello", "hi", 11
    ],

    "num": 10,
}

my_dict['mydict']['inner']['key2'].insert(2, 99)
print(my_dict['mydict']['inner']['key2'][2:4])
