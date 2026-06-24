import sys
import time
import cmd
import random as rand 

uni_random = rand.uniform(0.10,0.08)

BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"

def print_slow(prefix, text, color_code):
    full_text = f"{prefix} {text}"
    sys.stdout.write(color_code)
    for char in full_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print("\033[0m")
    
def official_starttothegame():
    print_slow("??? : ", "ARE YOU WILLING TO BEGIN THIS EXPIDITION... (YES OR NO)",)


    
def main(timetoload):
    time.sleep(timetoload)
    print_slow("???: " , "WeLcOmE tO ThE fLOWeR" , RED )
    time.sleep(uni_random)
    print_slow("NARRATOR: " , "FOR ANY CLUES FOLLOW TO www.theflowerdatabase.gg" , LIGHT_RED)
    time.sleep(0.5)
    print_slow("???: " , "Lets set a few house rules. You shall only awnser me in the terms [YES, NO] if not..." , RED )
    print_slow("" , "CoNsEqUeNcEs WiLl bE aPpLiEd." , RED )
    time.sleep(200)
    official_starttothegame()
    
    
main(0.08)