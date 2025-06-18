# Write a Python program to print the Fibonacci series.

n = int(input("Enter the last number of Fibonacci series : "))
a = 0
b = 1
print("Fibonacci series is : ")
for i in range(n):
    c = a +b
    print("\t\t\t",c)
    a = b
    b = c 
