class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print("run")

class ToyotaCar(Car):
    def run(self):
        print("fast")

class TeslaCar(Car):
    def __init__(self, model="Model S", enable_auto_run=False):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, value):
        self._enable_auto_run = value

    def run(self):
        print("slow")
    def auto_run(self):
        print("auto run")

tesla = TeslaCar("Model S")
tesla.enable_auto_run = True
print(tesla.enable_auto_run)