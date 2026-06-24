import os
import sys
import time

BOLD = "\033[1m"
RED = "\033[0;31m"
END = "\033[0m"

def clear_screen():
    """Clears the terminal screen entirely."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(prefix, text, color_code):
    """Prints text character by character."""
    full_text = f"{prefix} {text}" if prefix else text
    sys.stdout.write(color_code)
    for char in full_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print("\033[0m") 

def get_valid_input(prompt, valid_choices):
    """Forces the user to type a valid answer or triggers consequences."""
    while True:
        user_choice = input(f"{BOLD}{prompt}{END} ").strip().upper()
        
        if user_choice in valid_choices:
            return user_choice
        
        clear_screen()
        print_slow("???:", "INVALID ANSWER. PAY ATTENTION TO THE RULES.", RED)
        time.sleep(1)