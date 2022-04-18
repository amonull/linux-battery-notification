#!/usr/bin/python3

import subprocess

main_path="/sys/class/power_supply/BAT0"

energy_full = int(open(f"{main_path}/energy_full").read())
energy_full_design = int(open(f"{main_path}/energy_full_design").read())
battery_level = int(open(f"{main_path}/energy_now").read())
status = str(open(f"{main_path}/status").read()).replace("\n", "")

# POLYBAR BATTERY MODULE ROUNDS SO MOST VARIABLES ARE ALSO ROUNDED
BATTERY_LEVEL = round((battery_level / energy_full) *100)
# BATTEYR_MAX needs to be int. or it cant reach to higher percentages (battery cant reach 100 even if life at 99.9%) int(99.9)=99 round(99.9)=100
BATTERY_MAX = int((energy_full / energy_full_design) *100)

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
