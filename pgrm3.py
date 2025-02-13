name = "Ashish"

print("Hello, I am"+name)   # Hello, I amAshish

print("Hello, I am",name)   # Hello, I am Ashish

var = "Mango"

print(var[0:-3])
print(var[0:len(var)-3])  #both are same for every minus value in argument python take it is total length - provided value ==> here it is 5 - 3 = 2 ==> so will show 0,1 positioned values only

print(var[-1:-3])   #5-1=4 to 5-3=2  --> Python can't backtrace like this --> so a blank will be printed

print(var[-3:-1])   #5-3=2 to 5-1=4  --> 2,3 positioned value 