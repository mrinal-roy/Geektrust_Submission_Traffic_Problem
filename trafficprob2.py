'''This program evaluates between the fastest route to visit Hallitharam and RK Puram on the basis
of the weather conditions and traffic speeds of the orbits 1,2,3, and 4. It then suggests King Shan
to opt the type of vehicle and take the quickest orbit route.'''
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
orbit_object_datafile = "datafiles/orbitdataprob2.txt"
for i in range(4):
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
'''Any route combination has to have Orbit4 in common. So evaluating the time taken by each vehicle
under the weather condition to travel Orbit 4 by separating Orbit 4 object from the set of orbits.
'''
ORBIT4 = ORBIT_SET.pop()
ORBIT_SET4 = []
ORBIT_SET4.append(ORBIT4)
ROUTE_OPTION1 = routeOptions(ORBIT_SET, SET_OF_VEHICLES, CURRENT_WEATHER)
ROUTE_OPTION2 = routeOptions(ORBIT_SET4, SET_OF_VEHICLES, CURRENT_WEATHER)

TOTAL_ROUTE_TIMES = []
for each2 in ROUTE_OPTION2:
    for each1 in ROUTE_OPTION1:
        if each1[0]==each2[0]:
            means = each1[0]
            route1 = each1[1]
            route2 = each2[1]
            time = each1[2]+each2[2]
            TOTAL_ROUTE_TIMES.append((means, route1, route2, time))
        else:
            continue
LEAST_TIME_OPTION = minTime(TOTAL_ROUTE_TIMES)
LEAST_TIME_OPTION[1]
for eachOrbitObj in ORBIT_SET:
    if eachOrbitObj.route_name == LEAST_TIME_OPTION[1]:
        dest1 = eachOrbitObj.point2
    else:
        continue
    if dest1 == ORBIT4.point1:
        dest2 = ORBIT4.point2
    else:
        dest2 = ORBIT4.point1
        continue

print("Please take vehicle {} to {} via {} and then {} via {}."
.format(LEAST_TIME_OPTION[0], dest1, LEAST_TIME_OPTION[1], dest2, LEAST_TIME_OPTION[2]))
