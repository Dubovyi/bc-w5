import pytest
from vector.vector import Vector


def test_default_constructor():
    v = Vector()

    assert v.x == 0.0
    assert v.y == 0.0


def test_constructor():
    v = Vector(2, 5)

    assert v.x == 2.0
    assert v.y == 5.0


def test_setters():
    v = Vector(2, 5)

    assert v.x == 2.0
    assert v.y == 5.0

    v.x = 8
    v.y = 9

    assert v.x == 8.0
    assert v.y == 9.0


def test_len():
    assert Vector(2, 5).len() == 5.385164807134504


def test_eq():
    v1, v2 = Vector(), Vector()
    v3 = Vector(1, 2)

    assert v1 == v2
    assert v1 != v3
    assert not v1 != v2
    assert not v1 == v3

    with pytest.raises(TypeError):
        assert v1 == 'asd'

    with pytest.raises(TypeError):
        assert v1 != 'asd'


def test_vector_math():
    v1, v2 = Vector(), Vector()
    v3 = Vector(1, 2)
    v4 = Vector(3, 4)

    assert v1 + v3 == Vector(1, 2)
    assert v4 - v3 == Vector(2, 2)

    v1 += v3
    v5 = v1

    assert v1 == v5

    v2 -= v4
    v6 = v2

    assert v2 == v6


def test_vector_exceptions():
    v1 = Vector()

    with pytest.raises(TypeError):
        assert v1 + 'asd'

    with pytest.raises(TypeError):
        assert v1 - 'asd'

    with pytest.raises(TypeError):
        v1 += 'asd'

    with pytest.raises(TypeError):
        v1 -= 'asd'


def test_vector_to_string():
    assert Vector(2, 5).__str__() == '(2.0, 5.0)'
    assert Vector().__str__() == '(0.0, 0.0)'
