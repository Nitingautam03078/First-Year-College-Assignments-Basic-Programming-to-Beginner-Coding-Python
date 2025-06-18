# Write a python program to print first n odd numbers in descending order.

n = int(input("Enter the last number of digit : "))          
l = []                  # creat a empty list. 
l2 = [] 
i = 1
while n>i:              
    l.append(i)         # insert the element of list.
    i = i+2
'''for j in l:
    if j%2 == 1:
        l2.append(j)'''
l.sort(reverse=True)
for a in l:
    print(a)