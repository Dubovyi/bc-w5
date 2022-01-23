import unittest
from vector import Vector


class TestVector(unittest.TestCase):
    def test_constructor(self):
        p = Vector()
        self.assertEqual(p.x, 0.0)
        self.assertEqual(p.y, 0.0)

        p = Vector(2, 19)
        self.assertEqual(p.x, 2.0)
        self.assertEqual(p.y, 19.0)

        with self.assertRaises(TypeError):
            Vector(Vector(), 0.0)

        with self.assertRaises(ValueError):
            Vector('abc', 0.0)

    def test_operators(self):
        v1, v2 = Vector(), Vector()
        v3 = Vector(1, 7)
        v4 = Vector(2, 5)

        self.assertTrue(v1 == v2)
        self.assertFalse(v1 != v2)
        self.assertTrue(v1 != v3)
        self.assertFalse(v1 == v3)

        self.assertEqual(v1 + v3, Vector(1, 7))
        self.assertEqual(v4 + v3, Vector(3, 12))

        self.assertEqual(v3 - v4, Vector(-1, 2))
        self.assertEqual(v1 - v3, Vector(-1, -7))


if __name__ == '__main__':
    unittest.main()
