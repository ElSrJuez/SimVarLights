#####################################################################
# SimVarLights v0.1
# Illuminated RGB Addressable Lights based on SimConnect Variables
# by: Diego Vásquez (2020)
# This Software is Open Source under GNU License
# MAIN MODULE
import sys
import csv
import types
import time
from os import system
from openrgb.utils import RGBColor
from SimConnect import *
from RGB import *

sm = None
myBindings = []
aq = None
ae = None
RGBDefaultBackground = None
RGBINOPColor = None

#######################################################################
# Data File has Config Parameters including Simulator Variable Bindings
filename = 'data/bindings.csv'

#######################################################################
# Function for Creating SimConnect Objects and Connection
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

    aq = AircraftRequests(sm, _time=defaultRefreshTime)    

#######################################################################
# Function for Loading Configuration File
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

#######################################################################
# Read Special Global Configuration Lines
            if row["SimVar"] == "BACKGROUND":
                RGBDefaultBackground = row["SimVar"]
                print("Default Key Background Color will be ",RGBDefaultBackground)
            elif row["SimVar"] == "INOP":
                RGBINOPColor = row["SimVar"]
                print("INOP SimVar Color will be ",RGBINOPColor)

#######################################################################
# Read Variables
            else:                
                csv_rows.append(row)
                print(f'Added variable from line {line_count} with name {row["SimVar"]}')
                line_count += 1
            
        print(f'Processed {line_count} lines.')
        return csv_rows

#######################################################################
# Create Simulator Variable List
def init_simvars(varList):
    myVars=[]

    for i in varList:
        meta = None
        print(f'Getting variable details for {i["SimVar"]}...')
        meta = aq.find(i["SimVar"])
   
        t = i.copy()
        if meta:            
            t["INOP"]=False
        else:
            t["INOP"]=True
            print(f'Warning, could not find variable {i["SimVar"]}.')
        myVars.append(t)
    return myVars


#######################################################################
# Invoke Load Configuration File
csv_data = read_config(filename)
#print("csv file dictionary: ",csv_data.__dict__)

#######################################################################
# Initialize SimConnect
init_simconnect(defaultRefreshTime = 2000)

#######################################################################
# Main Processing
if sm is not None:
    print("SimConnect Object: ",sm)    
    myBindings = init_simvars(csv_data)
    print(dir(myBindings))

#######################################################################
# Set Special Colors for Variables that are not Found on the Live Sim
    inopLights = []
    for i in myBindings:
        if i["INOP"]:
            print(f'Marking variable {i["SimVar"]} with RGBLEDNumber {i["RGBLEDNumber"]} as INOP.')
            inopLights.append(int(i["RGBLEDNumber"]))
    keyboard_leds = initRGB()
    led_count=len(keyboard_leds)
    light_background(backColorHEX='#000020',inopColorHEX='#800000',INOP=inopLights)

#######################################################################
# Main Loop
    while True:
        system('cls')
        for i in myBindings:
            #print("getting value for ",i)
            var_value = None
            var_value = aq.get(i["SimVar"])
            #RGBColorIf = RGBColor.fromHEX(i["RGBColorIf"])
            #RGBColorElse = RGBColor.fromHEX(i["RGBColorElse"])
            RGBColorIf=RGBColor(0,0,255)
            RGBColorElse=RGBColor(0,32,0)
            print(f'Var: {i["SimVar"]}, Value: {var_value}')
            if int(i["SimVarValueToMatch"]) == var_value:
                light_led(id = int(i["RGBLEDNumber"]),litColor = RGBColorIf)
            else:
                light_led(id = int(i["RGBLEDNumber"]),litColor = RGBColorElse)
        time.sleep(1)
else:
    print("SimConnect Object was not initialized.")