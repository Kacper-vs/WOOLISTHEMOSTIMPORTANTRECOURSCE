import time
import random as rand
# Import everything from your new helper file
from input import clear_screen, print_slow, get_valid_input

uni_random = rand.uniform(0.08, 0.10)

# Main game specific colors
RED = "\033[0;31m"
GREEN = "\033[0;32m"
LIGHT_RED = "\033[1;31m"
BOLD = "\033[1m" 

def official_starttothegame():
    time.sleep(1)
    print_slow("??? :", "ARE YOU WILLING TO BEGIN THIS EXPIDITION... (YES OR NO)", BOLD)
    
    # Using the input helper function from game_utils.py
    choice = get_valid_input("> ", ["YES", "NO"])
    
    clear_screen()
    if choice == "YES":
        print_slow("SYSTEM:", "The expedition has commenced...", GREEN)
    elif choice == "NO":
        print_slow("???:", "Then stay in the dark.", RED)

def main(timetoload):
    clear_screen()
    time.sleep(timetoload)
    print_slow("???:", "WeLcOmE tO ThE fLOWeR", RED)
    time.sleep(uni_random)
    print_slow("NARRATOR:", "FOR ANY CLUES FOLLOW TO www.theflowerdatabase.gg", LIGHT_RED)
    time.sleep(0.5)
    print_slow("???:", "Lets set a few house rules. You shall only awnser me in the terms [YES, NO] if not...", RED)
    print_slow("", "CoNsEqUeNcEs WiLl bE aPpLiEd.", RED)
    official_starttothegame()

main(0.08)
