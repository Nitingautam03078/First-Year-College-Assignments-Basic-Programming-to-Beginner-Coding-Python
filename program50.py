# Write a Python program to demonstrate the Iterators.

n = int(input("Entr the numbers of beloces : "))
l = []
print("enter the elements is : ")
for i in range(n):
    ele = int(input())
    l.append(ele)
object = iter(l)
print("\nITERATOR IN A VALUE IS : \n\n")
for i in range(len(l)):
    print(next(object))
