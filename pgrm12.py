#f-String in python 
#it is used insted of string.format()

'''Old way using format()'''
myprint = "Hello World! I am {} and I am a {} coder."
name = "Ashish Kumar"
lang = "Python"

print(myprint.format(name, lang))


'''Another way of doing same thing'''
myprint = "Hello World! I am {0} and I am a {1} coder."
name = "Ashish Kumar"
lang = "Python"

print(myprint.format(name, lang))

'''One more way of doing same thing: now the values passed are reversed and the {0} and {1} in string is also interchanged'''
myprint = "Hello World! I am {1} and I am a {0} coder."
name = "Ashish Kumar"
lang = "Python"

print(myprint.format(lang, name))


'''But, in Python we don't love to write more and more, so new method was intorduced using f'''

print(f"Hello World! I am {name} and I am a {lang} coder.") #just passed in the {}

'''Its more powerful if we use it with floats, this can limit the no of decimal values as: .2f --> seems similar to C prgming'''


marks = 8.1151225
print(f"He has got {marks: .3f} in IELTS")

'''What if we want to show this f-string works?? We want to print the whole thing as it is. Without replacing the values of {} with the variable passed. May be to let the new coder know how the whole f-string works'''
'''Answer: Just use {{}} insted of {}.'''

print(f"The fstring works like this --> Hello World! I am {{}} and I am a {{}} coder.")