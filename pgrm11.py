#Tuple Implementation

tup= (1)    #Python consider this as int type, usko lagta hain ki ek int ko () me pass kar rhe

tup1 = (1,) #Here, it will take it as tuple

print(type(tup), type(tup))

tup2 = (1,2,5,3,7)

tup1 = tup2
print(id(tup1), id(tup2))   #same as list

# As list tuples can have duolicate elements
tup2 = (1,2,3,4,5,1,2)
print(tup2)

#Immutable tuple
#tup2[1]=3   #Error

#changes in tuple is not possible so convert it to list and do the changes and convert it back to tuple
list1 = list(tup2)
list1.append(10)
list1[1]=100
list1.pop(3)
tup2 = tuple(list1)
print(tup2)