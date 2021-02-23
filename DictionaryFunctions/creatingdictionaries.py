# Way 1 => Straight away create it
d = {1: "one", 2: "two", 3: "three"}

#Way 2 => create an empty dictionary then add key-value pairs
d = {}  # first initialize an empty dictionary then add key value pairs to it
d[1] = "one" #key = 1, value = "one"
d[2] = "two" #key = 2, value = "two"
d[3] = "three"  # key = 3, value = "three"
print(d)  # prints {1: 'one', 2: 'two', 3: 'three'}

#Way 3 => by using dict function
d = dict(one=1, two=2)
print(d)  # prints {'one': 1, 'two': 2}

#Way 4 => by sequence list or tuple
l = [[1, "one"], [2, "two"], [3, "three"]]
d = dict(l)
print(d)  # prints {1: 'one', 2: 'two', 3: 'three'}




