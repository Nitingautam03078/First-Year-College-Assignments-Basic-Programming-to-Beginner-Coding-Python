# Write a Python program to find the factorial of a number using recursion.

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)
n = int(input("enter the number : "))
print("factorial is ",fact(n))