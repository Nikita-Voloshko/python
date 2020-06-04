import time


class TrafficLight:
    color = ["\033[31m\033[41m", "\033[43m\033[43m", "\033[32m\033[42m"]

    # def __method(self):
    def running(self):
        while True:
            print(TrafficLight.color[0])
            print()
            time.sleep(7)
            print(TrafficLight.color[1])
            print()
            time.sleep(2)
            print(TrafficLight.color[2])
            print()
            time.sleep(7)
            print(TrafficLight.color[1])
            print()
            time.sleep(2)
        return TrafficLight.__color


text = TrafficLight()
color = ['g', 'd', 'f', 'e']
text.running()