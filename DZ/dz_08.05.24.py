class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def total_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __sub__(self, other):
        difference_seconds = self.total_seconds() - other.total_seconds()
        hours = difference_seconds // 3600
        minutes = (difference_seconds % 3600) // 60
        seconds = difference_seconds % 60
        return Time(hours, minutes, seconds)

    def __mul__(self, other):
        product_seconds = self.total_seconds() * other.total_seconds()
        hours = product_seconds // 3600
        minutes = (product_seconds % 3600) // 60
        seconds = product_seconds % 60
        return Time(hours, minutes, seconds)

    def __floordiv__(self, other):
        quotient_seconds = self.total_seconds() // other.total_seconds()
        hours = quotient_seconds // 3600
        minutes = (quotient_seconds % 3600) // 60
        seconds = quotient_seconds % 60
        return Time(hours, minutes, seconds)

    def __mod__(self, other):
        remainder_seconds = self.total_seconds() % other.total_seconds()
        hours = remainder_seconds // 3600
        minutes = (remainder_seconds % 3600) // 60
        seconds = remainder_seconds % 60
        return Time(hours, minutes, seconds)

    def __isub__(self, other):
        result = self - other
        self.hours, self.minutes, self.seconds = result.hours, result.minutes, result.seconds
        return self

    def __imul__(self, other):
        result = self * other
        self.hours, self.minutes, self.seconds = result.hours, result.minutes, result.seconds
        return self

    def __ifloordiv__(self, other):
        result = self // other
        self.hours, self.minutes, self.seconds = result.hours, result.minutes, result.seconds
        return self

    def __imod__(self, other):
        result = self % other
        self.hours, self.minutes, self.seconds = result.hours, result.minutes, result.seconds
        return self

c1 = Time(0, 10, 0)
c2 = Time(0, 0, 40)

c3 = c1 - c2
c4 = c1 * c2
c5 = c1 // c2
c6 = c1 % c2
c1 -= c2
c1 *= c2
c1 //= c2
c1 %= c2

print("c1:", c1.hours, ":", c1.minutes, ":", c1.seconds)
print("c1 - c2:", c3.hours, ":", c3.minutes, ":", c3.seconds)
print("c1 * c2:", c4.hours, ":", c4.minutes, ":", c4.seconds)
print("c1 // c2:", c5.hours, ":", c5.minutes, ":", c5.seconds)
print("c1 % c2:", c6.hours, ":", c6.minutes, ":", c6.seconds)
