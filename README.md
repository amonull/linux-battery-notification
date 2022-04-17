# linux-battery-notification

this is a python only script that uses notify-send to send user notifications when their battery is too low(15%) or critical(5%) 

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

so far this script sends user notifications continusly it is not inteneded to be that way i just havent figured out how to not do it that way.
