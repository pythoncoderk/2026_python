class Circle:

    pi = 3.14

    def cl(self, r):
        return r * 2 * Circle.pi

    def ca(self, r):
        return r * r * Circle.pi


print(Circle().cl(1))

