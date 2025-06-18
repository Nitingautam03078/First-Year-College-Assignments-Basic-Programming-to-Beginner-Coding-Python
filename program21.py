# Write a Python program to sort words in alphabetic order.

ch = input("Enter the words : ")
a = ch.lower()
sp = a.split()
sp.sort()
for i in sp:
    print(i)
    