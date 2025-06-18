# Write a Python program to demonstrate the example of single inheritance.

class A:
    def first(self):
        print("first class is called : ")
class B(A):
    def second(self):
        print("sencod class is called : ")
ob = B()
ob.first()
ob.second()
