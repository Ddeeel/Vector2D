class Vector2D:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def __add__(self, other):
        return Vector2D(self._x + other._x, self._y + other._y)
    def __sub__(self, other):
        return Vector2D(self._x - other._x, self._y - other._y)
    def __mul__(self, scalar):
        return Vector2D(self._x * scalar, self._y * scalar)
    def __eq__(self, other):
        return self._x == other._x and self._y == other._y
    def __str__(self):
        return f"({self._x}, {self._y})"
    def lengt(self):
        return (self._x **2 + self._y**2) ** 0.5
    def normalize(self):
        length = self.lengt()
        if length == 0:
            return Vector2D(0, 0)
        return Vector2D(self._x / length, self._y / length)
    def dot_product(self, other):
        return self._x * other._x + self._y * other._y
if __name__ == "__main__":
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)

    print(f"Вектор v1: {v1}")
    print(f"Вектор v2: {v2}")
    print(f"Сума: {v1 + v2}")
    print(f"Різниця: {v1 - v2}")
    print(f"Множення на 2: {v1 * 2}")
    print(f"Довжина v1: {v1.lengt()}")
    print(f"Нормалізований v1: {v1.normalize()}")
    print(f"Скалярний добуток: {v1.dot_product(v2)}")

    v3 = Vector2D(3, 4)
    print(f"v1 == v2: {v1 == v2}")
    print(f"v1 == v3: {v1 == v3}")