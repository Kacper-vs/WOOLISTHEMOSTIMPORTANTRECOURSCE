import time,os,sys 

def typing_print(text,delay): 
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
        
def typing_input(text,delay): 
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    
def countdown_timer(seconds,color):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print( f"Time Remaining: {timer}", end="\r")
        time.sleep(1)
        seconds -= 1
        
