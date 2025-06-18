# Write a Python program that accepts a string and calculates the number of digits and letter.

n = input("Enter the string : ")
m = list[n]
#print(m.count())
m = n.split()
count1 = 0
count2 = 0
for i in m:
    if i.isalpha() == True:
        count1 = count1 + len(i)
    elif i.isdigit() == True:
        count2 = count2 + len(i)
    else:
        print("That is only count the alphabet and digits : ")
print("number of alphabet in a string is : ",count1)
print("number of digits in a string is : ",count2)