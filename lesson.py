class Car(object):
    def run(self):
        print('run')

class ToyotaCar(Car):
    pass

class TeslaCar(Car):
    def auto_run(self):
        print('auto_run')

car = Car()
car.run()

print("##############")
toyotacar = ToyotaCar()
toyotacar.run()
print("##############")
tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()