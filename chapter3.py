#string & type conversion
# a="h"
# print (ord(a)) # 104 knows as unicode value of character

#indexing in string

#POSTIVE INDEXING
# a="college"
# print (a[4]) # prints the character at index 4 which is 'e'

#NEGATIVE INDEXING
# a="elder"
# print(a[-3]) # prints the character at index -3 which is 'd'
# print(a[0],a[-5]) # prints the character at index 0 which is 'e' and at index -5 which is 'e'

#string slicing
# a="college"
# print(a[2:5:2]) #output is le prints the character at index 2 to 5 with a step of 2 which is 'l' and 'e'
# #print(a[start:stop:step]) at stop add +1 in the index value to get the desired output
# #start is inclusive and stop is exclusive and step is the number of characters to skip 
# print (a[0:7:2]) #output clee
# #smart way
# print (a[::2]) #still output is clee as it takes the default values of start and stop which is 0 and length of the string respectively

# #print how are you individually using slicing
# b="hello how are you"
# print (b[6:9]) #output is how

# print (b[10:13]) #print are
# print (b[14:17])#print you

#type conversion
# a= "10"
# b=int(a)
# print (type(a)) #output is string
# print ((b)) #now the output is 10 as integer
# print (type(b)) #output is integer

#python is a interpreted language it runs line by line and changes the value
# a=10
# a=50
# a=60
# a=12.56
# print (a) #output is 12.56 as it is the last value assigned to a

# a="12"
# a=int(a)
# print(type(a)) #output is integer

# #what if we want to convert a float to integer
# a=12.56
# a=int(a)
# print(type(a)) #output is integer but the value is 12 as it removes the decimal
# print(a) #output is 12

#but what if converyting a float to int
# a="12.56"
# a=int(int(a))
# print(a) #gets the error

#you can convert string if it holds valid integers
#you can convert float values to int

# a="12.5"
# a=float(a)
# print(a) #output is 12.5 as float
# print(type(a)) #output is float

# a="12"
# a=float(a)
# print(a) #output is 12.0 as float adds .0 to the integer value

# a=143
# a=float(a)
# print(a) #output is 143.0 as float adds .0 to the integer value

# a=50
# b=86
# c=86+96j
# d=True
# a=str(a)
# b=str(b)
# c=str(c)
# d=str(d)
# print(a)
# print(b)
# print(c)  
# print(d)

#bool
#8 false values in python rest are true
# None, False, 0, 0.0,"", [], {}, set()

# a=None 
# print(bool(a)) #output is false

# a=12
# b=0
# c=""
# d=["hello"]
# print(bool(a)) #output is true
# print(bool(b)) #output is false
# print(bool(c)) #output is false
# print(bool(d)) #output is true as it has a value in it

#everything we studied is implict manually changing the data
#now we will see explicit type conversion

a=12
print(a/2) #output is 6.0 as it converts the integer to float automatically