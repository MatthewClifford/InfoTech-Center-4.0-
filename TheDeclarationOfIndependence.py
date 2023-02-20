# Merged Welcome Screen and Gasoline Branches - Stable
# Programmer: Matthew Clifford
# Date: 1.20.23

# Program: InfoTech center upgrades

"""
Our Welcome Screen will start our program letting
drivers know that the InfoTech Center 4.0 OS is loading
"""

# Import Libraries Here
import time, sys, colorama, random
from time import sleep
import colorama
from colorama import Fore
# pygame
import pygame
from pygame import mixer

print(Fore.RED + "\n\nWelcome - InfoTech Center 4.0\n")
sleep(2)

x = 0
a = 0

while x != 9:
    x += 1
    b = (Fore.BLUE + "InfoTech Center 4.0 OS is Loading" + "." * a)
    a = a + 1
    # so `b` is printed on top of the previous line.
    sys.stdout.write('\r' + b)

    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 9:
        print(Fore.GREEN + '\n\nAccess Granted!\n')
        sleep(2)

# Date: 1.30.23
# Program: Infotech center 4.0 - Gasoline

"""
We will create a function that will tell us our Fuel Gage Level
   - Create a List with Gas Levels
   - Randomize a choice in the list to determine our gas level
Create a function to determine our closet Gas Station
   - Create a list of gas stations
   - Randomly choose a gas station from the list
Create a function to determine our gas level and closest gas station
   - print Gas Level
   - print Closest gas station
"""


# Gas Level Function
def gas_level_gauge():
    gas_level_list = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    current_gas_level = random.choice(gas_level_list)
    return current_gas_level


# Variable to calling gas level gauge function to store it's value
gas_level_indicator = gas_level_gauge()


# List of Gas Stations nearby
def list_of_gas_stations():
    gas_stations = ["Shell", "Costco", "Buc-ee's", "Speed Way", "Circle-K", "Meijer", "Marathon"]
    gas_station_nearby = random.choice(gas_stations)
    return gas_station_nearby


# Determine Gas Level & closest gas station
def gas_level_alert():
    miles_to_gas_station_low = round(random.uniform(1, 25), 2)
    miles_to_gas_station_quarter = round(random.uniform(26, 50), 2)

    if gas_level_indicator == "Empty":
        print("***\nWARNING YOU ARE ON EMPTY ***")
        sleep(1)
        print("\nCalling Emergency Contact")

    elif gas_level_indicator == "Low":
        print("\n***Warning***")
        sleep(1)
        print("\nGas tank is very low, checking Google Maps for the closest gas station.")
        sleep(1)
        print("\nThe closest gas station is", list_of_gas_stations(), "which is", miles_to_gas_station_low,
              "miles away")

    elif gas_level_indicator == "Quarter Tank":
        print("\n***Warning***")
        sleep(1)
        print("\nGas tank is only a quarter full and the closest gas station is", list_of_gas_stations(), "which is",
              miles_to_gas_station_quarter, "miles away.")

    elif gas_level_indicator == 'Half Tank':
        print("\nGas Tank is only Half Full. You have enough fuel to make it to your destination.")

    elif gas_level_indicator == "Three Quarter Tank":
        print("\nGas tank is Three Quarters Full. You have enough fuel to make it to your destination.")

    else:
        print("\nGas tank is Full. You have enough fuel to make it to your destination.")


# Programmer: Matthew Clifford
# Date: 2.8.23
# Program: Weather System Updates


# Create weather conditions in a list and choose it randomly
def weather():
    weather_forecast = ["Snowing", "Blizzard", "Rain", "Foggy", "Windy", "Icy", "Sunny"]
    weather_condition = random.choice(weather_forecast)
    return weather_condition


# Variable to call weather() once in our VRS)
weather_alert = weather()


# VRS() to respond to the weather condition
def vehicle_response_system():
    if weather_alert == "Snowing":
        print("\nNWS has changed your alarm by 15 minutes because of the weather forcast:", weather_alert + ".")
        print("\nVRS has been engaged only allowing your vehicle to go 45 MPH.")

    elif weather_alert == "Blizzard":
        print("\nNWS has changed your alarm by 30 minutes because of the weather forcast:", weather_alert + ".")
        print("\nVRS has been engaged only allowing your vehicle to go 35 MPH.")

    elif weather_alert == "Rain":
        print("\nNWS is calling for", weather_alert + ", please drive with caution.")

    elif weather_alert == "Foggy":
        print("\nNWS is calling for", weather_alert + " conditions, please drive with caution.")

    elif weather_alert == "Windy":
        print("\nNWS is calling for", weather_alert + " conditions, please drive with caution.")

    elif weather_alert == "Icy":
        print("\nNWS is calling for", weather_alert + " conditions, please drive with caution")
        print("\nVRS has been engaged only allowing your vehicle to go 25 MPH.")

    else:
        print("\nNWS is calling for some", weather_alert + "skies. Dirve salfely and have a wonderful day!")


# Checking NWS
sleep(2)

x = 0
a = 0

while x != 9:
    x += 1
    b = (Fore.BLUE + "Checking NWS for weather conditions" + "." * a)
    a = a + 1
    # so `b` is printed on top of the previous line.
    sys.stdout.write('\r' + b)

    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 9:
        vehicle_response_system()
        sleep(2)

