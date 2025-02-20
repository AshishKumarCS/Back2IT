#Set Implementation - It doesn't contains duplicates & not keeps the sequence

s = {1,2,2,3,4,5}
print(s)

for item in s:
    print(item)
    
#check something is in set or not
print(f'5 in s : {5 in s}')
print(f'10 in s: {10 in s}')

#Getting unique letters from a word
s1 = set("Ashish")
print(s1)
s2 = set("Kumar Harish")
print(s2)
# some of the set functions that can easily be used

#Difference: In s1 but not in s2  ==> minus
print(f"Difference: {s1-s2}") #Only 'A' is not in s2
print("This can also be done using .difference() :", s1.difference(s2))
s1.difference_update(s2)
print("another method difference_update() will update s1 the calling set with difference. values in s1 after --> s1.difference_update(s2) ", s1)

#Intersection: in both   ==> &
print(f"\nIntersection: {s1 & s2}")
print("Same can be done using the intersection() and intersection_update() methods")

#Union: all items of s1 and s2  ==> |
print(f"\nUnion: {s1 | s2}")
print("Same thing can be done using union(): ", s1.union(s2))

#Compliment: All items except not common
print(f"\nCompliment : {(s1 | s2)-(s1 & s2)}")

#set comprehension
print("\nSet comprehension: ", end='')
print({x for x in 'abracadabra' if x not in 'abc'})
'''Let's break it down step by step:

1. 'abracadabra' – This is a string containing the characters: 'a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a'.

2. {x for x in 'abracadabra'} – This is a set comprehension that creates a set of unique characters from the string 'abracadabra'.

3. if x not in 'abc' – This filters out the characters 'a', 'b', and 'c', meaning they will not be included in the set.

4. Result: The remaining characters are 'r' and 'd', so the output will be:

   python
   {'r', 'd'}
   
### In simple terms:
- We take each letter from 'abracadabra'.
- We remove 'a', 'b', and 'c' from the selection.
- We store the remaining letters in a set (which automatically removes duplicates).
- The final output is {'r', 'd'}.
'''
#isdisjoint() - Checks whether the sets are disjoint or not
print("\ns1.isdisjoint(s2): ", s1.isdisjoint(s2))

#issubset()	- Returns True if all elements of a set A are present in another set B
s3 = set('abracadabra')
s4 = set('rac')
print(f's3 is {s3} and s4 is {s4} and s4.issubset(s3) is : {s4.issubset(s3)}')


s1 = set("Kumar Harish")    #as so many actions performed, re intialising the values
#add()
s1.add(1)
print('\nAfter s1.add() use: ',s1) 

#discard()
s1.discard('h')
print("\nAfter s1.discard('h'): ",s1) 
print('If element is not in the set no error will be thrown'.center(60,'*'))
s1.discard('p')
print(f"After s1.discard('p'): ",s1)

#remove()
print("\ns1 is ", s1)
s1.remove('s')
print(f"After s1.remove('s'): ",s1) 
print('\nRemove method is same as discard, but it THROWS error if element not exists'.center(80,'*'))
#print('If k is not in the set no error will be thrown'.center(60,'*'))
#s1.remove('p')
#print(f"After s1.discard('p'): ",s1)  #this line will not execute

#copy()
s5 = s1
print("s5 is ",s5)
print("\ns5.clear() ", s5.clear())

s6 = s1.copy()
print("\ns6 = s1.copy()", s6)

#update()	Adds elements to the set 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print(f"\nx set is : {x}")
print(f"y set is : {y}")
x.update(y)
print(f"After x.update(y): x is {x}")

#pop()
print("x.pop() =  ",x.pop(),"<-- Evertime this value will be different as set doesn't maintain order")