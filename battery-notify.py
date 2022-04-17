#!/usr/bin/python3

import subprocess

main_path="/sys/class/power_supply/BAT0"

with open(f"{main_path}/energy_full") as energy_full:
    energy_full = int(energy_full.read()) 
with open(f"{main_path}/energy_full_design") as energy_full_design:
    energy_full_design = int(energy_full_design.read())
with open(f"{main_path}/energy_now") as battery_level:
    battery_level = int(battery_level.read())
with open(f"{main_path}/status") as status:
    status = str(status.read()).replace("\n", "")

# POLYBAR BATTERY MODULE ROUNDS SO MOST VARIABLES ARE ALSO ROUNDED
BATTERY_LEVEL = round((battery_level / energy_full) *100)
# BATTEYR_MAX needs to be int. or it cant reach to higher percentages (battery cant reach 100 even if life at 99.9% as round makes 99.9 to 100 but int makes 99.9 just 99)
BATTERY_MAX = int((energy_full / energy_full_design) *100)

# to change low/critical being 15/5 change the first values
LOW_BATTERY = round((15/100) *BATTERY_MAX)
CRITICAL_BATTERY = round((5/100) *BATTERY_MAX)

def main():
    # checks if battery is charging and if it is it doesnt run it
    if status == "Discharging":
        # full path for notify-send (/usr/bin/notify-send) is needed for crontab
        if LOW_BATTERY  >= BATTERY_LEVEL and BATTERY_LEVEL >= CRITICAL_BATTERY and BATTERY_LEVEL != CRITICAL_BATTERY:
            subprocess.run(["/usr/bin/notify-send", "-t", "15000", "-u", "normal", "Low Battery", f"Battery Level Is {BATTERY_LEVEL}%"])
        elif CRITICAL_BATTERY >= BATTERY_LEVEL:
            subprocess.run(["/usr/bin/notify-send", "-t", "15000", "-u", "critical", "Critical Battery", f"Battery Level Is {BATTERY_LEVEL}%"])

if __name__ == "__main__":
    main()
