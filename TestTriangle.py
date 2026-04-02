import unittest
from Triangle import classifyTriangle

class TestClassifyTriangle(unittest.TestCase):

    # InvalidInput tests
    def test_invalid_negative(self):
        self.assertEqual(classifyTriangle(-1, 2, 3), 'InvalidInput')
    def test_invalid_zero(self):
        self.assertEqual(classifyTriangle(0, 5, 5), 'InvalidInput')
    def test_invalid_over_200(self):
        self.assertEqual(classifyTriangle(201, 5, 5), 'InvalidInput')
    def test_invalid_float(self):
        self.assertEqual(classifyTriangle(1.5, 2, 3), 'InvalidInput')
    def test_invalid_string(self):
        self.assertEqual(classifyTriangle('a', 2, 3), 'InvalidInput')

    # NotATriangle tests
    def test_not_triangle_sum_equal(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle')
    def test_not_triangle_large_side(self):
        self.assertEqual(classifyTriangle(1, 1, 10), 'NotATriangle')
    def test_not_triangle_basic(self):
        self.assertEqual(classifyTriangle(5, 1, 2), 'NotATriangle')

    # Equilateral tests
    def test_equilateral_small(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral')
    def test_equilateral_medium(self):
        self.assertEqual(classifyTriangle(5, 5, 5), 'Equilateral')
    def test_equilateral_large(self):
        self.assertEqual(classifyTriangle(100, 100, 100), 'Equilateral')

    # Right triangle tests
    def test_right_3_4_5(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')
    def test_right_5_12_13(self):
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right')
    def test_right_8_15_17(self):
        self.assertEqual(classifyTriangle(8, 15, 17), 'Right')
    def test_right_order_independent(self):
        self.assertEqual(classifyTriangle(4, 3, 5), 'Right')

    # Isosceles tests
    def test_isosceles_ab(self):
        self.assertEqual(classifyTriangle(5, 5, 3), 'Isoceles')
    def test_isosceles_bc(self):
        self.assertEqual(classifyTriangle(3, 5, 5), 'Isoceles')
    def test_isosceles_ac(self):
        self.assertEqual(classifyTriangle(5, 3, 5), 'Isoceles')

    # Scalene tests
    def test_scalene_basic(self):
        self.assertEqual(classifyTriangle(3, 4, 6), 'Scalene')
    def test_scalene_large(self):
        self.assertEqual(classifyTriangle(7, 10, 12), 'Scalene')
    def test_scalene_another(self):
        self.assertEqual(classifyTriangle(6, 8, 11), 'Scalene')

if __name__ == '__main__':
    unittest.main()