# linux-battery-notification
gives notifications to user when their battery is 15% or 5% or when full. when battery is 5% or full a beep sound is sent using sox.

the beep sound working with cronie is not yet tested and may not work as expected.

papirus icon theme dependency can be removed buy commenting out the ```-i``` line from ```subporcess.run``` for when the notification is being sent to not use any icons.

# depends:
- python3
- acpi
- dunst (notification)
- sox (sound/beep effect)
- cronie
- papirus-icon-theme (optional) (used to have icons when notification is sent)

# TODO:
- make getting the path of acpi/send-notify/play more versitile to work on other paths/when cronie doesn't have access to path.
- make having icons optional.
- make having sound optional.
- make temp files optional (incase the user wants repeated notification).

# installation:
- git clone https://github.com/amonull/linux-battery-notification.git && cd linux-battery-notification
- chmod +x /path/to/script # must be executable for all user for crontab to access it
- add this to your crontab -e 

**example on how my crontab -e looks:**

```* * * * * /usr/bin/python3 /path/to/file```


**IMPORTANT**

to use GUI applications from cronie you may need to add

```DISPLAY=:0```
