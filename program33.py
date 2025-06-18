# Write a python program to remove an element from list.

n = int(input("Enter the number form input in list : "))
l = []
print("Enter the elements : ")
for i in range(n):
    ele = int(input())
    l.append(ele)
print("List : ",l)
rmve = int(input("Enter the element you want remove : "))
if rmve in l:
    l.remove(rmve)
else: 
    print("That is invalid element ")
    print("Entr the only List element ")
print("your Nem List is : ",l)
