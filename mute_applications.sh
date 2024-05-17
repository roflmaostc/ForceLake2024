#!/bin/bash



# export XDG_RUNTIME_DIR="/run/user/1000" && export DISPLAY=:0 && /usr/bin/bash /home/username/mute_applications.sh

#list_of_inds=`pacmd list-sink-inputs | awk '/index:|chromium:/ {print $2};'`


# list_of_inds=`pacmd list-sink-inputs | tr '\n' '\r' | perl -pe 's/.*? *index: ([0-9]+).+?application\.name = "([^\r]+)"\r.+?(?=index:|$)/\2:\1\r/g' | tr '\r' '\n' | cut -d : -f2#`

list_of_inds=`pacmd list-sink-inputs | tr '\n' '\r' | perl -pe 's/.*? *index: ([0-9]+).+?application\.name = "([^\r]+)"\r.+?(?=index:|$)/\2:\1\r/g' | tr '\r' '\n' | grep Chromium | cut -d : -f2`

readarray -t array <<< "$list_of_inds"
echo $list_of_inds

for i in "${array[@]}"; do
    pacmd set-sink-input-mute $i true
    echo $i
done

mplayer $1 

for i in "${array[@]}"; do
    pacmd set-sink-input-mute $i false
done
