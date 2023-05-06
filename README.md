# linux-battery-notification
gives notifications to user when their battery is 15% or 5% or when full. when battery is 5% or full a beep sound is sent using sox.

the beep sound working with cronie is not yet tested and may not work as expected.

papirus icon theme dependency can be removed buy commenting out the `-i` line from `subporcess.run` for when the notification is being sent to not use any icons.

# depends:
- python3
- notify2
- cronie
- papirus-icon-theme (optional) (used to have icons when notification is sent) to turn notifications off read last part [of](#linux-battery-notification)

# TODO:
- add flags to turn some options off (like icons)
- make temp files optional (incase the user wants repeated notification) (option for flags mentiond above).
- add logging

# installation:
- `$ git clone https://github.com/amonull/linux-battery-notification.git && cd linux-battery-notification`
- `$ pip install -r requirments.txt` # installs notify2
- `$ chmod +x battery-notify/main.py` # must be executable for all user for crontab to access it
- `# mv battery-notify/main.py /usr/local/bin/battery-notify`
- add this to your crontab -e 

**example on how my crontab -e looks:**

`* * * * * /usr/bin/python3 /usr/local/bin/battery-notify`


# Important information for gui with cronie
to use GUI applications from cronie you may need to add

```DISPLAY=:0```
