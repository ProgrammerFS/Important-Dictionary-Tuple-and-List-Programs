#We can delete elements by using del function
d = {1: 'one', 2: 'two', 3: 'three'}
del d[1]  # always give the key not the value
print(d)  # prints {2: 'two', 3: 'three'}

#We can delete elements by using pop also
d = {1: 'one', 2: 'two', 3: 'three'}
d.pop(1)
print(d)  # prints {2: 'two', 3: 'three'}

#We can also use popitem which deletes the last item of a dictionary
d = {1:"one", 2: 'two', 3: 'three'}
d.popitem()
print(d)  # prints {1: 'one', 2: 'two'}
