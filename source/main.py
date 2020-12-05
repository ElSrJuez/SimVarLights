import sys
import svhelper

# Initialize SimConnect



# Get the aircraft's current altitude
altitude = aq.get("PLANE_ALTITUDE")
altitude = altitude + 1000

# Set the aircraft's current altitude
aq.set("PLANE_ALTITUDE", altitude)

ae = AircraftEvents(sm)
# Trigger a simple event
event_to_trigger = ae.find("AP_MASTER")  # Toggles autopilot on or off
event_to_trigger()

# Trigger an event while passing a variable
target_altitude = 15000
event_to_trigger = ae.find("AP_ALT_VAR_SET_ENGLISH")  # Sets AP autopilot hold level
event_to_trigger(target_altitude)
sm.quit()
exit()