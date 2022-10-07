import pyfiglet
import time
import datetime
from colorama import Fore, Style

####################

# Variables

VERSION = "0.1.0.1"
TIME = datetime.datetime.now()
SLEEP_MIN = 2 #0
SLEEP_MAX = 5 #0

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
    print("You chose yes. You decide to go and run, and then you notice.. Somethings not right.." + "\n")
    part_2()
    
  elif pt149_input == "no" or pt149_input == "n":
    print("An unexplainable creature comes out of nowhere.. You see it, and suddenly, everything turns black and white.." + "\n")
    print("You blink and suddenly, you're in the endless, dark, cold void. There is no life here, in fact there's nothing." + "\n")
    print("You call for help... but nobody answered..")
    time.sleep(SLEEP_MIN)
    rip()
    exit(0)

  else:
    print(Fore.RED + "Error: type in y/yes or n/no" + Style.RESET_ALL)
    print("Check out this cool QR code!!")
    troll()

def part_2():
  print("There seems to be a strange portal in the street of your home.." + "\n")
  print("Oh and everything is black and white around you. The grass, the sky, your neighbors house, and even yourself.." + "\n")

  portal_input = input("Would you like to jump into the portal?" + "\n")

  if portal_input == "yes" or portal_input == "y":
    print("You get transported to the fourth dimension and well.. your human brain cannot possibly comprehend what your looking at so you instantly die. :(")
    rip()
    exit(0)

  elif portal_input == "no" or portal_input == "n":
    print("...")
    time.sleep(SLEEP_MIN)
    print("....")
    time.sleep(SLEEP_MIN)
    print("A godly being comes from the sky and saves your life. You then get back to your normal life :D")
    print("Everything is well and great, or is it?")
    end()

def end():
  end_banner = pyfiglet.figlet_format("The End")
  print(Fore.GREEN + end_banner + Style.RESET_ALL)

intro()
part_1()
