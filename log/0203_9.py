class A:
    def hello(self):
        print("A")

class B(A):
    def hello(self):
        super().hello()
        print("B")

class C(B):
    def hello(self):
        super().hello()
        print("C")

C().hello()
