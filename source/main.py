import sys
import csv
import types
import time
from os import system
from SimConnect import *

sm = None
myBindings = []
aq = None
ae = None
RGBDefaultBackground = None
RGBINOPColor = None

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

    aq = AircraftRequests(sm, _time=defaultRefreshTime)    

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

            if row["SimVar"] == "BACKGROUND":
                RGBDefaultBackground = row["SimVar"]
                print("Default Key Background Color will be ",RGBDefaultBackground)
            elif row["SimVar"] == "INOP":
                RGBINOPColor = row["SimVar"]
                print("INOP SimVar Color will be ",RGBINOPColor)
            else:                
                #print(f'\t Title: {row["Title"]} SimVar: {row["SimVar"]} SimVarValueToMatch: {row["SimVarValueToMatch"]} RGBColorIf: {row["RGBColorIf"]} RGBColorElse: {row["RGBColorElse"]}.')           
                csv_rows.append(row)
                print(f'Added variable from line {line_count} with name {row["SimVar"]}')
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
        system('cls')
        for i in myBindings:
            #print("getting value for ",i)
            var_value = None
            var_value = aq.get(i["SimVar"])
            print(f'Var: {i["SimVar"]}, Value: {var_value}')
        time.sleep(2)
else:
    print("SimConnect Object was not initialized.")