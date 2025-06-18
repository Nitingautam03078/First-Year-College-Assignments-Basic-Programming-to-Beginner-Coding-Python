# Write a python program to find the sum of the series : 1+1/2+1/3+......+1/N.

n = int(input("Enter the last number of the series : "))
sum = 0
for i in range(1,n+1):
    sum = sum + 1/i
print("series is : ",sum)