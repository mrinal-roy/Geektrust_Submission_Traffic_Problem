class Vehicle():
    """
    This class creates Vehicle object with only instantiation of the object without
    any attribute initialization.
    """
    def __init__(self):
        pass

    def setVehicle(self, veh_type, max_speed, cross_crater, can_travel):
        '''
        This object function initializes the attributes of an Vehicle object
        '''
        self.veh_type = veh_type
        self.max_speed = max_speed
        self.cross_crater = cross_crater
        self.can_travel = can_travel
        return self

    def weather_suitability(self, wetter):
        '''
    This Vehicle class function checks the suitability of the vehicle type(class) with the weather
    in which it can be driven. It takes a weather object as parameter and checks if the weather
    object is in the list of permitted weather type in the vehicle class. '''
        return wetter in self.can_travel

class Orbit():
    '''
    This Orbit class creates Orbit object/instances with attributes of its route name, distance between
    start & end point, and the number of craters in the orbit route. '''

    def __init__(self):
        pass

    def setOrbit(self, route_name, distance, craters, traffic_speed, point1, point2):
        '''
        This object function initializes the attributes of an Orbit object
        '''
        self.route_name = route_name
        self.distance = distance
        self.craters = craters
        self.traffic_speed = traffic_speed
        self.point1 = point1
        self.point2 = point2
        return

    def defineOrbit(self, name, orbitSpeed, orbit_object_datafile):
        '''
        This object function initializes the attributes of an Orbit object. It takes
        in an user input of speed of an orbit and uses the passed on module defined values
        of the name of the Orbit and the datafile location, and creates an orbit object.
        '''
        import json
        with open(orbit_object_datafile, "r") as file_temp1:
            data = json.load(file_temp1)
        for eachOrbitKey in data:
            if data[eachOrbitKey]["route_name"] == name:
                data[eachOrbitKey]["traffic_speed"] = orbitSpeed
                with open(orbit_object_datafile, "w") as file_temp2:
                    json.dump(data, file_temp2)
                    self.setOrbit(data[eachOrbitKey]["route_name"], data[eachOrbitKey]["distance"], data[eachOrbitKey]["craters"], data[eachOrbitKey]["traffic_speed"], data[eachOrbitKey]["point_one"], data[eachOrbitKey]["point_two"])
        return self
