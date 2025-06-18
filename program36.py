# Write a python program to find largest and smallest number from a list of elements.

n = int(input("Enter the number of list from append : "))
l = []
max = 0
for i in range(n):
    user = int(input())
    l.append(user)
min = l[0]
for i in l:
    if i > max:                 # max(l) = find max value of list (method)
        max = i
for i in l:
    if i < min:                 # min(l) = find min value of list (method)
         min =i         
print("max value is : ",max)
print("min value is : ",min)