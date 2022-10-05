import pyfiglet
import time
import datetime
from colorama import Fore, Style

####################
# Function Handeler

# To be added here

####################
# Variables

VERSION = "0.1.0.1"
TIME = datetime.datetime.now()
SLEEP_MIN = 0 #2
SLEEP_MAX = 0 #5

####################

def intro():

  print("Starting up CLI-Game..." + "\n")
  
  cligame_banner = pyfiglet.figlet_format("CLI-Game")
  
  time.sleep(SLEEP_MAX)
  
  print(Fore.BLUE + cligame_banner + Style.RESET_ALL)
  
  print("==============================")
  print("SPHS PTLW 2022-23 Comp Sci")
  print("Interactive Fiction Project" + "\n")
  print("Version " + VERSION + " Indev")
  print("Built", TIME, "UTC")
  print("==============================")
  
  time.sleep(SLEEP_MIN)
  
  print("\n" + "Please wait.." + "\n")
  
  time.sleep(SLEEP_MAX)

def rip():
  rip_banner = pyfiglet.figlet_format("You Died")
  print(Fore.RED + rip_banner + Style.RESET_ALL)

def troll():
  print( """
 ▄▄▄▄▄▄▄  ▄▄   ▄▄▄▄ ▄  ▄ ▄ ▄▄▄▄▄▄▄
 █ ▄▄▄ █ ▀  █ ▄▄█ ▄▀▄▄▄█▀  █ ▄▄▄ █
 █ ███ █ ▀ ▄ █▀▀▄ ▀ ▄▀▀▀ ▄ █ ███ █
 █▄▄▄▄▄█ █▀█ █▀▄▀█▀█▀█▀█ █ █▄▄▄▄▄█
 ▄ ▄▄ ▄▄▄██▄ ▄ ▄█▀▄█▄▄▀▄██▄▄▄ ▄ ▄ 
 ▄ ▄▀█ ▄   ▀▄▀█  ▀ ▄▀  █ ██▄ ▄ ▄ ▄
 ▀▀█▀█▄▄  █▄▀█▀▀██ ▄█ ▄▄▀█▀▀▀▄ ▄  
 █ ▄█ █▄▀█▄▄ ▀▄▀▀▄█▀▄ ▄▄█▄█▄▄▄█▀██
 █▀ ██ ▄▀█ ▀ █ █  ▄ ▄██▄  ▄ █▄▀▄▄█
 ▄▀▀▀▀█▄█  ▀▀ ▀▀▀▀ ▄▄ ▀██▄▄ █▄  ▀█
 ▀▄▀▀▀▄▄█▀▄█ █ ▄█▄▄ ▄ ███▄█  ▀▄▄█ 
 ▄▀ ██▄▄▀▀█▄▀ █ ███▀█▀▀▄▀▀▀██▄▀ ▀▀
 ▀██▄▀ ▄█▀▄▄██▄▀▄▄▀ ▄█▄▄█▄▄▄▄▄██ ▄
 ▄▄▄▄▄▄▄ ██▄▀▄██▄▄ ▀▀ ▄▄ █ ▄ █▄▀▄ 
 █ ▄▄▄ █ ▀▀█▄▀▄▀▄▄▀ ▀▀▀ ██▄▄▄█▄▄ ▄
 █ ███ █ █ ▄▀▀▀▄ ▀▀▄   ▄▀ ▀█ ▀ ▀ ▀
 █▄▄▄▄▄█ ▄█▄ ██▀▀▀ ████▄  ▄   ▀▄ ▀
  """)
def part_1():
  print("You wake up.. Somethings is wrong. It's almost as if the world is fading away.." + "\n")

  print("As you think that, you hear a strange noise.. Something's coming towards you")
  
  pt149_input = input("Would you like to run?" + "\n")

  if pt149_input == "yes" or pt149_input == "y":
    print("You chose yes. You are running towards the attic, and then you notice.. Somethings not right about yourself.." + "\n")
    
  elif pt149_input == "no" or pt149_input == "n":
    print("An unexplainable creature comes out of one of the attics storage boxes.. You see it, and suddenly, everything turns black and white.." + "\n")
    print("You blink and suddenly, you're in the endless, dark, cold void. There is no life here, in fact there's nothing." + "\n")
    print("You call for help... but nobody answered..")
    time.sleep(SLEEP_MIN)
    rip()
    exit(0)

  else:
    print(Fore.RED + "Error: type in y/yes or n/no" + Style.RESET_ALL)
    print("Check out this cool QR code!!")
    troll()

intro()
part_1()