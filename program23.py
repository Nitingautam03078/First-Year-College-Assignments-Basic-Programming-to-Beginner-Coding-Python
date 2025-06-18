# Write a Python program to find the sum of digits in a number.

n = int(input("Enter the digits : "))
sum = 0 
while n>0:
    f = n%10
    sum = sum + f
    n = n//10
print("Sum is : ",sum)