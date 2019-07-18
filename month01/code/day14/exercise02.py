class Vector1:
    def __init__(self,x):
        self.x = x

    def __str__(self):
        return "%d"%int(self.x)

    def __add__(self, other):
        return Vector1(self.x + other)

    def __radd__(self, other):
        return Vector1(self.x + other)

    def __sub__(self, other):
        return Vector1(self.x - other)

    def __rsub__(self, other):
        return Vector1(self.x - other)

    def __mul__(self, other):
        return Vector1(self.x * other)

    def __rmul__(self, other):
        return Vector1(self.x * other)

    def __truediv__(self, other):
        return Vector1(self.x / other)

    def __rtruediv__(self, other):
        return Vector1(self.x / other)

v1 = Vector1(5)
print(v1+3)
print(v1-3)
print(v1*3)
print(v1/3)

print(3+v1)
print(3-v1)
print(3*v1)
print(3/v1)