class Stationery():
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f'Рисуем текст :{self.title}')
class Pen(Stationery): # Дочерний класс
    def draw(self):
        print(f"Рисуем текст карандашом от компании {self.title}")
class Pencil(Stationery):
    def draw(self):
        print(f"Рисуем теккст ручкой от компании {self.title}")
class Handle(Stationery):
    def draw(self):
        print(f"Рисуем текст маркером от компании {self.title}")
start = Stationery('Comon')
a = Pen('Comon')
a.draw()
b = Pencil('DC')
b.draw()
c = Handle('Marvel')
c.draw()
