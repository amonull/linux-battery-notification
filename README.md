# linux-battery-notification

this is my first proper attempt at trying to make a git repo and working with both python and bash at the same time so if someting doesnt work i wont be of much help.

used to send notification when battery is low, critical or full. as this script does use cronie to work it will not send a message the instant battery percentage falls to or below the low/critical percentage and will take a full minute.
the only reason this file uses python as well is because my bash scripting skills were not good enough to make it check for battery health but it should be possible to do so if you do wish to do it.

depends:
- python3
- dunst
- cronie
- acpi

installation:
- git clone https://github.com/amonull/linux-battery-notification.git && cd linux-battery-notification
- cp script /path/you/want
- chmod +x /path/to/script
- add this to your crontab -e 

example on how my crontab -e looks:

```* * * * * /usr/bin/python3 /path/to/file```


IMPORTANT

to use GUI applications from cronie you may need to add

```DISPLAY=:0```
