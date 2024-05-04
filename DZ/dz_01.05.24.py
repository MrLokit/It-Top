class Student:

    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name, end = '')

    class Laptop:
        def __init__(self):
            self.model = 'HP'
            self.cpu = 'i7'
            self.ram = 16

        def show(self):
            print(f' => {self.model}, {self.cpu}, {self.ram}')

s1 = Student('Roman')
s2 = Student('Vladimir')
l = Student.Laptop()

s1.show()
l.show()
s2.show()
l.show()