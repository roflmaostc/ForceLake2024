#!/bin/python

from datetime import datetime, timedelta
import time
import subprocess

import sys

import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'



PATH = sys.argv[1]
APPLICATON = sys.argv[2]

year = 2024
month = 5
saturday = 25
sunday = 26

slots_saturday = [datetime(year, month, saturday, i, 0) for i in range(9, 17)]
teams = ["0_hammer_novas", "1_universe_huckers", "2_nasa_noobs", "3_space_cowboys", "4_overhead_orbiters", "5_layout_alliance", "6_greatest_wookies", "7_moon_patrol", "8_scoober_seekers", "9_vulcan_league"]


slots_sunday = [datetime(year, month, sunday, 9, 0),
                datetime(year, month, sunday, 10, 0),
                datetime(year, month, sunday, 11, 15),
                datetime(year, month, sunday, 12, 15),
                datetime(year, month, sunday, 13, 45),
                datetime(year, month, sunday, 14, 45)]


# matches_saturday = [
#     [0, 1, 2, 3, 4, 5],
#     [6, 7, 8, 9, None, None],
#     [4, 2, 0, 3, 1, 5],
#     [6, 9, None, None, 8, 7],
#     [None, None, 3, 5, 1, 2],
#     [6, 4, 8, 0, 7, 9],
#     [5, 2, None, None, 1, 3],
    # [7, 4, 8, 6, 9, 0],
# ]




# make a schedule like this with numbers, but just with the team names as string, if there is "Warm - Up" just insert two times None
# matches_satur
# HAMMER NOVAS	UNIVERSE HUCKERS	 NASA NOOBS	SPACE COWBOYS	OVERHEAD ORBITERS	LAYOUT ALLIANCE
# GREATEST WOOKIES	MOON PATROL	SCOOBER SEEKERS	VULCAN LEAGUE	WARM - UP	
# OVERHEAD ORBITERS	 NASA NOOBS	HAMMER NOVAS	SPACE COWBOYS	UNIVERSE HUCKERS	LAYOUT ALLIANCE
# GREATEST WOOKIES	VULCAN LEAGUE	WARM - UP		SCOOBER SEEKERS	MOON PATROL
# WARM - UP		SPACE COWBOYS	LAYOUT ALLIANCE	UNIVERSE HUCKERS	 NASA NOOBS
# GREATEST WOOKIES	OVERHEAD ORBITERS	SCOOBER SEEKERS	HAMMER NOVAS	MOON PATROL	VULCAN LEAGUE
# LAYOUT ALLIANCE	 NASA NOOBS	WARM - UP		UNIVERSE HUCKERS	SPACE COWBOYS
# MOON PATROL	OVERHEAD ORBITERS	SCOOBER SEEKERS	GREATEST WOOKIES	VULCAN LEAGUE	HAMMER NOVAS

# matches_sunday
matches_saturday = [
    ["HAMMER_NOVAS", "UNIVERSE_HUCKERS", "NASA_NOOBS", "SPACE_COWBOYS", "OVERHEAD_ORBITERS", "LAYOUT_ALLIANCE"],
    ["GREATEST_WOOKIES", "MOON_PATROL", "SCOOBER_SEEKERS", "VULCAN_LEAGUE", None, None],
    ["OVERHEAD_ORBITERS", "NASA_NOOBS", "HAMMER_NOVAS", "SPACE_COWBOYS", "UNIVERSE_HUCKERS", "LAYOUT_ALLIANCE"],
    ["GREATEST_WOOKIES", "VULCAN_LEAGUE", None, None, "SCOOBER_SEEKERS", "MOON_PATROL"],
    [None, None, "SPACE_COWBOYS", "LAYOUT_ALLIANCE", "UNIVERSE_HUCKERS", "NASA_NOOBS"],
    ["GREATEST_WOOKIES", "OVERHEAD_ORBITERS", "SCOOBER_SEEKERS", "HAMMER_NOVAS", "MOON_PATROL", "VULCAN_LEAGUE"],
    ["LAYOUT_ALLIANCE", "NASA_NOOBS", None, None, "UNIVERSE_HUCKERS", "SPACE_COWBOYS"],
    ["MOON_PATROL", "OVERHEAD_ORBITERS", "SCOOBER_SEEKERS", "GREATEST_WOOKIES", "VULCAN_LEAGUE", "HAMMER_NOVAS"]
]


# WARM - UP		 NASA NOOBS	GREATEST WOOKIES	OVERHEAD ORBITERS	SCOOBER SEEKERS
# UNIVERSE HUCKERS	MOON PATROL	HAMMER NOVAS	LAYOUT ALLIANCE	SPACE COWBOYS	VULCAN LEAGUE

matches_sunday = [[None, None, "NASA_NOOBS", "GREATEST_WOOKIES", "OVERHEAD_ORBITERS", "SCOOBER_SEEKERS"],
                  ["UNIVERSE_HUCKERS", "MOON_PATROL", "HAMMER_NOVAS", "LAYOUT_ALLIANCE", "SPACE_COWBOYS", "VULCAN_LEAGUE"]
                  ]

