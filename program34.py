# Write a python program to sort a number in ascendingr order.
n = int(input("enter the number insert elements : "))
l = []
print("Enter the elements : ")
for i in range(n):
    ele = int(input())
    l.append(ele)
l.sort(reverse=False)
print(l)
