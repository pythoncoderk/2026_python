class SuperClass:
    spr = "スーパー"

    def super_print(self):
        print("スーパークラスのメソッドです")

class SubClass(SuperClass):
    def sub_print(self):
        print("サブクラスのメソッドです")
    def spr_print(self):
        print(self.spr)

obj = SubClass()
obj.super_print()
obj.sub_print()
obj.spr_print()