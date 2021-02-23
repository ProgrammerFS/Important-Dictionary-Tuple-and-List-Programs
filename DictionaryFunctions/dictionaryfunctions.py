#len() method
#it returns the length of a dictionary
d = {1: 'one', 2: 'two', 3: "three"}
print(len(d))  # prints 3

#clear() method
#it deletes all the content of the dictionary without actually deleting the dictionary
d = {1: 'one', 2: 'two', 3: "three"}
d.clear()
print(d)  # prints {}

#get() method
#it gives the item with the given key or it returns the value we put after a comma if the key doesnt exist
d = {1: 'one', 2: 'two', 3: "three"}
print(d.get(1))  # prints one
print(d.get(4, 0))  # prints 0 because the key 4 doesnt exist

#keys() method
#it returns the list of all the keys in the dictionary
d = {1: 'one', 2: 'two', 3: "three"}
print(d.keys())  # prints dict_keys([1, 2, 3])

#values() method
#it returns the list of all the values in the dictionary
d = {1: 'one', 2: 'two', 3: "three"}
print(d.values())  # prints dict_values(['one', 'two', 'three'])

#items() method
#it returns the list of tuples in which tuple is (key, value)
d = {1: "one", 2: "two", 3: "three"}
print(d.items())  # prints dict_items([(1, 'one'), (2, 'two'), (3, 'three')])
# here in (1,"one") 1 is the key and 'one' is value

#update()method
#it adds two dictionary and stores it in the original dictionary
d1 = {1: 'one', 2: 'two', 3: "three"}
d2 = {4: "four", 5: "five"}
d1.update(d2)
print(d1)  # prints {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
#only d1 gets updated d2 remains as it is
print(d2)  # prints {4: 'four', 5: 'five'}

#setdefault() method
#its format is d.setdefault(key, value)
#if key is there it returns the value of the key
#otherwise it will add that element to the dictionary and return the value
d = {1: 'one', 2: 'two', 3: "three"}
print(d.setdefault(4, "four")) # adds the key 4 with value "four" to the dictionary and prints four
print(d.setdefault(3, 0)) # prints the value of the key 3 because it already exists
print(d)  # prints {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
