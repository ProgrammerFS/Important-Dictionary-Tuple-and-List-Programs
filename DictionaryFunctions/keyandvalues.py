#d.keys()
#it returns the list of all keys in a dictionary
d = {1: "one", 2: "two", 3: "three"}
print(d.keys())  # prints dict_keys([1, 2, 3])

#d.values()
#it returns the list of all values in a dictionary
d = {1: "one", 2: "two", 3: "three"}
print(d.values())  # prints dict_values(['one', 'two', 'three'])

#d.items()
#it returns the list of tuples in which tuple is (key, value)
d = {1: "one", 2: "two", 3: "three"}
print(d.items())  # prints dict_items([(1, 'one'), (2, 'two'), (3, 'three')])
                  # here in (1,"one") 1 is the key and 'one' is value

