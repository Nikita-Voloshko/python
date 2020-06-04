class Road():
    length = 0
    width = 0
    def __init__(self, length, width):
        Road.length = length
        Road.width = width
    def sum(self):
        return float(Road.length) * float(Road.width) * 25 * 5 / 1000


a = Road
a.__init__(0, input('Введите длину '), input('Введите ширину '))
print(a.sum(0), "тонн.")
