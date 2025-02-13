import time

print("Testing strftime(), need typecasting".center(50,'*'))
timestamp = int(time.strftime('%H'))   #it can be time.strftime('%h:%m:%s') also
if(timestamp > 1):
	print("GM")
elif(timestamp<=12 and timestamp > 17):
	print("GA")
elif(timestamp >=17 and timestamp < 20):
	print("GE")
else:
	print("GN")


print("Testing localtime() with . and index".center(50,'*'))
print("time.localtime().tm_hour :",time.localtime().tm_hour)  #print hour
print("time.localtime()[3] :",time.localtime()[3])       #hour can be accessed by indexing also
print("".center(50,'*'))


print("If-else using timelocal().values dirctly, No typecasting needed")
this_hour = time.localtime().tm_hour

if(this_hour > 1):
	print("GM")
elif(this_hour<=12 and this_hour > 17):
	print("GA")
elif(this_hour >=17 and this_hour < 20):
	print("GE")
else:
	print("GN")

print("So, with localtime we get int values in time, whereas with strftime we get string")