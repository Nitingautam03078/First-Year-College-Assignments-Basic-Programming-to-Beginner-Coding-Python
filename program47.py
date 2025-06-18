# Write a Python program to demonstrate the Function Overloading.

class A:
    def sum(self):
        print("\n  welcom ")
    def sum(self,x = ""):
        print("Welcom ",x)
    def sum(self,x= "",y = ""):
        '''print("\n thrid function is called : ",x,y)'''
        print("Welcom ",x,y)
ob = A()
ob.sum()
ob.sum('nitin')
ob.sum('nitin','gautam')   
                    