#Dictionary implementation

dict_a = {'a': 1, 'b': 2}
dict_b = {'b': 3, 'c': 4}

print("dict_a is : ",dict_a)
print("dict_b is : ",dict_b)

dict_a['ram']=5545
print(f"\nWe can use = operator also. like dict_a['ram']=5545 ==>   ",dict_a)

print(f"dict_a['a'] is: {dict_a['a']}")

del dict_a['a']
print("del dict_a['a']: ", dict_a)

#*******************************************************************************************
print("*".center(60,"*"))
print("update method updates the value, if both the dict has same key, it will update with the later one\n")
#1. using two dict
dict_c = {'B': 1234, 'C': 5678}
dict_a.update(dict_c)
print("dict_a.update(dict_c): ",dict_a) 

#2. using direct value passing using key=value format
print("another way of using update: ")
dict_a.update(D=5486, E=4095)
print(dict_a)

#3. When two dict used in update have same key ==> will replace with the value of later one 
print("dict_a is : ",dict_a)
print("dict_b is : ",dict_b)
dict_a.update(dict_b)
print("After dict_a.update(dict_b): ", dict_a)  # Output: {'a': 1, 'b': 3, 'c': 4}

#*******************************************************************************************
print("\nSorted(dict_a): ",sorted(dict_a))


print(f"'A' in dict_a","A" in dict_a)
print(f"'B' in dict_a","B" in dict_a)
print(f"'C' not in dict_a","C" not in dict_a)


#******************************************************************************************
print("*".center(60,"*"))
print("another ways to create a dictionary")
#The dict() constructor builds dictionaries directly from sequences of key-value pairs:
d1 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]) #passing the tuples in key value pair in list and then to dict constructor
print(d1)

d3 = dict(zip(['sape', 'guido', 'jack'], [4139, 4127, 4098]))
print(d3)

keys = (1,2,3,4,5) #Note this is a tuple, it can be list also
val = "hari"
d4 = dict.fromkeys(keys,val)
print(d4)

print("What if we only give keys")
d5 = dict.fromkeys(keys) 
print(d5)

#Updating value using key
d1['sape']=1000
print(d1)

print("Methods".center(60,"*"))
print(f"get() gives the value of the key given in argument. dict_a.get('guido'): {dict_a.get('B')}")

print(f"items()	Returns a list containing a tuple for each key value pair",dict_a.items())

print(f"keys()	Returns a list containing the dictionary's keys. dict_a.keys(): ",dict_a.keys())
print(f"values() returns the list of all values of the dict. dict_a.values(): ", dict_a.values())

dict_a.pop('C')
print(f"pop() removes the ele with the key given. dict_a after pop('c'): ", dict_a)

#popitem() method removes the item that was last inserted into the dictionary. Before v3.7, the popitem() method removes a random item.
dict_a.popitem()
print("After dict.popitem() dict_a", dict_a)


print("creating dictionary differently")
d0={x: x**2 for x in (2, 4, 6)}
print(d0)

d0.clear()
print("clear function",d0)

#*******************************************************************************************
print("*".center(60,"*"))
for k, v in dict_a.items():
    print(k,v)
    
    
#*******************************************************************************************
print("*".center(60,"*"))
for i, v in enumerate(d1):
    print(i,v)
    
#*******************************************************************************************
print("*".center(60,"*"))
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for k, v in zip(questions, answers):    #zipping and extracting at the same time
    print(f"What is you {k}. Answer is: {v}")
    

for i in sorted(questions):
    print(i)