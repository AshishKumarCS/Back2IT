# In this, I am working on Function:

def checkGreater(a,b): 
    print (f"In {a} & {b}: ", end="")
    if a==b:
        print("Both are equal")
    elif a>b:
        print("a is greater")
    else:
        print("b is greater")

def checkEven(a=24, b=8):	#Default Value passed 
    print (f"For values {a} & {b}: ", end="")
    print("Both are Even" if a%2==0 and b%2 ==0 else "Either one or both are Odd")
	
def mandatoryArgs(a,b=10):
    print("Here a is mandatory parameter as it has no default value.\nHowever, we can skip b as it has default value 10")
    print("a:",a,"b:",b)
    
    
#testing
checkGreater(10,5)
checkGreater(11,15)

checkEven()
checkEven(10,11)
checkEven(b=10,a=2)     #Here as the b=sth and a=sth is given so no need to maintain the sequence as defined in the function definition

mandatoryArgs(10)
mandatoryArgs(10,100)
mandatoryArgs()     #will throw error
