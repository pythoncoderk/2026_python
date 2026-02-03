class A(object):
    def hello(self):
        print("A")

class B(object):
    def hello(self):
        print("B")

class C(B, A):
    pass

C().hello()