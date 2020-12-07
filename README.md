# SimVarLights
Have your Simulator State Machine to your Lighted Devices (a Python Project)

![SimVarLights Logo](/assets/SimVarLights-github-preview.png)

# Description
A script for updating Addressable RGB Lights from SimConnect Variables. 

## It was developed and tested with:
* Flight Simulator 2020
* OpenRGB Python
* Razer Chroma v2
* Python 3.9

## It will help if you have:
* Elemental Understanding of SimConnect and Simulator Variables
* Elemental Understanding of Python
* Elemental Understanding of Git
* Know how to edit a CSV file

## Instructions
1. Install Python
2. Clone the Repo to a suitable location
3. Run PIP to install requirements.txt
4. Edit the bindings.csv to add/remove SimVars as needed, use Microsoft SDK as a Reference
5. Launch your simulator and start your flight
6. Launch main.py

## The keyboard will light based on the dynamic status of variables as configured.

# Next Steps / ToDo
* Gauge interest and feedback
* Testing and Cleanup 
* Adding more parameters to configuration file
* Build and Release Management / Automation
* Adding more default variables (feedback is appreciated)

# Known Issues
* Due to OpenRGB Python limitation, app is ignoring custom light colors

