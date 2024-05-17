#!/bin/python

from datetime import datetime, timedelta
import time
import subprocess
import os

import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

APPLICATON = "Chromium"

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

PATH = "/home/fxw/Documents/Sport/Ultimate_Frisbee/2024_Force_Lake/ForceLake2024"

year = 2024
month = 5
saturday = 25
sunday = 26

slots_saturday = [datetime(2024, 5, saturday, i, 0) for i in range(9, 17)]


# 0 Hammer Novas
# 1 Universe Huckers
# 2 NASA Noobs
# 3 Space Cowboys
# 4 Overhead Orbiters
# 5 Layout Alliance
# 6 Greatest Wookies
# 7 Moon Patrol
# 8 Scoober Seekers
# 9 Vulcan League

teams = ["0_hammer_novas", "1_universe_huckers", "2_nasa_noobs", "3_space_cowboys", "4_overhead_orbiters", "5_layout_alliance", "6_greatest_wookies", "7_moon_patrol", "8_scoober_seekers", "9_vulcan_league"]

# HAMMER NOVAS vs UNIVERSE HUCKERS	    NASA NOOBS vs	SPACE COWBOYS	    OVERHEAD ORBITERS vs LAYOUT ALLIANCE
# GREATEST WOOKIES vs MOON PATROL       SCOOBER SEEKERS vs VULCAN LEAGUE    WARM - UP
# OVERHEAD ORBITERS	vs NASA NOOBS	    HAMMER NOVAS vs SPACE COWBOYS	    UNIVERSE HUCKERS vsLAYOUT ALLIANCE
# GREATEST WOOKIES vs VULCAN LEAGUE	    WARM - UP		                    SCOOBER SEEKERS	vs MOON PATROL
# WARM - UP		                        SPACE COWBOYS vs LAYOUT ALLIANCE    UNIVERSE HUCKERS vs NASA NOOBS
# GREATEST WOOKIES vs OVERHEAD ORBITERS	SCOOBER SEEKERS	vs HAMMER NOVAS	    MOON PATROL	vs VULCAN LEAGUE
# LAYOUT ALLIANCE vs NASA NOOBS	        WARM - UP		                    UNIVERSE HUCKERS vs SPACE COWBOYS
# MOON PATROL vs OVERHEAD ORBITERS	    SCOOBER SEEKERS	vs GREATEST WOOKIES	VULCAN LEAGUE vs HAMMER NOVAS


# insert numbers in front of the names
# 1 HAMMER NOVAS vs 2 UNIVERSE HUCKERS	        3 NASA NOOBS vs	4 SPACE COWBOYS	            5 OVERHEAD ORBITERS vs 6 LAYOUT ALLIANCE
# 7 GREATEST WOOKIES vs 8 MOON PATROL           9 SCOOBER SEEKERS vs 10 VULCAN LEAGUE       WARM - UP
# 5 OVERHEAD ORBITERS	vs 3 NASA NOOBS	        1 HAMMER NOVAS vs 4 SPACE COWBOYS	        2 UNIVERSE HUCKERS vs 6 LAYOUT ALLIANCE
# 7 GREATEST WOOKIES vs 10 VULCAN LEAGUE	    WARM - UP		                            9 SCOOBER SEEKERS	vs 8 MOON PATROL
# WARM - UP		                                4 SPACE COWBOYS vs 6 LAYOUT ALLIANCE        2 UNIVERSE HUCKERS vs 3 NASA NOOBS
# 7 GREATEST WOOKIES vs 5 OVERHEAD ORBITERS 	9 SCOOBER SEEKERS	vs 1 HAMMER NOVAS	    8 MOON PATROL	vs 10 VULCAN LEAGUE
# 6 LAYOUT ALLIANCE vs 3 NASA NOOBS	            WARM - UP		                            2 UNIVERSE HUCKERS vs 4 SPACE COWBOYS
# 8 MOON PATROL vs 5 OVERHEAD ORBITERS	        9 SCOOBER SEEKERS	vs 7 GREATEST WOOKIES	10 VULCAN LEAGUE vs 1 HAMMER NOVAS

# if there is "WARM - UP", do "None, None"

