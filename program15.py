# Writer a program to find sum of series 1-2+3-4+5.......+N.

n = int(input("enter the last number of series : "))
sum = 0
for i in range(1,n+1):
    if i %2 == 0:
        sum += i
    else :
        sum -= i
print("series is : ",sum)
