# Write a python program to print all the prime numbers within a geven range.

n = int(input("Enter the range : "))
for i in range(n):
    if i%2 == 1 or i == 2 or i == 1:
        print("number is prime no. : ",i) 
        