# Write a python program that counts the number of alphabets and digits, uppercase letters, lowercase latter, spaces and other characters in the entered.

n = input("Enter the string : ")
upper = 0
lower = 0
space = 0
digit = 0 
space = 0
special = 0
for i in n:
    if (i.isupper()):
        upper = upper+1
    elif (i.islower()):
        lower = lower + 1
    elif (i.isdigit()):
        digit = digit + 1
    elif (i.isspace()):
        space = space + 1
    else :
        special = special + 1
print("string upper case is : ",upper)
print("string lower case is : ",lower)
print("string is digit : ",digit)
print("string space is : ",space)
print("string special character is : ",special)