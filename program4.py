# Write a python program that accept marks in 5  subjects and display its percentage.  
print(" -: entr the number any one subject out of 100 marks :-")
s1 = int(input("enter the first subect number : "))
s2 = int(input("enter the second subect number : "))
s3 = int(input("enter the thrid subject number : "))
s4 = int(input("enter the fourth subject number : "))
s5 = int(input("enter the five subject number : "))
total = s1 + s2 + s3 + s4 +s5
percent = total/500*100
t = [ s1 , s2 , s3 , s4 ,s5]
a = 0
for i in range(5):
    a = a+1
    if t[i] >= 33:
        print("pass subject ",a)
    else: 
        print("fail subject ",a)

print("Total marks = ",total)
print("percentage is : ",percent)

if percent >= 80:
    print("excllent percent : ",percent)
elif percent >= 60 and percent < 80 :
    print("first division : ",percent)
elif percent >= 50 and percent < 60:
    print("secont divison : ",percent)
elif percent >= 40 and percent < 50: 
    print("third division : ",percent)
else :
    print("you are fail : ",percent)




