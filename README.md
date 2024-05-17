# Automatic Announce of games 

Install Python and clone this full repository.

To test some slots run:

```
python play_sounds.py <PATH TO THIS REPOSITORY> debug
```


## Setting up Cronjob
Call `crontab -e` and then insert:
```
* * * * * export XDG_RUNTIME_DIR="/run/user/1000" && export DISPLAY=:0 && /usr/bin/python <PATH>/play_sounds.py <PATH>
```
