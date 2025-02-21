s1 = "this is a * String is a is"
s2 = "test1"
s3 = "PYTHON"
s4 = "123"
s5 = "Thank you Python\nIts so easy to code."

print("\n******************\n")
print("s1: ", s1, "\ns2: ", s2, "\ns3: ",s3, "\ns4: ",s4,"\ns5: ",s5, "\n******************\n") 

#String Methods implementation

print('s1.capitalize()', s1.capitalize())  #first character is converted to upper case, and the rest are converted to lower case

print('\ns1.casefold()', s1.casefold())  #This method is similar to the lower() method, but the casefold() method is stronger, more aggressive

''' this will make a string of length 20 of which s2 will be in centre, and both side will be filled by * => though only one length args is necessary, default value is " " for side spaces '''
print('\ns2.center(\'*\')', s2.center(20, "*"))

print('\ns1.count(\'is\') : returns the number of times a specified value appears in the string.', s1.count('is'))   #count(value_to_find, start_index, end_index) ==> Default: start 0, end last-index


print('\ns1.endswith(\'is\')', s1.endswith('is'))  #check if the string ends with value given 
print('\ns1.find(\'is\')', s1.find('is'))  #finds the first occurrence of the specified value, else return -1
print('\ns1.index(\'is\')', s1.index('is'))    #same as find() but return exception if not found.
print('\ns2.isalnum()', s2.isalnum())  # returns True if all the characters are alphanumeric
print('\ns1.isalpha()', s1.isalpha())    #returns True if all the characters are alphabet 
print('\ns4.isdecimal()', s4.isdecimal())    #returns True if all the characters are decimals 
print('\ns4.isdigit()', s4.isdigit())    
print('\ns3.isupper()', s3.isupper(), "\nislower()", s2.islower())
print('\ns4.lstrip()', s4.lstrip(), "\nrstrip()", s4.rstrip())    
print('\ns4.isdecimal()', s4.isdecimal())

print('\ns1.swapcase()', s1.swapcase())

print('\ns1.lower()',s1.lower(), '\ns2.upper()', s2.upper()) #return all in lower/upper case
print('\ns1.split(\'*\')', s1.split("*"))    #split using given seperator, default: whitespace

print('\ns5.splitlines()', s5.splitlines())  

print('\ns5.title()', s5.title())  