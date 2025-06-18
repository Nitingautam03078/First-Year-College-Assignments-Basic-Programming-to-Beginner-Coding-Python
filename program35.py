# Write a python program to sort the word in alphabetical order.

n = input("Enter the string : ")
s = list(n)
s.sort(reverse= False)
for i in s:
    print(i)