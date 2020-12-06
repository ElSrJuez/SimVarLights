
# Initialize SimConnect

from SimConnect import *
import sys
import json

sm = [None]
myVars = [None]
aq = [None]

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

def newVar(varName: str, varRefresh: int):
    global myVars
    global aq 
    thisVar = aq.find(varName)
    if varRefresh > 0:
        thisVar.time = varRefresh
    myVars.append(thisVar)
