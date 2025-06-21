class Vector2D:
    def init(self, x, y):
        self._x = x
        self._y = y
    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    def sub(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    def mul(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)
    def eq(self, other):
        return self.x == other.x and self.y == other.y
    def str(self):
        return f"({self.x}, {self.y})"

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def normalize(self):
        length = self.length()
        if length == 0:
            return Vector2D(0, 0)
        return Vector2D(self.x / length, self.y / length)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y