#List implementation

fruits = [
    "Apple", "Banana", "Mango", "Orange", "Grapes",
    "Pineapple", "Strawberry", "Watermelon", "Papaya", "Guava",
    "Kiwi", "Pomegranate", "Cherry", "Peach", "Plum",
    "Lychee", "Coconut", "Blueberry", "Raspberry", "Dragon Fruit"
]

print("Every 3rd value: ",fruits[::3])

#Very Important: for the below command it must be included inside [ ]
print("Only those fruits which has \'r\' in it", [fruit for fruit in fruits if "r" in fruit])

print("Only those whose name length >5", [fruit for fruit in fruits if len(fruit)>5])