def deltat(min):
    return timedelta(hours=0, minutes=min)


def find_index(application="Spotify"):
    
    out = str(subprocess.check_output(["pacmd list-sink-inputs"], shell=True))
    indices = []
    for line in out.split("\\n"):
        line = line.strip()
        

        if line.startswith("index"):
            index = line.split()[-1] 
       
        if application in line:
            indices.append(index)

    return indices 


def play_sound(files):
    indices = find_index(APPLICATON)
    for file in files:
        subprocess.call(["mplayer", file])


def mute():
    indices = find_index(APPLICATON)
    for index in indices:
        subprocess.call(["pactl", "set-sink-input-mute", index, "true"])

def unmute():
    indices = find_index(APPLICATON)
    for index in indices:
        subprocess.call(["pactl", "set-sink-input-mute", index, "false"])


def find_slot(slots, time_to_find):
    for i in range(len(slots)):
        if slots[i] == time_to_find:
            return i

    return None


def main(now=None):
    if now is None:
        now = datetime.now().replace(microsecond=0, second=0)
    
    # Saturday    
    if now.day == 25:
        matches = matches_saturday
        slots = slots_saturday
    elif now.day == 26:
        matches = matches_sunday
        slots = slots_sunday
    else:
        return


    # announce teams
    slot = find_slot(slots, now + deltat(10))
    if slot is not None:
        mute()
        if matches[slot][0] is not None:
            team1 = matches[slot][0].lower()
            team2 = matches[slot][1].lower()
            print("Match : ", team1, " vs ", team2)
            play_sound([os.path.join(PATH, "files/" + team1 + ".mp3"),
                        os.path.join(PATH, "files/versus.mp3"),
                        os.path.join(PATH, "files/" + team2 + ".mp3"),
                        os.path.join(PATH, "files/field_1.mp3")])
        if matches[slot][2] is not None:
            team1 = matches[slot][2].lower()
            team2 = matches[slot][3].lower()
            print("Match : ", team1, " vs ", team2)
            play_sound([os.path.join(PATH, "files/" + team1 + ".mp3"),
                        os.path.join(PATH, "files/versus.mp3"),
                        os.path.join(PATH, "files/" + team2 + ".mp3"),
                        os.path.join(PATH, "files/field_2.mp3")])
        if matches[slot][4] is not None:
            team1 = matches[slot][4].lower()
            team2 = matches[slot][5].lower()
            print("Match : ", team1, " vs ", team2)
            play_sound([os.path.join(PATH, "files/" + team1 + ".mp3"),
                        os.path.join(PATH, "files/versus.mp3"),
                        os.path.join(PATH, "files/" + team2 + ".mp3"),
                        os.path.join(PATH, "files/field_3.mp3")])

        unmute()
        return 0


    # 5min before the match
    slot = find_slot(slots, now + deltat(5))
    if slot is not None:
        mute()
        print("Matches start in 5min")
        play_sound([os.path.join(PATH, "files/MatchsStartIn5.mp3")])
        unmute()
        return 0
    
    # 0min matches start
    slot = find_slot(slots, now)
    if slot is not None:
        mute()
        print("Matches start now")
        play_sound([os.path.join(PATH, "files/MatchsStart.mp3")])
        unmute()
        return 0

    # 22min after the start, halftime
    slot = find_slot(slots, now - deltat(23))
    if slot is not None:
        mute()
        print("Halftime")
        play_sound([os.path.join(PATH, "files/halftime.mp3")])
        unmute()
        return 0
    
    # 40min after the start, end of the match
    slot = find_slot(slots, now - deltat(40))
    if slot is not None:
        mute()
        print("Matches almost over")
        play_sound([os.path.join(PATH, "files/MatchsEndIn5.mp3")])
        unmute()
        return 0

    # 45min after the start, end of the match
    slot = find_slot(slots, now - deltat(45))
    if slot is not None:
        mute()
        print("Matches over")
        play_sound([os.path.join(PATH, "files/MatchsEnd.mp3")])

        unmute()
        return 0


    return



if len(sys.argv) > 3 and sys.argv[3] == "debug":
    try:
        # main()
        # main(datetime(year, 5, 26, 8, 50))
        # main(datetime(year, 5, 26, 9, 50))
        # main(datetime(year, 5, 25, 8, 50))
        # main(datetime(year, 5, 25, 9, 50))
        main(datetime(year, 5, 25, 8, 55))
        main(datetime(year, 5, 25, 9, 0))
        main(datetime(year, 5, 25, 9, 23))
        main(datetime(year, 5, 25, 9, 40))
        main(datetime(year, 5, 25, 9, 45))
        main(datetime(year, 5, 25, 9, 50))
    except KeyboardInterrupt:
        unmute()

else:
    main()
    unmute()

