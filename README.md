# linux-battery-notification

used to send notification when battery is low, critical or full. as this script does use cronie to work it will not send a message the instant battery percentage falls to or below the low/critical percentage and will take a full minute.
the only reason this file uses python as well is because my bash scripting skills were not good enough to make it check for battery health but it should be possible to do so if you do wish to do it.

there are 2 versions of this that can be selected:
  with python and bash (battery-notify.py & run-battery-notify):
   calculates the battery health from the energy_full_design and enerfy_full files and decides how the low and critical amounts based on that (15=Low 5=critical).
  
  bash (bash-only-script):
    only sends notification however only uses bash to do this so it i couldnt make it check for battery health but unlike the other version python is not           required and works from a single file.

depends:
- python3 (optional if using bash only)
- dunst
- cronie
- acpi

installation:
- clone this repository and choose the version you want to use
- (only for bash and python script):
if you chose bash and python copy the scripts to /usr/local/bin or change the file path on run-battery-notify line 15 to where ever you copied battery-notify.py to
- chmod +x script(s)
- add this to your crontab -e 

example on how my crontab -e looks:
* * * * * /bin/bash /path/to/file/{bash or bash with python}
