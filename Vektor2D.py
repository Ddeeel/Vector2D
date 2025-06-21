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