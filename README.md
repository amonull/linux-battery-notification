# linux-battery-notification
gives notifications to user when their battery is 15% or 5% or when full. when battery is 5% or full a beep sound is sent using sox.

the beep sound working with cronie is not yet tested and may not work as expected.

# depends:
- python3
- dunst (notification)
- sox (sound/beep effect)
- cronie
- papirus-icon-theme (optional) (used to have icons when notification is sent)

# installation:
- git clone https://github.com/amonull/linux-battery-notification.git && cd linux-battery-notification
- chmod +x /path/to/script # must be executable for all user for crontab to access it
- add this to your crontab -e 

**example on how my crontab -e looks:**

```* * * * * /usr/bin/python3 /path/to/file```


**IMPORTANT**

to use GUI applications from cronie you may need to add

```DISPLAY=:0```
