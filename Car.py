from random import randint
class Car():
    speed = 0
    color = ''
    name= ''
    is_police = False
    def show_speed(self, speed):
         Car.speed = speed
         if (Car.speed > 60):
             print("Выяснилось , что машина двигалась слишком быстро. Ее оштрафовали.")
         elif(Car.speed > 40):
              print("Машина двигалась слишком быстро. Ее оштрафовали.")
         else:
            print("Машина двигается с приемлемой скоростью.")
    def go(self, name, color):
        Car.color = color
        Car.name = name
        print(Car.name)
        print(f"Цвет машины: {color}")
        print('Машина завилась.')
    def stop(self):
        print("Машина остановилась")
    def turn(self):
        i = 0
        while (i < 5):
            car_turn = int(randint(0,1))
            if (car_turn == 0):
                print('Машина повернула направо.')
            else:
                print('Машина повернула налево.')
            i +=1

class TownCar(Car):
    def __init__(self, speed, name, color):
        super().go(name, color)
        print()
        super().turn()
        print()
        print("Скорость машины", speed, "км\ч")
        super().show_speed(speed)
        super().stop()
class SportCar(Car):
    def __init__(self, speed, name, color):
         super().go(name, color)
         print()
         super().turn()
         print()
         print("Скорость машины", speed, "км\ч")
         super().show_speed(speed)
         super().stop()
class WorkCar(Car):
    def __init__(self, speed, name, color):
         super().go(name, color)
         print()
         super().turn()
         print()
         print("Скорость машины", speed, "км\ч")
         super().show_speed(speed)
         super().stop()
class PoliceCar(Car):
    def __init__(self, speed, name, color):
         print("Полецейская машина")
         super().go(name, color)
         print()
         super().turn()
         print()
         print("Скорость машины", speed, "км\ч")
         super().show_speed(speed)
         super().stop()

user_car = TownCar(70, "Town car", "Зеленый")
# user_car = WorkCar(30, "Work car")

# ---------------------------------------------Вариант-----------------------------------------------
# from random import randint
# class Car():
#     def show_speed(self):
#          if (TownCar.speed > 60):
#              print("Выяснилось , что машина двигалась слишком быстро. Ее оштрафовали.")
#          elif(WorkCar.speed > 40):
#               print("Машина двигалась слишком быстро. Ее оштрафовали.")
#          else:
#             print("Машина двигается с приемлемой скоростью.")
#     def go(self, name):
#         self.name = name
#         print(self.name)
#         print('Машина завилась.')
#     def stop(self):
#         print("Машина остановилась")
#     def turn(self):
#         i = 0
#         while (i < 5):
#             car_turn = int(randint(0,1))
#             if (car_turn == 0):
#                 print('Машина повернула направо.')
#             else:
#                 print('Машина повернула налево.')
#             i +=1
#
# class TownCar(Car):
#     name = "Town Car"
#     speed = 70
# class SportCar(Car):
#     name = "Sport Car"
#     speed = 70
# class WorkCar(Car):
#     name = "Work Car"
#     speed = 70
# class PoliceCar(Car):
#     name = "Police Car"
#     speed = 70
# user_car = TownCar()
# user_car.go("Town Car")
# user_car.turn()
# user_car.show_speed()
# user_car.stop()
