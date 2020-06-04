class Worker():
    name = 'Никита'
    surname = 'Волошко'
    position = 'Директор'
    income = {"wage":22234, "bonus":345}
class Position(Worker):
    def get_full_name(self):
        return Worker.position + ' ' + Worker.surname + ' ' + Worker.name
    def get_total_income(self):
        return Worker.income["wage"] + Worker.income["bonus"]

a = Position()
print(a.get_full_name())
print('Зарплата', a.get_total_income(), 'рублей.')