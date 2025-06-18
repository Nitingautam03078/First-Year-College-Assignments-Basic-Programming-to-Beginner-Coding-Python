# Write a Python program to display the multiplication table.

n = int(input("Enter the last number of table you want : "))
for j in range(2,n):
    for i in range(1,11):
        print(j ,"X", i ," = ", j*i)
    print("\t")
    