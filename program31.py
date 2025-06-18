# Write a python program to reverse a strig without funtion.

s = input("Enter the string : ")
char = ""
print("reverse of string : ")
for i in range(len(s)-1,-1,-1):
    char += s[i]
print(char)
