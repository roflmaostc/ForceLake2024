# Automatic Announce of games 

Install Python and clone this full repository.
This runs most likely only on Linux. Tested on Arch Linux and Ubuntu.
To test some slots run:

```
python play_sounds.py <PATH TO THIS REPOSITORY> <APPLICATION NAME TO MUTE> debug
```
Application name should be something like *Spotify* or *Chromium*. Check with `pacmd list-sink-inputs` which applications currently run.

## Setting up Cronjob
Call `crontab -e` and then insert. 
```
* * * * * export XDG_RUNTIME_DIR="/run/user/1000" && export DISPLAY=:0 && /usr/bin/python <PATH>/play_sounds.py <PATH> Chromium
```
Be sure that your cronjob is activated `systemctl start cron` and `systemctl enable cron`
