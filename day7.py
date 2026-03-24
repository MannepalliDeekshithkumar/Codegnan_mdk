'''STRING ---> String is a collection of characters,which represented by ""or ''
and we can access the using indexing (string can also allow negative indexing)and also slicing.This is also where i could not
able to modified on that particular vari...'''
'''any = 'deekshith'
print(any)'''

'''any = 'deekshith'
print(any[2])'''

'''any = 'deekshith'
print (any[2:8])'''

'''any = 'deekshith'
print(any.replace("deekshith","kanna"))#we can change the name 
print(any)'''

'''any = 'deekshith'
print(any[-6])
print(any)[-20] # Indexerror:string index out of range'''

'''day_1 = "I am deekshith from visakhapatnam,have completed my btech in chennai "
print(f"My name is {day_1[5:14]}")
print(f"i am from {day_1[20:33]}")
print(f"completed my{day_1[51:57]}")
print(f"in{day_1[-9:-1]}")'''


'''name = "deekshith"
print(name[::-1])#to reverse  a string'''

#len()---> len() method is usedto getchar present in the string or find the length
#of the string


'''day_1 = "I am deekshith from visakhapatnam,have completed my btech in chennai "
print(len(day_1))'''

#NOTE: WE CAN CONVERT A STRING INTO INTEGER,IF THE CONTAIN ONLY INTERGER VALUES

some = "123"
num = int (some)
print(type(num))

#if
#some = "123p" we can not convert into integer.

some = "python is good coding language"
print(some.split(" "))


 #              (((( methods of string)))))))
                     
#split---> remove space, and the is in the list[]it will give the separated thing
#in each index
#SYNTAX--->variable_name.split("substring")

'''some = "python is good coding language"
print(some.split("good"))'''

#lower()--->this is used to convert all letter into lower case
#SYNTAX--->variable_name.lower())

'''some = "pytHon IS goOd coding lAnguage"
print(some.lower())'''


#upper()--->this is used to covert all letter into upper case
#SYNTAX--->variable_name.upper(SUBSTRING)

some = "python is good coding language"
print(some.upper())


#REPLACE--->this is used to replace old str with the new string.
#syntax--->variable_name.replace("old string",new string")

'''some = "python is good coding language"
print(some.replace("coding","nrml"))'''

some = "python is good coding language"
if "python" in some:
    print("yes")
else:
    print("no")







































      















































