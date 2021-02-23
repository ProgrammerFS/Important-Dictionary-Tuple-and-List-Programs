# this adds a list to another list
l1 = [1, 2, 3, 4] 
l2 = [5, 6, 7, 8]
l1.extend(l2)  #Only l1 will be changed l2 will remain as it is
print(l1)  # prints [1, 2, 3, 4, 5, 6, 7, 8]
print(l2)  # prints [5, 6, 7, 8]
