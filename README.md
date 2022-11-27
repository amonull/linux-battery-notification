# linux-battery-notification
if you want to change the low battery or critical battery levels LOW/CIRITICAL_BATTERY and change the 15/5 to your desired level. 

notify2 uses the notify2 library while the other file uses subprocess to send their notification. they do the same things just in different ways.

if you dont want to use the papirus icons remove it from where the notification is being sent (subprocess.run[] for normal and full/low/crit_notification for notify2).

# depends:
- python3
- dunst/libnotify or notify2 (pip install notify2)
- cronie
- papirus-icon-theme (optional)

# TODO:
- add sound using sox/sox-devel
- create another more versatile version using ```acpi | awk '{print $4}' -> get battery percent && acpi | awk  '{print $3}' | cut -d , -f1 -> get status'``` and not reading files. -> should make code faster/less complicated
# installation:
- git clone https://github.com/amonull/linux-battery-notification.git && cd linux-battery-notification
- chmod +x /path/to/script # must be executable for all user for crontab to access it
- add this to your crontab -e 

**example on how my crontab -e looks:**

```* * * * * /usr/bin/python3 /path/to/file```


**IMPORTANT**

to use GUI applications from cronie you may need to add

```DISPLAY=:0```