# Checking Gas Level
sleep(2)

x = 0
a = 0

while x != 9:
    x += 1
    b = (Fore.BLUE + "Checking Current Gas Level" + "." * a)
    a = a + 1
    # so `b` is printed on top of the previous line.
    sys.stdout.write('\r' + b)

    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 9:
        gas_level_alert()
        sleep(2)

# Import Libraries Here
import pygame
from pygame import mixer

pygame.init()
mixer.init()

# Stop song
def stop_song():
    stop_song = input("> ")
    if stop_song == 'x':
        mixer.music.pause()

# SONGS GO HERE

# Movie Themes
def jurassic_park():
    mixer.music.load("Jurassic Park theme song..ogg")
    mixer.music.set_volume(1)
    mixer.music.play()
    stop_song()

def indiana_jones():
    mixer.music.load("indiana-jones-theme-song.mp3")
    mixer.music.set_volume(1)
    mixer.music.play()
    stop_song()

def star_wars():
    mixer.music.load("Star Wars Theme Song By John Williams.ogg")
    mixer.music.set_volume(1)
    mixer.music.play()
    stop_song()

def pirates():
    mixer.music.load("Pirates of the Caribbean - Hes a Pirate.ogg")
    mixer.music.set_volume(1)
    mixer.music.play()
    stop_song()

# Classic Rock songs GO HERE
def back_in_back():
    mixer.music.load("06 Back in Black.mp3")
    mixer.music.set_volume(1)
    mixer.music.play()
    stop_song()

def more_than_a_feeling():
    mixer.music.load("More Than A Feeling.ogg")
    mixer.music.set_volume(1)
    mixer.music.play()
    stop_song()

def thunderstruck():
    mixer.music.load("ACDC  Thunderstruck.mp3")
    mixer.music.set_volume(1)
    mixer.music.play()
    stop_song()

def whole_lotta_love():
    mixer.music.load("wholeLottaLove.ogg")
    mixer.music.set_volume(1)
    mixer.music.play()
    stop_song()

# Classical Songs GO HERE

def fur_elise():
    mixer.music.load("Fur Elise.mp3")
    mixer.music.set_volume(1)
    mixer.music.play()
    stop_song()

def moonlight_sonata():
    mixer.music.load("Pinao Sonata.mp3")
    mixer.music.set_volume(1)
    mixer.music.play()
    stop_song()

def fith_symphony():
    mixer.music.load("Beethoven - 5th Symphony.mp3")
    mixer.music.set_volume(1)
    mixer.music.play()
    stop_song()

def radio_condition():
    global on_or_off
    on_or_off = input("Would you like to access the radio? Type 'on' or 'off'. > ")


def classic_rock():
    print("\nYou are listening to Classic Rock.")
    print("""
  Songs Available:
  1. Back In Black
  2. More Than a Feeling
  3. Whole Lotta Love 
  4. Thunderstruck
  
  Hit the 'x' key and enter to stop the song...
  """)


def classical():
    print("\nYou are now listening to Classical Music.")
    print("""
  Songs Available:
  1. Fur Elise
  2. Moonlight Sonata
  3. Beethoven's 5th 
  
  Hit the 'x' key and enter to stop the song...
  """)


def movie_themes():
    print("You are now Listening to Movie Themes.")
    print("""
  Songs Available;
  1. Jurassic Park
  2. Star Wars
  3. Indiana Jones
  4. Pirates of the Caribbean
  5. Marvel
  6. Harry Potter
  
  Hit the 'x' key and enter to stop the song...
  """)


def station_select_function():
    global station_select
    print("""
  Stations Available:
    1. Classic Rock
    2. Classical
    3. Movie Themes
    """)
    station_select = input("Select a Station to listen to! > ")


radio_condition()

# RADIO ON
if on_or_off == 'on':
    radio = True
    while radio == True:
        station_select_function()

        # Classic Rock
        if station_select.lower() == 'classic rock':
            classic_rock()
            classic_rock_song_choice = input("select a song. > ")

            if classic_rock_song_choice.lower() == 'back in black':
                back_in_back()

            elif classic_rock_song_choice.lower() == 'more than a feeling':
                more_than_a_feeling()

            elif classic_rock_song_choice.lower() == "whole lotta love":
                whole_lotta_love()

            elif classic_rock_song_choice.lower() == "thunderstruck":
                thunderstruck()

            else:
                print("\nNot An Option")
                break
        # Classical
        elif station_select.lower() == "classical":
            classical()
            classical_song_choice = input("Select a song. > ")

            if classical_song_choice.lower() == 'fur elise':
                fur_elise()

            if classical_song_choice.lower() == 'moonlight sonata':
                moonlight_sonata()

            if classical_song_choice.lower() == "beethoven's 5th":
                fith_symphony()

        # Movie Themes
        elif station_select.lower() == "movie themes":
            movie_themes()
            movie_theme_song_choice = input("Select a song. > ")

            if movie_theme_song_choice.lower() == "jurassic park":
                jurassic_park()

            elif movie_theme_song_choice.lower() == "indiana jones":
                indiana_jones()

            elif movie_theme_song_choice.lower() == 'star wars':
                star_wars()

            elif movie_theme_song_choice.lower() == 'pirates of the caribbean':
                pirates()

