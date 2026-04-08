class Animal:
    kingdom = "Animalia"   # クラス変数

    def __init__(self, name):
        self.name = name   # インスタンス変数
        self.energy = 100  # インスタンス変数

    def speak(self):
        return f"{self.name} makes a sound"

    def info(self):
        return f"name={self.name}, energy={self.energy}, kingdom={self.kingdom}"


class Dog(Animal):
    species = "Dog"   # クラス変数

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed   # インスタンス変数

    def speak(self):
        return f"{self.name} barks"

    @classmethod
    def class_info(cls):
        return f"species={cls.species}, kingdom={cls.kingdom}"


class GuideDog(Dog):
    species = "GuideDog"   # クラス変数を上書き

    def __init__(self, name, breed, owner):
        super().__init__(name, breed)
        self.owner = owner   # インスタンス変数

    def info(self):
        parent_info = super().info()
        return f"{parent_info}, breed={self.breed}, owner={self.owner}"


dog1 = Dog("Pochi", "Shiba")
dog2 = GuideDog("Hachi", "Labrador", "Tanaka")

print(dog1.speak())
print(dog2.speak())
print(dog1.info())
print(dog2.info())
print(Dog.class_info())
print(GuideDog.class_info())

print("dog1.__dict__ =", dog1.__dict__)
print("dog2.__dict__ =", dog2.__dict__)
print("Animal.__dict__.keys() =", Animal.__dict__.keys())
print("Dog.__dict__.keys() =", Dog.__dict__.keys())
print("GuideDog.__dict__.keys() =", GuideDog.__dict__.keys())

print(dog2.species)