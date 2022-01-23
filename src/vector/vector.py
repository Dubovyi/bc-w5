from __future__ import annotations
from math import hypot


class Vector:
    __slots__ = ('_x', '_y')

    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @x.setter
    def x(self, val: float) -> None:
        self._x = val

    @y.setter
    def y(self, val: float) -> None:
        self._y = val

    def len(self) -> float:
        return hypot(self.x, self.y)

    def __eq__(self, other: Vector) -> bool:
        if not isinstance(other, self.__class__):
            raise TypeError()
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: Vector) -> bool:
        return not self == other

    def __iadd__(self, other: Vector) -> None:
        if not isinstance(other, self.__class__):
            raise TypeError()
        self.x += other.x
        self.y += other.y

    def __isub__(self, other: Vector) -> None:
        if not isinstance(other, self.__class__):
            raise TypeError()
        self.x -= other.x
        self.y -= other.y

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, self.__class__):
            raise TypeError()
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, self.__class__):
            raise TypeError()
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'


if __name__ == '__main__':  # pragma: no cover
    vector = Vector(10, 15)
    vector2 = Vector(2, 5)
    vector3 = Vector()

    vector3 += vector

    print(vector)
    print(vector2)

    print(vector + vector2)

    print(vector2.len())
