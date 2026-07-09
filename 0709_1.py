class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self, monster):
        print(f"{self.name}の攻撃！")
        monster.damage(20)


class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def damage(self, power):
        self.hp -= power
        print(f"{self.name}は{power}ダメージ受けた")
        print(f"残りHP：{self.hp}")


hero = Hero("勇者", 100)
monster = Monster("スライム", 50)

hero.attack(monster)