class A:
    x = 10
    def __init__(self):
        self.y = 20
    def show(self):
        return self.x + self.y

class B(A):
    x = 100
    def __init__(self):
        super().__init__()
        self.x = 1000

obj = B()
print(obj.x)
print(obj.y)
print(B.x)
print(A.x)
print(obj.show())
print(obj.__dict__)