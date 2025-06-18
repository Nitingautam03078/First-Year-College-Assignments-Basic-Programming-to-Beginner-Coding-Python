# Write a Python program to demonstrate the Binary Operator Overloading.

class A:
    def __init__(self,a):
        self.a = a
    def __add__(self,other):
        print("first no is : ",self.a)
        print("second no is : ",other.a)
        print('sum of two object is : ')
        return((self.a + other.a))
ob = A(10)
ob1 = A(20)
ob2 = ob + ob1
print(ob2)