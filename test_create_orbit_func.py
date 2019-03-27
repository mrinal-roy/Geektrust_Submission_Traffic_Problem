import unittest
from function.functraffic import *
from classfiles.classtraffic import *


class TestOrbitCreation(unittest.TestCase):
    '''It tests creation of two orbit objects using function test_defineOrbit which in
    turn tests for function defineOrbit.
    '''

    def setUp(self):
        self.orb_1 = Orbit()
        self.orb_2 = Orbit()
        self.veh_1 = Vehicle()
        self.veh_1.setVehicle('vehicle1', 10, 3, ['WINDY', 'RAINY'])
        self.veh_2 = Vehicle()
        self.veh_2.setVehicle('vehicle2', 15, 3, ['SUNNY'])
        return

    def tearDown(self):
        pass

#    def test_setOrbit(self):
#        self.assertIsInstance(self.orb_1.setOrbit('Orbit1', 25, 12, 10), Orbit)
#        self.assertIsInstance(self.orb_2.setOrbit('Orbit2', 20, 18, 16), Orbit)

    def test_defineOrbit(self):
        self.assertIsInstance(self.orb_1.defineOrbit('Orbit1', 16, "datafiles/orbitdataprob1.txt"), Orbit)
        self.assertIsInstance(self.orb_2.defineOrbit('Orbit2', 14, "datafiles/orbitdataprob1.txt"), Orbit)

if __name__ == '__main__':
    unittest.main()
