#!/bin/python

from datetime import datetime, timedelta
import time



five_min = timedelta(hours=0, minutes=5)

year = 2024
month = 5
saturday = 25
sunday = 26

slots_saturday = [date(month, year, day, i, 0) for i in range(9, 17)]


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
matches_SAT = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, None, None],
    [5, 3, 1, 4, 2, 6],
    [7, 10, None, None, 9, 8],
    [None, None, 4, 6, 2, 3],
    [7, 5, 9, 1, 8, 10],
    [6, 3, None, None, 2, 4],
    [8, 5, 9, 7, 10, 1],
]




def find_slot(slots, time_to_find):
    for i in length(slots):
        if slots[i] == time_to_find:
            return i

    return None

def main(now=None):
    if now is None:
        now = datetime.now().replace(microsecond=0, second=0)
    
    
    if now.day == 25
        
    if find_slot_index(now + five_min) is not None:
        return



