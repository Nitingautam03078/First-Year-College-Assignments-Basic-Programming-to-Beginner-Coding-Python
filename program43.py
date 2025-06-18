# Write a Python program to find sum of square of first n natural numbers using function.

def funct(n):
    sum1 = 0
    for i in range(n+1):
        sum1 = sum1 + i ** 2
    print("sum of square of first n natural number : ",sum1)
n = int(input("Enter the range of nature numbers : "))
funct(n)
