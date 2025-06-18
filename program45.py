# Write a Python program to create a class which perform basic calculation operations.

class Basic:
    def Operat(self,n,m):
        print("sum of tow numbers is : ",n + m)
        print("subtect is two number is : ",n - m)
        print('multiful of two numbers is : ',n * m)
        print("dived of two numbers is : ",n/m)
obj = Basic()
obj.Operat(10,5)