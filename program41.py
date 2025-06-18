# Write a python program to print the longest word in a list of words.

n = input("Enter the string : ")
m = n.split()
m_new = m[0]
for i in m:
    if i < m_new:
        m_new = i
print("longest word is : ",m_new)