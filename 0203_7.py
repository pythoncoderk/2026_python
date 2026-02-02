class A(object):
    def foo(self):
        print("A")

class B(object):
    def bar(self):
        print("B")

class C(A, B):
    pass

c = C()
c.foo()
c.bar()