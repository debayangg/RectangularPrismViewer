from prism_calculator import PrismCalculator
import unittest

class TestPrismCalculator(unittest.TestCase):
    def test_surface_area_integer(self):
        """
        Tests surface_area method of the PrismCalculator class with integer values.
        """
        self.assertEqual(PrismCalculator.surface_area(2, 2, 3), 32)
        self.assertNotEqual(PrismCalculator.surface_area(2, 2, 3), 27)
    
    def test_surface_area_float(self):
        """
        Tests surface_area method of the PrismCalculator class with float values.
        """
        self.assertEqual(PrismCalculator.surface_area(2.0,2.0,3.0), 32.0)
        self.assertNotEqual(PrismCalculator.surface_area(2.0,2.0,3.0), 27.0)

    def test_volume_integer(self):
        """
        Tests volume method of the PrismCalculator class with integer values.
        """
        self.assertEqual(PrismCalculator.volume(2, 2, 3), 12)
        self.assertNotEqual(PrismCalculator.volume(2, 2, 3), 13)

    def test_volume_float(self):
        """
        Tests volume method of the PrismCalculator class with float values.
        """
        self.assertEqual(PrismCalculator.volume(2.0, 2.0, 3.0), 12.0)
        self.assertNotEqual(PrismCalculator.volume(2.0, 2.0, 3.0), 13.0)

if __name__ == '__main__':
    unittest.main()