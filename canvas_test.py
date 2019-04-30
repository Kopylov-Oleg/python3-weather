import unittest
from canvas import *

if __name__ == '__main__':
     
    class TestWeatherData(unittest.TestCase):
        def test_add_colors(self):
            self.assertEqual(Color([1,2,2]) + Color([2,1,1]), Color([3,3,3]))
            
        def test_add_color_int(self):
            self.assertEqual(Color([1,2,2]) + 1, Color([2,3,3]))
            
        def test_div_colors(self):
            self.assertEqual(Color([2,2,2])//2, Color([1,1,1]))
            
        def test_mul_colors(self):
            self.assertEqual(Color([2,1,1])*3, Color([6,3,3]))
            
        def test_clamp_color(self):
            self.assertEqual(Color([-1, 0, 266]).clamp(), Color([0, 0, 255]))
            self.assertEqual(Color([255, 256, 266]).clamp(), Color([255, 255, 255]))
            
        def test_to_hex(self):
            self.assertEqual(Color([0,0,0]).to_hex(), '#000000')
            self.assertEqual(Color([255,255,255]).to_hex(), '#FFFFFF')
            
    unittest.main()
