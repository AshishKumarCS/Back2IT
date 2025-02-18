#DocString "methodname.__doc__"

def square(i):
	'''This takes an int and returns it square.'''  #This must be placed just after def ...() line
	print(i*i)

square(10)
print(square.__doc__)

#********************************************************************
import this #Zen of Python - A beautiful poem full of insights of clean coding