# Write a python program to prints even lenth words in string.

n = input("Enter the string : ")
new_list = []
new_string = n.split()
for i in new_string:
    if len(i) % 2 == 0:
        new_list.append(i)
print(new_list)