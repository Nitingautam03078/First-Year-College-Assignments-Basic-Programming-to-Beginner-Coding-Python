# Write a Python program to check the number is Armstrong or not.

n = int(input("Enter the number : "))
n1 = n
sum = 0
while n>0:
    t = n%10
    sum = sum + t**3
    n = n//10
if sum == n1:
    print("number is Armstrog no. : ",sum)
else : 
    print("Number is not Armstrog no. : ",sum)