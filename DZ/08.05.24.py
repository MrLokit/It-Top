class Comparison:
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

    def __gt__(self, other):
        return self.c2 > self.c1

    def __ge__(self, other):
        return self.c2 >= self.c1

    def __lt__(self, other):
        return self.c2 < self.c1

    def __le__(self, other):
        return self.c2 <= self.c1

comp = Comparison(1, 3)
print('c2 > c1', comp.c2 > comp.c1)
print('c2 >= c1', comp.c2 >= comp.c1)
print('c2 < c1', comp.c2 < comp.c1)
print('c2 <= c1', comp.c2 <= comp.c1, '\n')

class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.total_seconds = hours * 3600 + minutes * 60 + seconds

    def __sub__(self, other):
        result_seconds = self.total_seconds - other.total_seconds
        hours = result_seconds // 3600
        minutes = (result_seconds % 3600) // 60
        seconds = result_seconds % 60
        return Time(hours, minutes, seconds)

    def __mul__(self, other):
        result_seconds = self.total_seconds * other.total_seconds
        hours = result_seconds // 3600
        minutes = (result_seconds % 3600) // 60
        seconds = result_seconds % 60
        return Time(hours, minutes, seconds)

    def __floordiv__(self, other):
        result_seconds = self.total_seconds // other.total_seconds
        hours = result_seconds // 3600
        minutes = (result_seconds % 3600) // 60
        seconds = result_seconds % 60
        return Time(hours, minutes, seconds)

    def __mod__(self, other):
        result_seconds = self.total_seconds % other.total_seconds
        hours = result_seconds // 3600
        minutes = (result_seconds % 3600) // 60
        seconds = result_seconds % 60
        return Time(hours, minutes, seconds)

    def __isub__(self, other):
        self.total_seconds -= other.total_seconds
        result_seconds = self.total_seconds
        hours = result_seconds // 3600
        minutes = (result_seconds % 3600) // 60
        seconds = result_seconds % 60
        return Time(hours, minutes, seconds)

    def __imul__(self, other):
        self.total_seconds *= other.total_seconds
        result_seconds = self.total_seconds
        hours = result_seconds // 3600
        minutes = (result_seconds % 3600) // 60
        seconds = result_seconds % 60
        return Time(hours, minutes, seconds)

    def __ifloordiv__(self, other):
        self.total_seconds //= other.total_seconds
        result_seconds = self.total_seconds
        hours = result_seconds // 3600
        minutes = (result_seconds % 3600) // 60
        seconds = result_seconds % 60
        return Time(hours, minutes, seconds)

    def __imod__(self, other):
        self.total_seconds %= other.total_seconds
        result_seconds = self.total_seconds
        hours = result_seconds // 3600
        minutes = (result_seconds % 3600) // 60
        seconds = result_seconds % 60
        return Time(hours, minutes, seconds)

    def __str__(self):
        return f"{(self.total_seconds // 3600):02}:{(self.total_seconds % 3600) // 60:02}:{self.total_seconds % 60:02}"

c1 = Time(0, 10, 0)
c2 = Time(0, 3, 20)
print("c1:", c1)
print("c1 - c2:", c1 - c2)

c2 = Time(0, 0, 56)
print("c1 * c2:", c1 * c2)

c2 = Time(0, 3, 20)
print("c1 // c2:", c1 // c2)

c2 = Time(0, 0, 1)
print("c1 % c2:", c1 % c2)

c2 = Time(0, 3, 20)
c1 -= c2
print("c1 -= c2:", c1)

c2 = Time(0, 3, 20)
c1 *= c2
print("c1 *= c2:", c1)

c2 = Time(0, 3, 20)
c1 //= c2
print("c1 //= c2:", c1)

c2 = Time(0, 0, 1)
c1 %= c2
print("c1 %= c2:", c1)



