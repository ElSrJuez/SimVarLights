import sys
import json
from SimConnect import *

sm = None
myVars = []
aq = None
ae = None
filename 

def initAll(defaultRefreshTime: int):
    global aq
    global sm 
    
    try:
        sm = SimConnect()
    except:
        print("Unexpected error, ",sys.exc_info()[0])
        return

    if sm:
        print("Succesful SimConnect call: ",sm)
    else:
        print("Unsuccesful Simconnect call, exiting.")
        return
    # Note the default _time is 2000 to be refreshed every 2 seconds

    aq = AircraftRequests(sm, _time=defaultRefreshTime)    
    # Use _time=ms where ms is the time in milliseconds to cache the data.
    # Setting ms to 0 will disable data caching and always pull new data from the sim.
    # There is still a timeout of 4 tries with a 10ms delay between checks.
    # If no data is received in 40ms the value will be set to None
    # Each request can be fine tuned by setting the time param.

# Initialize SimConnect
initAll(defaultRefreshTime = 2000)

if sm is not None:
    print(sm)
    brakevar = aq.find('BRAKE_PARKING_INDICATOR')
    print("brake var: ",brakevar)
    myVars.append(brakevar)    
    altitudevar = aq.find('PLANE_ALTITUDE')
    altitudevar.time = 200
    print("altitude var: ",altitudevar)
    myVars.append(altitudevar)
    for i in myVars:
        for att in dir(i):
            print("Var Definition: ", i.definition)
            print("Var Description: ", i.description)
            print("Var Description: ", i.description)
            print (att, getattr(i,att))

    

    #aq.set("PLANE_ALTITUDE", altitude)

    #ae = AircraftEvents(sm)
    # Trigger a simple event
    #event_to_trigger = ae.find("AP_MASTER")  # Toggles autopilot on or off
    #event_to_trigger()

    # Trigger an event while passing a variable
    #target_altitude = 15000
    #event_to_trigger = ae.find("AP_ALT_VAR_SET_ENGLISH")  # Sets AP autopilot hold level
    #event_to_trigger(target_altitude)
    #sm.quit()
else:
    print("SimConnect Object was not initialized.")