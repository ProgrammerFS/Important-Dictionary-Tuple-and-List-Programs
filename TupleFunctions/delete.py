#this deletes the whole tuple 
t = (1, 2, 3, 4)
del t
print(t)  # gives error
#u cannot do del t[0:2] because tuples are immutable this will give error 