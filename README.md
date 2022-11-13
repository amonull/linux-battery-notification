# linux-battery-notification
if you want to change the low battery or critical battery levels LOW/CIRITICAL_BATTERY and change the 15/5 to your desired level. 

notify2 uses the notify2 library while the other file uses subprocess to send their notification. they do the same things just in different ways.

if you dont want to use the papirus icons remove it from where the notification is being sent (subprocess.run[] for normal and full/low/crit_notification for notify2).

**depends:**
- python3
- dunst
- cronie
- papirus-icon-theme

if using notify2 version:
```pip install notify2```

**installation:**
- git clone https://github.com/amonull/linux-battery-notification.git && cd linux-battery-notification
- cp script /path/to/script
- chmod +x /path/to/script
- add this to your crontab -e 

**example on how my crontab -e looks:**

```* * * * * /usr/bin/python3 /path/to/file```


**IMPORTANT**

to use GUI applications from cronie you may need to add

```DISPLAY=:0```
