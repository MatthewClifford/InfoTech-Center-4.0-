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

