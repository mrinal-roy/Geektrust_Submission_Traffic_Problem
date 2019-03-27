'''This unit test module tests the functions crater_factor, minTime functions.
'''
import unittest
from function import functraffic

class TestFunctraffic(unittest.TestCase):
    '''This unit test class constructs the test cases of the the functions crater_factor,
minTime functions.'''

    def test_crater_result_one(self):
        '''This test checks crater_factor function to return the correct expected
        value with sunny weather condition as input from the user.
        '''
        weather = 'SUNNY'
        self.assertEqual(functraffic.crater_factor(weather), 0.9)

    def test_crater_result_two(self):
        '''This test checks crater_factor function to return the correct expected
        value with rainy weather condition as input from the user.
        '''
        weather = 'RAINY'
        self.assertEqual(functraffic.crater_factor(weather), 1.2)

    def test_crater_result_three(self):
        '''This test checks crater_factor function to return the correct expected
        value with any weather condition other than sunny or rainy as input from the user.
        '''
        weather = 'Any Thing Else'
        self.assertEqual(functraffic.crater_factor(weather), 1)

    def test_min_time(self):
        '''This test checks the function minTime to generate the orbit option with the least
        travel time.
        '''
        routes = [('orb1', 'vehicle1', 17.32), ('orb4', 'vehicle4', 12.32),
                  ('orb2', 'vehicle2', 20), ('orb3', 'vehicle3', 15)]
        self.assertEqual(functraffic.minTime(routes), ('orb4', 'vehicle4', 12.32))

    def test_min_time_negative(self):
        '''This test checks the function minTime to generate the orbit option with the least
        travel time. It tests minTime against a negative time value and returns successful
        if the minimum time value matches with the expected minimum time value. This condition
        might happen due to user input wrongly given as negative.
        '''
        routes = [('orb1', 'vehicle1', -17.32), ('orb4', 'vehicle4', 12.32),
                  ('orb2', 'vehicle2', 20), ('orb3', 'vehicle3', 15)]
        self.assertEqual(functraffic.minTime(routes), ('orb1', 'vehicle1', -17.32))


if __name__ == "__main__":
    unittest.main()
