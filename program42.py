# Write a Python program to find whether an inputted number is perfect or not.

n = int(input("Enter the number : "))
m = n
sum = 0
for i in range(1,n):
    if m%i == 0:
        sum = sum + i
if n == sum:
    print("perfect number is : ",sum)
else:
    print("number is not perfect number : ",sum)
