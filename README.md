# linux-battery-notification

this script uses rounding as it is meant to be used together with the polybar battery module, from testing before i found that my module was using rounding instead of giving exact battery levels, this can be changed by removing round() and making its variable types float or int. this is a python only script that uses notify-send to send user notifications when their battery is too low(15%) or critical(5%). it uses subprocess to use send-notify. this script also gets battery health and gets a rounded percentage of what the low, critical, full and battery level should be.

**depends:**
- python3
- dunst
- cronie

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
