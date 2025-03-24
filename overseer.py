import argparse                  # HANDLE ARGUMENTS
import os                        # CLEARING OF SCREEN
import time                      # PAUSING EXEC, ETC
import sys                       # GRADIENT
import ctypes                    # ADMINISTRATOR REQUEST

from util.rename_win import rename_window
from util.clear_s import clear_screen

from modules.nmap_scanner import nmap_scanner
from modules.domain_search import domain_search

APP_VERSION = 1.0

def rgb_to_ansi(r, g, b):
    """Convert RGB to ANSI 24-bit escape code."""
    return f"\033[38;2;{r};{g};{b}m"

def gradient_text(text, start_color, end_color):
    """Apply a smooth gradient from start_color to end_color across text lines."""
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    lines = text.split("\n")
    gradient_ascii = ""

    for i, line in enumerate(lines):
        r = int(start_r + (end_r - start_r) * (i / max(1, len(lines) - 1)))
        g = int(start_g + (end_g - start_g) * (i / max(1, len(lines) - 1)))
        b = int(start_b + (end_b - start_b) * (i / max(1, len(lines) - 1)))

        gradient_ascii += rgb_to_ansi(r, g, b) + line + "\033[0m\n"

    return gradient_ascii

ASCII_ART = gradient_text(f'''

   ___   __   __   ___     ___     ___     ___     ___     ___   
  / _ \\  \\ \\ / /  | __|   | _ \\   / __|   | __|   | __|   | _ \\  
 | (_) |  \\ V /   | _|    |   /   \\__ \\   | _|    | _|    |   /  
  \\___/   _\\_/_   |___|   |_|_\\   |___/   |___|   |___|   |_|_\\  
_|"""""|_| """"|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 

   [1] username search
    |
    |______[2] domain lookup
            |
            |______[3] ip lookup
                    |
                    |______[4] nmap scanner
                            |
                            |______[5] phone num lookup
                                    |
                                    |______[6] darkweb search
                                            |
                                            |______[7] file metadata
                                                    |
                                                    |______[8] databreach lookup
                                                            |
                                                           [0] exit
''', (153, 0, 0), (255, 153, 102))
      # START COL  # END COL

def draw_menu():
    while True:
        clear_screen()
        print(ASCII_ART)
        choice = input("Mode => ").strip()

        match choice:
            case "1":
                clear_screen()
                pass
            case "2":
                clear_screen()
                web = input("Input website to search => ")
                domain_search(web)
            case "3":
                clear_screen()
                pass
            case "4":
                clear_screen()
                nmap_scanner()
            case "5":
                clear_screen()
                pass
            case "6":
                clear_screen()
                pass
            case "7":
                clear_screen()
                pass
            case "8":
                clear_screen()
                pass
            case "0":
                clear_screen()
                print("\n[!] Exiting Overseer Framework...\n")
                time.sleep(3)
                sys.exit(0)
            case _:
                clear_screen()
                print("\n[!] Invalid choice, please select a valid option.\n")
                time.sleep(1)

def main():
    rename_window("Overseer" + " V"+str(APP_VERSION))
    draw_menu()

if __name__ == "__main__":
    main()