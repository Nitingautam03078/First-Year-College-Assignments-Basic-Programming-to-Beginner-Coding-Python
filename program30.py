# Write a python program to print the sum of all elements in an array.

n = int(input("Enter the how many number you want is : "))
array = []
for i in range(n):
    m = int(input("Enter the "+str(i+1)+" value : "))
    array.append(m)
s = sum(array)
print("array is : ",array)
print("sum of array is : ",s)