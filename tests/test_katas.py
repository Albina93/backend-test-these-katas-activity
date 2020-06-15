import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(5, 3), 8)
        self.assertEqual(katas.add(5, 2), 7)

    def test_multiply(self):
        self.assertEqual(katas.multiply(5, 3), 15)
        self.assertEqual(katas.multiply(5, 2), 10)

    def test_power(self):
        self.assertEqual(katas.power(5, 3), 125)
        self.assertEqual(katas.power(5, 2), 25)

    def test_factorial(self):
        self.assertEqual(katas.factorial(5), 120)
        self.assertEqual(katas.factorial(4), 24)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(5), 3)
        self.assertEqual(katas.fibonacci(4), 2)


if __name__ == '__main__':
    unittest.main()
