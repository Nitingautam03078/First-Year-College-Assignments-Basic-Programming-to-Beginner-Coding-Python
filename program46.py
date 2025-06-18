# Write a Python program to demonstrate the constructor.
class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def dis(self):
        print("sum is two numbers : ",self.a + self.b)
ob = A(4,8)
ob.dis()