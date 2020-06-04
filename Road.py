class Road():
    def __init__(length, width):
        return float(length) * float(width) * 25 * 5 / 1000


a = Road
print(a.__init__(input('Введите длину '), input('Введите ширину ')), "тонн.")
