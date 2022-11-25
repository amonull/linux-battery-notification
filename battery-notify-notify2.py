#!/usr/bin/python3

import tempfile
import glob
import notify2

notify2.init("battery-notify")

main_path = "/sys/class/power_supply/BAT0"
main_tmp_path = "/tmp"

opened_energy_full = open(f"{main_path}/energy_full", 'r')
opened_energy_full_design = open(f"{main_path}/energy_full_design", 'r')
opened_battery_level = open(f"{main_path}/energy_now", 'r')
opened_status = open(f"{main_path}/status", 'r')

energy_full = int(opened_energy_full.read())
energy_full_design = int(opened_energy_full_design.read())
battery_level = int(opened_battery_level.read())
status = str(opened_status.read().replace("\n", ""))

try:
    opened_tmp_battery_state_status = open(glob.glob(f"{main_tmp_path}/battery-state-stat.*")[0], 'r+')
except IndexError:
    opened_tmp_battery_state_status = tempfile.NamedTemporaryFile(mode='r+', delete=False, prefix="battery-state-stat.")
try:
    tmp_battery_state_status = int(opened_tmp_battery_state_status.read()) # MUST be kept as int and not changed to str since only ints work (i.e. "CRITICAL" does not work)
    opened_tmp_battery_state_status.seek(0)
except ValueError:
    tmp_battery_state_status = 0

if (energy_full/energy_full_design)*100 > 99:
    # int(99.9%) == 99% (can reach it) round(99.9%) == 100% (cannot reach it) 
    BATTERY_MAX = int((energy_full / energy_full_design) *100)
else:
    BATTERY_MAX = round((energy_full / energy_full_design) *100)
BATTERY_LEVEL = round((battery_level / energy_full) *100)

DMG_BAT_DIFF = 100 - BATTERY_MAX

LOW_BATTERY = round((15/100) *BATTERY_MAX)
CRITICAL_BATTERY = round((5/100) *BATTERY_MAX)

def exit_func():
    opened_energy_full.close()
    opened_energy_full_design.close()
    opened_battery_level.close()
    opened_status.close()
    opened_tmp_battery_state_status.close()

def main():
    if status == "Discharging":
        if (CRITICAL_BATTERY >= BATTERY_LEVEL) and (tmp_battery_state_status != 3):
            crit_notification = notify2.Notification(summary="Critical Battery", message=f"Battery Level Is {BATTERY_LEVEL}%", icon="/usr/share/icons/Papirus/16x16/status/package-remove.svg")
            crit_notification.set_urgency(notify2.URGENCY_CRITICAL)
            crit_notification.set_timeout(15000)
            crit_notification.show()
            opened_tmp_battery_state_status.truncate()
            opened_tmp_battery_state_status.write("3")
        if (LOW_BATTERY  >= BATTERY_LEVEL) and (tmp_battery_state_status != 2):
            low_notification = notify2.Notification(summary="Low Battery", message=f"Battery Level Is {BATTERY_LEVEL}%", icon="/usr/share/icons/Papirus/16x16/status/package-remove.svg")
            low_notification.set_urgency(notify2.URGENCY_NORMAL)
            low_notification.set_timeout(15000)
            low_notification.show()
            opened_tmp_battery_state_status.truncate()
            opened_tmp_battery_state_status.write("2")
    else:
        # i perfer continous notifications when bat is full
        if (BATTERY_LEVEL == BATTERY_MAX): #and (tmp_battery_state_status != 1):
            full_notification = notify2.Notification(summary="Full Battery", message=f"Battery Level Is {BATTERY_LEVEL+DMG_BAT_DIFF}%", icon="/usr/share/icons/Papirus/16x16/status/package-install.svg")
            full_notification.set_urgency(notify2.URGENCY_LOW)
            full_notification.set_timeout(15000)
            full_notification.show()
            opened_tmp_battery_state_status.truncate()
            opened_tmp_battery_state_status.write("1")

    exit_func()

if __name__ == "__main__":
    main()
