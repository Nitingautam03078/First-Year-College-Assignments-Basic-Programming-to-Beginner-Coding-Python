# Write a python program to check if the string is paliandrome or not using loop.

n = input("Enter the string : ")
n1 = ""           # To creat empty string 
for i in n:       # string revese method
    n1 = i + n1   # string insert a elements like a queue data member  "first in last out" 
if n == n1:
    print("\n\t-:String is a paliandrome :- ")          # if any string and its revese are equal then it is called palindrome 
    print("\n\t your string is : ",n)
    print("\n\t your string after revese is : ",n1,"\n")
else:
    print("\n\t-:string is not palandrome : ")
    print("\n\t your string is : ",n)
    print("\n\t your string after revese is : ",n1,"\n")
