import unittest
from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter

class TestShapes(unittest.TestCase):

    # Circle tests
    def test_circle_area(self):
        with self.subTest("Circle area for radius 1"):
            self.assertAlmostEqual(circle_area(1), 3.1416, places=4)
        with self.subTest("Circle area for radius 0"):
            self.assertEqual(circle_area(0), 0)
    
    def test_circle_perimeter(self):
        with self.subTest("Circle perimeter for radius 1"):
            self.assertAlmostEqual(circle_perimeter(1), 6.2832, places=4)
        with self.subTest("Circle perimeter for radius 0"):
            self.assertEqual(circle_perimeter(0), 0)
    
    # Rectangle tests
    def test_rectangle_area(self):
        with self.subTest("Rectangle area for sides 2 and 3"):
            self.assertEqual(rectangle_area(2, 3), 6)
        with self.subTest("Rectangle area for sides 0 and 5"):
            self.assertEqual(rectangle_area(0, 5), 0)

    def test_rectangle_perimeter(self):
        with self.subTest("Rectangle perimeter for sides 2 and 3"):
            self.assertEqual(rectangle_perimeter(2, 3), 10)
        with self.subTest("Rectangle perimeter for sides 0 and 5"):
            self.assertEqual(rectangle_perimeter(0, 5), 10)
    
    # Square tests
    def test_square_area(self):
        with self.subTest("Square area for side 4"):
            self.assertEqual(square_area(4), 16)
        with self.subTest("Square area for side 0"):
            self.assertEqual(square_area(0), 0)

    def test_square_perimeter(self):
        with self.subTest("Square perimeter for side 4"):
            self.assertEqual(square_perimeter(4), 16)
        with self.subTest("Square perimeter for side 0"):
            self.assertEqual(square_perimeter(0), 0)
    
    # Triangle tests
    def test_triangle_area(self):
        with self.subTest("Triangle area for base 4 and height 5"):
            self.assertEqual(triangle_area(4, 5), 10)
        with self.subTest("Triangle area for base 0 and height 5"):
            self.assertEqual(triangle_area(0, 5), 0)

    def test_triangle_perimeter(self):
        with self.subTest("Triangle perimeter for sides 3, 4, and 5"):
            self.assertEqual(triangle_perimeter(3, 4, 5), 12)
        with self.subTest("Triangle perimeter for sides 0, 0, and 0"):
            self.assertEqual(triangle_perimeter(0, 0, 0), 0)

if __name__ == "__main__":
    unittest.main()
