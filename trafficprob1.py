'''This program evaluates between 2 routes (Orbits) for the fastest travel time and tells user
which to take on the basis of the minimum travel time. The user gives information on weather
conditions and the trafic speed in each route.'''
import json
from function.functraffic import *
from classfiles.classtraffic import *

while True:
    CURRENT_WEATHER = input("How is the weather currently \
(Choose only Sunny/Rainy/Windy): ").upper()
    if CURRENT_WEATHER in ['SUNNY', 'RAINY', 'WINDY']:
        break
ORBITS = []
ORBSPEED = []
ORBIT_SET = []
orbit_object_datafile = "datafiles/orbitdataprob1.txt"
for i in range(2):
    USERINPUTSPEED = True
    ORBITS.append(Orbit())
    name = "Orbit"+str(i+1)
    while USERINPUTSPEED:
        try:
            print("Enter current traffic speed in Orbit-{} : ".format(i+1), end="")
            ORBSPEED.append(float(input()))
            break
        except:
            print('You should only enter number values for speed (either a whole number or a \
                decimal number)')
        else:
            USERINPUTSPEED = False
    OrbitObj = ORBITS[i].defineOrbit(name, ORBSPEED[i], orbit_object_datafile)
    ORBIT_SET.append(OrbitObj)

SET_OF_VEHICLES = []
with open("datafiles/vehicledata.txt", "r") as veh_data:
    v_data = json.load(veh_data)
vehicleObj = []
i=0
for eachVehKey in v_data:
    vehicleObj.append(Vehicle())
    vehicleObj[i].setVehicle(v_data[eachVehKey]['veh_type'], v_data[eachVehKey]['max_speed'],\
                             v_data[eachVehKey]['cross_crater'], v_data[eachVehKey]['can_travel'])
    SET_OF_VEHICLES.append(vehicleObj[i])
    i+=1

ROUTE_OPTIONS = routeOptions(ORBIT_SET, SET_OF_VEHICLES, CURRENT_WEATHER)
if ROUTE_OPTIONS == None:
    print('Try after some time')
else:
    LEAST_TIME_OPTION = minTime(ROUTE_OPTIONS)
    print("Please take {} by {} as it will take the least time of {} hour to travel."
          .format(LEAST_TIME_OPTION[0], LEAST_TIME_OPTION[1], round((LEAST_TIME_OPTION[2]), 2)))
