import unittest
from weather_logic import *

class TestWeatherData(unittest.TestCase):
        
    def test_get_visibility(self):
        d = {'current' : {'vis_km' : 1000}}
        self.assertEqual(get_visibility(d), 1000)
            
    def test_get_wind_speed(self):
        d = {'current' : {'wind_kph' : 100}}
        self.assertEqual(get_wind_speed(d), 100)
            
    def test_get_day_night(self):
        d = {'current' : {'is_day' : True}}
        self.assertEqual(get_day_night(d), 'день')
            
    def test_get_conditions(self):
        d = {'current' : {'condition' : {'text' : 'Зефирные облака'}}}
        self.assertEqual(get_conditions(d), 'Зефирные облака')
            
    def test_get_feels_like(self):
        d = {'current' : { 'feelslike_c' : 220 } }
        self.assertEqual(get_feels_like(d), 220)
            
    d = {'current' : {'temp_c' : 380}, 'location' : {'localtime' : '2019-04-30 01:44'}}
            
    def test_get_real_temp(self):
        self.assertEqual(get_real_temp(self.d), 380)
        
    def test_get_time(self):
        self.assertEqual(get_time(self.d), '01:44')
            
unittest.main()