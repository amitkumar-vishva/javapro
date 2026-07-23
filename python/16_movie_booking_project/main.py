import os
import sys
from  datetime import datetime

movies = {
    "1": {"title": "The Super Mario Galaxy Movie", "language": "English", "print": 800},
    "2": {"title": "Avengers: Endgame", "language": "English", "print": 1200},
    "3": {"title": "Spider-Man: No Way Home", "language": "English", "print": 950},
    "4": {"title": "KGF: Chapter 2", "language": "Hindi", "print": 850},
    "5": {"title": "RRR", "language": "Telugu", "print": 900},
    "6": {"title": "Pushpa: The Rise", "language": "Telugu", "print": 750},
    "7": {"title": "Dangal", "language": "Hindi", "print": 700},
    "8": {"title": "Baahubali: The Beginning", "language": "Telugu", "print": 820},
    "9": {"title": "3 Idiots", "language": "Hindi", "print": 650},
    "10":{"title": "Interstellar", "language": "English", "print": 1000},
}

shows = {
    "1": ["10:00 AM", "02:00 PM", "06:00 PM", "10:00 PM"],
    "2": ["09:30 AM", "01:00 PM", "05:00 PM", "09:30 PM"],
    "3": ["11:00 AM", "03:00 PM", "07:00 PM", "11:00 PM"],
    "4": ["08:30 AM", "12:30 PM", "04:30 PM", "08:30 PM"],
    "5": ["10:15 AM", "01:45 PM", "05:15 PM", "09:15 PM"],
    "6": ["09:00 AM", "12:00 PM", "03:30 PM", "07:30 PM"],
    "7": ["11:30 AM", "02:30 PM", "06:30 PM", "10:30 PM"],
    "8": ["08:00 AM", "11:30 AM", "03:00 PM", "07:00 PM"],
    "9": ["10:45 AM", "02:15 PM", "05:45 PM", "09:45 PM"],
    "10": ["09:15 AM", "12:45 PM", "04:15 PM", "08:15 PM"],
}

ROWS = 8
COLS = 10

seat_maps = {}
for m_id in movies:
    seat_maps[m_id] = {}
    for show_time in shows[m_id]:
        seat_maps[m_id][show_time] = [["0" for _ in range(COLS)] for _ in range(ROWS)]


bookings = {}
booking_counter = 1000

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress Enter to continue....")

def print_header(title):
    clear_screen()
    print("=" * 55)
    print(f"{title.center(55)}")
    print("=" * 55)

def seat_label(row, col):
    return f"{chr(65 + row)}{col + 1}"

def print_seat_map(grid):
    print("\n       SCREEN THIS SIDE")
    print("     " + "-" * (COLS * 4))
    col_header = "      " + "".join(f"{c + 1:>4}" for c in range(COLS))
    print(col_header)
    for r in range(ROWS):
        row_str = f"{chr(65 + r):>2} |"
        for c in range(COLS):
            row_str +=f"{grid[r][c]:>4}"
        print(row_str)
    print("\nLegend: 0 = Avaiable X = Booked\n")