matches_saturday = [
    [0, 1, 2, 3, 4, 5],
    [6, 7, 8, 9, None, None],
    [4, 2, 0, 3, 1, 5],
    [6, 9, None, None, 8, 7],
    [None, None, 3, 5, 1, 2],
    [6, 4, 8, 0, 7, 9],
    [5, 2, None, None, 1, 3],
    [7, 4, 8, 6, 9, 0],
]

def find_slot(slots, time_to_find):
    for i in range(len(slots)):
        if slots[i] == time_to_find:
            return i

    return None

# 10min before the match
# announce teams
# 5min before the match 
# 0min matches start
# 22min after the start, halftime
# 40min after start, matches almost over
# 45min after start, matches over


def main(now=None):
    if now is None:
        now = datetime.now().replace(microsecond=0, second=0)
    
    # Saturday    
    if now.day == 25:
        # announce teams
        slot = find_slot(slots_saturday, now + deltat(10))
        if slot is not None:
            mute()
            if matches_saturday[slot][0] is not None:
                team1 = teams[matches_saturday[slot][0]]
                team2 = teams[matches_saturday[slot][1]]
                print("Match : ", team1, " vs ", team2)
                play_sound([os.path.join(PATH, "files/Team-field-announcements/field_1.m4a.mp3"),
                            os.path.join(PATH, "files/Team-field-announcements/" + team1 + ".m4a.mp3"),
                            os.path.join(PATH, "files/Team-field-announcements/versus.m4a.mp3"),
                            os.path.join(PATH, "files/Team-field-announcements/" + team2 + ".m4a.mp3")])
            if matches_saturday[slot][2] is not None:
                team1 = teams[matches_saturday[slot][2]]
                team2 = teams[matches_saturday[slot][3]]
                print("Match : ", team1, " vs ", team2)
                play_sound([os.path.join(PATH, "files/Team-field-announcements/field_2.m4a.mp3"),
                            os.path.join(PATH, "files/Team-field-announcements/" + team1 + ".m4a.mp3"),
                            os.path.join(PATH, "files/Team-field-announcements/versus.m4a.mp3"),
                            os.path.join(PATH, "files/Team-field-announcements/" + team2 + ".m4a.mp3")])
            if matches_saturday[slot][4] is not None:
                team1 = teams[matches_saturday[slot][4]]
                team2 = teams[matches_saturday[slot][5]]
                print("Match : ", team1, " vs ", team2)
                play_sound([os.path.join(PATH, "files/Team-field-announcements/field_3.m4a.mp3"),
                            os.path.join(PATH, "files/Team-field-announcements/" + team1 + ".m4a.mp3"),
                            os.path.join(PATH, "files/Team-field-announcements/versus.m4a.mp3"),
                            os.path.join(PATH, "files/Team-field-announcements/" + team2 + ".m4a.mp3")])

            unmute()
        # 5min before the match
        slot = find_slot(slots_saturday, now + deltat(5))
        if slot is not None:
            mute()
            print("Matches start in 5min")
            play_sound([os.path.join(PATH, "files/MatchsStartIn5_en.mp3")])
            unmute()

        # 0min matches start
        slot = find_slot(slots_saturday, now)
        if slot is not None:
            mute()
            print("Matches start now")
            play_sound([os.path.join(PATH, "files/MatchsStart.mp3")])
            unmute()


        # 22min after the start, halftime
        slot = find_slot(slots_saturday, now - deltat(22))
        if slot is not None:
            mute()
            print("Halftime")
            play_sound([os.path.join(PATH, "files/halftime.mp3")])
            unmute()

        # 40min after the start, end of the match
        slot = find_slot(slots_saturday, now - deltat(40))
        if slot is not None:
            mute()
            print("Matches almost over")
            play_sound([os.path.join(PATH, "files/MatchsEndIn5.mp3")])
            unmute()

        # 45min after the start, end of the match
        slot = find_slot(slots_saturday, now - deltat(45))
        if slot is not None:
            mute()
            print("Matches over")
            play_sound([os.path.join(PATH, "files/MatchsEnd_with_gameover.mp3")])

            unmute()
    # Sunday
    now.day == 26
       


    return

main(datetime(2024, 5, 25, 8, 50))
main(datetime(2024, 5, 25, 8, 55))
main(datetime(2024, 5, 25, 9, 0))
main(datetime(2024, 5, 25, 9, 22))
main(datetime(2024, 5, 25, 9, 40))
main(datetime(2024, 5, 25, 9, 45))

