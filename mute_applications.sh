#!/bin/bash


# Get the list of all the applications
list_of_inds=`pacmd list-sink-inputs | awk '/index:|firefox:/ {print $2};'`
readarray -t array <<< "$list_of_inds"

for i in "${array[@]}"; do
    pacmd set-sink-input-mute $i true
    echo $i
done

play /home/felix/Downloads/copper-bell-ding-4-204990.mp3

for i in "${array[@]}"; do
    pacmd set-sink-input-mute $i false
done
