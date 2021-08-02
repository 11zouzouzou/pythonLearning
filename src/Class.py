# class
# 原生类


print(type('a'))
print(type(1))
print(type(True))
# 创建Car类


class Car:
    speed = 0
    started = False
    # constructor

    def __init__(self, started=False, speed=1) -> None:
        self.speed = speed
        self.started = started

    def start(self):
        self.started = True
        print('car started')

    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print('Vrooom', self.speed)
        else:
            print('you need to start the car first')

    def stop(self):
        self.speed = 0
        print('halting')


# 创建Car类实例
car = Car(False, 2)
print(id(car))
car.increase_speed(10)
car.start()
car.increase_speed(40)
car2 = Car()
print(id(car2))

# inherits,继承


class InheritsCar(Car):
    trunkOpen = False
    # 覆盖重写构造方法

    def __init__(self, started, speed) -> None:
        self.trunkOpen = True
        super().__init__(started=started, speed=speed)

    def changeOpen(self):
        if self.trunkOpen:
            self.trunkOpen = False
        else:
            self.trunkOpen = True
        print(self.trunkOpen)


inheritsCar = InheritsCar()
inheritsCar.changeOpen()
