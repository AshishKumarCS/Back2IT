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
tup2[1]=3   #Error