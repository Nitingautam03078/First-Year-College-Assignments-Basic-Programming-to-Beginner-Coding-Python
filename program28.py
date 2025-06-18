# Write a python program to find the sum of Natural numbers.

n = int(input("Enter the last number you want : "))
sum = 0
for i in range(1,n+1):
    sum += i
print("sum of Natrual number is : ",sum)