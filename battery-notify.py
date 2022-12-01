#!/usr/bin/python3

import subprocess
import tempfile
import glob

def main():

    BAT_STAT = subprocess.getoutput("acpi | awk '{print $3}'").replace(',', '')
    BAT_PERCENT = int(subprocess.getoutput("acpi | awk '{print $4}'").replace('%', '').replace(',', '')) # replace used to be able to cast it to int

    CRITICAL_BATTERY = 5
    LOW_BATTERY = 15

    # Holds the status for what notification has been sent so far
    try:
        opened_tmp_battery_state_status = open(glob.glob("tmp/battery-state-stat.*")[0], 'r+')
    except IndexError:
        opened_tmp_battery_state_status = tempfile.NamedTemporaryFile(mode='r+', delete=False, prefix="battery-state-stat.")
    try:
        tmp_battery_state_status = int(opened_tmp_battery_state_status.read()) # MUST be kept as int and not changed to str since only ints work (i.e. "CRITICAL" does not work)
        opened_tmp_battery_state_status.seek(0) # sets cursor to the top of page again
    except ValueError:
        tmp_battery_state_status = 0

    if BAT_STAT == "Discharging":
        if (BAT_PERCENT <= CRITICAL_BATTERY and tmp_battery_state_status != 3): # CRITICAL
            # NOTIFICATION
            subprocess.run(["/usr/bin/notify-send", 
                            "-i", "/usr/share/icons/Papirus/16x16/status/package-remove.svg", 
                            "-t", "15000", 
                            "-u", "critical", 
                            "Critical Battery", 
                            f"Battery Level Is {BAT_PERCENT}%"])
            # SOUND
            subprocess.call(["/usr/bin/play",
                            "-n",
                            "-c4",
                            "synth", "0.25", # SPEED (runs for 0.25 seconds)
                            "sin", "1750"],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.STDOUT)
            opened_tmp_battery_state_status.truncate() # wipes file 
            opened_tmp_battery_state_status.write("3") # writes to file
        elif (BAT_PERCENT <= LOW_BATTERY and tmp_battery_state_status != 2): # LOW
            # NOTIFICATION
            subprocess.run(["/usr/bin/notify-send", 
                            "-i", "/usr/share/icons/Papirus/16x16/status/package-remove.svg",
                            "-t", "15000", 
                            "-u", "normal", 
                            "Low Battery", 
                            f"Battery Level Is {BAT_PERCENT}%"])
            # NO SOUND
            opened_tmp_battery_state_status.truncate()
            opened_tmp_battery_state_status.write("2")
    else:
        if (BAT_PERCENT == 100 and tmp_battery_state_status != 1):
            # NOTIFICATION
            subprocess.run(["/usr/bin/notify-send", 
                            "-i", "/usr/share/icons/Papirus/16x16/status/package-install.svg", 
                            "-t", "15000", 
                            "-u", "Low", 
                            "Full Battery", 
                            f"Battery Level Is {BAT_PERCENT}%"])
            # SOUND
            subprocess.call(["/usr/bin/play",
                            "-n",
                            "-c4",
                            "synth", "0.25", # SPEED (runs for 0.25 seconds)
                            "sin", "1750"],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.STDOUT)
            opened_tmp_battery_state_status.truncate()
            opened_tmp_battery_state_status.write("1")

    opened_tmp_battery_state_status.close()

if __name__ == "__main__":
    main()
