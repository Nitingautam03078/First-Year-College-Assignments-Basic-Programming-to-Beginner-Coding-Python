# Write a python program to find the greatest common divisor between two numbers.

n = int(input("Enter the first number : "))
n1 = int(input("Enter the second number : "))
gcd = 0
if n > n1:
    a = n
else :
    a = n1
for i in range(1,a+1):
    if n%i or n1%1:
        gcd = i
print("Gcd is : ",gcd)