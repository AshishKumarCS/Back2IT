#List implementation

fruits = [
    "Apple",  "Mango", "Orange",
    "Pineapple", "Strawberry", "Guava", "Mango"
    "Raspberry"
]

print("Every 3rd value: ",fruits[::3])

#Very Important: for the below command it must be included inside [ ]
print("Only those fruits which has \'r\' in it", [fruit for fruit in fruits if "r" in fruit])

print("Only those whose name length >7", [fruit for fruit in fruits if len(fruit)>7])

'''From here onwards methods of list are being implemented '''

print("Append".center(20,"-"))
# list.append(x)==> Append x at the last of the list. Similar to a[len(a):] = [x]
fruits.append("JackFruit")
print(fruits)


print("count".center(20,"-"))
# list.count(x) ==> Return the number of times x appears in the list
print(fruits.count("Mango"))


print("Copy".center(20,"-"))
# list.copy() ==> In list, list m = n means both are represnting same location. So, to make an actual copy in memory we use .copy() which return a shallow copy of the list. Similar to a[:]
list1 = fruits
print("Memory Address of list 1 is",id(list1))
print("Memory Address of fruits is",id(fruits))
list1=fruits.copy()
print("Updated Memory Address of list 1 is",id(list1))
print("Memory Address of fruits is",id(fruits))


print("Extend".center(20,"-"))
# list.extend(list2) ==> Extend the list by appending all the items from the list2 at the end of list. Similar to a[len(a):] = list2
italy_places = [
"Colosseum",
"Venice Canals",
"Leaning Tower"
]
fruits.extend(italy_places)
print(fruits)

print("index".center(20,"-"))
# list.index(x,start_index,end_index): Returns the index of the first occurrence of 'x'. Start, end optional. Raises a ValueError if there is no such item.
print(fruits.index("Mango"))

print("Insert".center(20,"-"))
# list.insert(index, element)
italy_places.insert(2,"Delhi")
print(italy_places)


print("Remove".center(20,"-"))
# list.remove(x) ==> Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
fruits.remove("Mango")
print(fruits)   

print("reverse".center(20,"-"))
# list_name.reverse() ==> reverse the element of the list
italy_places.reverse()
print(  italy_places)

print("Pop".center(20,"-"))
# list.pop() ==> removes the last item of the list and returns the last item in the list. It raises an IndexError if the list is empty or the index is outside range.
fruits.pop()
print(fruits)


print("Sort".center(20,"-"))
# list.sort(*, key=None, reverse=False) ==> Sort the items of the list in place. * means all, key and reverse are optional
fruits.sort()
print(fruits)


print("Clear".center(20,"-"))
# list.clear()  ==> Remove all items from the list. Similar to del a[:]
fruits.clear()
print(fruits)