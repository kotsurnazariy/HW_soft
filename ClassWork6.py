#1
# class Car():
#     '''what do car now'''
#     def __init__(self, name, make, model):
#         self.name = name
#         self.make = make
#         self.model = model

#     def start(self):
#         print(self.name, 'start move on', self.make)

#     def stop(self):
#         print(self.name, 'Finish mov on', self.make)

# car1 = Car('Nazar', 'Bmw', 'M5')
# car2 = Car('Vitalik', 'Mersedes', 'E')
# car1.start()
# car2.stop()

#2
class Osoba():
    '''What do osoba'''
    def __init__(self, name):
        self.name = name

    def info(self):
        print('Hello my name is', self.name)

class Car():
    def __init__(self, name):
        self.name = name

    def move(self):
        print('Hello my name is', self.name)


name = Osoba('Nazar')
name.info()