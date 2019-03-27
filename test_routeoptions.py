''' This test checks if the function routeOption runs successfully. It checks for 2 vehicle
types and 2 orbits. Also it checks for RAINY weather condition. It generates the set of orbit
or route options using the function routeOptions and checks against the expected value.'''

import unittest
from function.functraffic import routeOptions
from classfiles.classtraffic import Vehicle
from classfiles.classtraffic import Orbit

class TestRouteOptions(unittest.TestCase):
    ''' It sets up 2 vehicle objects and 2 orbit objects to test with.
    '''

    def setUp(self):
        self.veh_1 = Vehicle()
        self.veh_1.setVehicle('v1', 20, 2, ['SUNNY', 'RAINY'])
        self.veh_2 = Vehicle()
        self.veh_2.setVehicle('v2', 10, 3, ['WINDY', 'RAINY'])
        self.orb_1 = Orbit()
        self.orb_1.setOrbit('Orb1', 25, 12, 10, "pos1", "pos2")
        self.orb_2 = Orbit()
        self.orb_2.setOrbit('Orb2', 20, 18, 16, "pos1", "pos2")

    def tearDown(self):
        pass

    def test_route_options(self):
        ''' This test checks if the function routeOption runs successfully. It checks for 2 vehicle
    types and 2 orbits. It takes RAINY weather condition as input. It generates the set of orbit
    options using the function routeOptions and checks against the expected value. '''
        orbits_list = [self.orb_1, self.orb_2]
        set_of_vehicles = [self.veh_1, self.veh_2]
        wetter = 'RAINY'
        result = routeOptions(orbits_list, set_of_vehicles, wetter)
        value_expected = [('v1', 'Orb1', 2.98), ('v2', 'Orb1', 3.22),
                          ('v1', 'Orb2', 1.97), ('v2', 'Orb2', 3.08)]
        self.assertEqual(result, value_expected, 'Functions routeOptions did not generate \
                                                        expected value.')

if __name__ == "__main__":
    unittest.main()
