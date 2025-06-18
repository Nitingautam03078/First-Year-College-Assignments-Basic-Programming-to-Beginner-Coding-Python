# Write a python program to print a odd number within a given range.

n = int(input("Enter the range : "))
for i in range(n):
    if i%2 == 1:
        print("number is :",i)
