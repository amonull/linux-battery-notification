#!/usr/bin/python3

# sys.exit(value) used to return the correct value to help choose correct if statement in bash
import sys
# using sys.exit(value) isnt ideal as it is meant to be used to exit with error codes but couldnt find another way to pass a value to bash from pyhton script without creating another file

with open(r"/sys/class/power_supply/BAT0/energy_full") as energy_full:
    energy_full = int(energy_full.read()) 
with open(r"/sys/class/power_supply/BAT0/energy_full_design") as energy_full_design:
    energy_full_design = int(energy_full_design.read())
with open(r"/sys/class/power_supply/BAT0/energy_now") as battery_level:
    battery_level = int(battery_level.read())


BATTERY_LEVEL = int((battery_level / energy_full) *100)
BATTERY_MAX = int((energy_full / energy_full_design) *100)

LOW_BATTERY = int((15/100) *BATTERY_MAX)
CRITICAL_BATTERY = int((5/100) *BATTERY_MAX)

#run this script from bash after checking if battery is cahrging or not
def main():
    if LOW_BATTERY  >= BATTERY_LEVEL:
        return "Low"
    if CRITICAL_BATTERY >= BATTERY_LEVEL:
        return "Critical"
    if BATTERY_LEVEL == BATTERY_MAX:
        return "Full"

if __name__ == "__main__":
    return_value = main()
    sys.exit(return_value)
