#This is for Arbitary parameter in a function and dict method get()

def arbParam1(*numbers):		#This will make a tuple named numbers
	print(type(numbers),"\n",sum(numbers))
	
def arbParam2(**name):      #This will make a dictionary named name
	print(type(name))
	print("Hi,",name.get("fn","No name provided"),name.get("mn",""),name.get("ln",""))     #get(keyname,value_if_not_found) ==> dict method to access a value by key and if the key has not been any value provided it will return "value_if_not_found", by default it is "None".
	
arbParam1(5,10,15)
arbParam1(5,10,15,20)
arbParam1(5,10,15,20,25)

arbParam2(fn="Ashish",ln="Kumar")
arbParam2(fn="Ashish",mn="Sonuwaiya", ln="Kumar")
arbParam2(fn="Ashish")
arbParam2()  