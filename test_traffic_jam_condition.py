'''
This unit test tests the routeOptions function against traffic jam condition which is also
a division by zero condition as during traffic jam (blocked route) the user input might be
zero.
'''

import unittest
from function.functraffic import routeOptions
from classfiles.classtraffic import Vehicle, Orbit


class TestRouteJamCondition(unittest.TestCase):
    ''' This test checks if the function routeOption runs successfully during traffic jam
    in any of the two routes, wherein the traffic speed in the respective orbit shall be zero.
    This test thus checks the division by zero in the routeOption function.
    '''

    def setUp(self):
        self.veh_1 = Vehicle()
        self.veh_1.setVehicle('v1', 20, 2, ['SUNNY', 'RAINY'])
        self.veh_2 = Vehicle()
        self.veh_2.setVehicle('v2', 10, 3, ['WINDY', 'RAINY'])
        self.orb_1 = Orbit()
        self.orb_1.setOrbit('Orb1', 25, 12, 1, "pos1", "pos2")
        self.orb_2 = Orbit()
        self.orb_2.setOrbit('Orb2', 20, 18, 0, "pos1", "pos2")

    def tearDown(self):
        pass

    def test_routeoption_traffic_jam(self):
        '''
        This test function tests the function routeOption for a condition with zero speed input from
        the user which is same as the jam or route block condition. This tests the code for division
        by zero.
        '''
        orbits_list = [self.orb_1, self.orb_2]
        set_of_vehicles = [self.veh_1, self.veh_2]
        wetter = 'RAINY'
        result = routeOptions(orbits_list, set_of_vehicles, wetter)
        value_expected = None
        self.assertEqual(result, value_expected, 'Functions routeOptions did not generate \
                                expected value.')


if __name__ == "__main__":
    unittest.main()
