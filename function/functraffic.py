def crater_factor(current_weather):
    """This function modifies the crater numbers depending on weather conditions."""
    if current_weather == 'SUNNY':
        factor = 0.9
    elif current_weather == 'RAINY':
        factor = 1.2
    else:
        factor = 1
    return factor


def minTime(OPTIONS):
    """This function takes in a list of tupple and returns the tupple with
    minimum time parameter."""
    time_options = [OPTIONS[i][-1] for i in range(len(OPTIONS))]
    time_options.sort()
    min_time = time_options[0]
    for i in range(len(OPTIONS)):
        if OPTIONS[i][-1] == min_time:
            LEAST_TIME_OPTION = OPTIONS[i]
        else:
            continue
    return LEAST_TIME_OPTION


def routeOptions(ORBITS, SET_OF_VEHICLES, CURRENT_WEATHER):
    """This function returns the orbit route options with each vehicle type and the
    time taken in each route option. It basically returns a list of tuples each
    consisiting of a vehicle, route orbit and the time taken to travel in that orbit."""
    OPTION = []
    for eachOrbit in ORBITS:
        if eachOrbit.traffic_speed == 0:
            print('Route {} Blocked'.format(eachOrbit.route_name))
            OPTION = None
            break
        else:
            for eachVehicle in SET_OF_VEHICLES:
                if eachVehicle.weather_suitability(CURRENT_WEATHER):
                    eff_speed = min(eachVehicle.max_speed, eachOrbit.traffic_speed)
                    time_taken = (eachOrbit.distance/eff_speed)+(eachVehicle.cross_crater*eachOrbit.craters*crater_factor(CURRENT_WEATHER)/60)
                    time_taken = round(time_taken, 2)
                    OPTION.append((eachVehicle.veh_type, eachOrbit.route_name, time_taken))
                else:
                    continue
    return OPTION
