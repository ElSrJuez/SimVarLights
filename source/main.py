import sys
import csv
import types
import time
from SimConnect import *

sm = None
myBindings = []
aq = None
ae = None
RGBDefaultBackground = None

filename = 'data/bindings.csv'

def init_simconnect(defaultRefreshTime: int):
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

def read_config(csv_filename: str):
    global RGBDefaultBackground
    csv_rows = []
    with open(csv_filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0        
        for row in csv_reader:
            print(f"Processing Row {line_count} with data ",row)
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            # Add all Named Configuration Row processing here

            if row["SimVar"] == "BACKGROUND":
                RGBDefaultBackground = row["SimVar"]
                print("Default Key Background Color will be ",RGBDefaultBackground)

            else:                
                #print(f'\t Title: {row["Title"]} SimVar: {row["SimVar"]} SimVarValueToMatch: {row["SimVarValueToMatch"]} RGBColorIf: {row["RGBColorIf"]} RGBColorElse: {row["RGBColorElse"]}.')           
                csv_rows.append(row)
                #for c in csvColumns:
                #    myConcat = c+" "+row[c]
                #    print(f' {", ".join(myConcat)}')
                line_count += 1
            
        print(f'Processed {line_count} lines.')
        return csv_rows

def init_simvars(varList):
    myVars=[]

    for i in varList:
        meta = None
        #print(f'Var {i["SimVar"]}, Title {i["Title"]}, Title {i["Title"]}')
        print(f'Getting variable details for {i["SimVar"]}...')
        meta = aq.find(i["SimVar"])
        #print(dir(meta))
        #print(meta.__dict__)
        #print(meta["__dict__"]) 
        #if meta is not None:
        #    for att in dir(meta):
        #        print(f'Attribute {att} is {meta[""]}...')
        #        print(att)
        #        print (att, getattr(meta,att))        
        if meta:            
            t = i.copy()
            t["accesible"]=True
            myVars.append(t)
        else:
            print(f'Warning, could not find variable {i["SimVar"]}.')


    return myVars

# Load Configuration File
csv_data = read_config(filename)
#print("csv file dictionary: ",csv_data.__dict__)

# Initialize SimConnect
init_simconnect(defaultRefreshTime = 2000)

if sm is not None:
    print("SimConnect Object: ",sm)    
    myBindings = init_simvars(csv_data)
    print(dir(myBindings))

    while True:
        for i in myBindings:
            #print("getting value for ",i)
            var_value = None
            var_value = aq.get(i["SimVar"])
            print(f'Var: {i["SimVar"]}, Value: {var_value}')
        time.sleep(0.5)
    
    




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