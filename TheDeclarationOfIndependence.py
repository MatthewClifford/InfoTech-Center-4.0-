import pygame

# Program: A radio with 3 stations for selecting different songs.

pygame.init()

# Back in black
back_in_black = pygame.mixer.Sound('06 Back in Black.mp3')
back_in_black.set_volume(0.3)

def classic_rock():
    print("You are listening to Classic Rock.")
    print("To change stations type 'Change'.")
    print("""
      Songs available:
      1. Back In Black
      2. Sweet Emotion
      3.
      """)


def backInBlack():
    while True:
        back_in_black.play(loops = 1)


def radio_condition():
    global radio_on_off
    radio_on_off = input("Would you like to access the radio? Type 'on' or 'off' > ")

    if radio_on_off == 'on':
        radio = True
        while radio == True:
            print("""
            Available stations:
            1. Classic Rock
            2. Classical
            3. Movie Themes
            """)


            station = input("Select a station to listen to! > ")

            if station == "Classic Rock":
               classic_rock()
               classic_rock_song_choice = input("Select a song! > ")

               if classic_rock_song_choice == 'Back In Black':
                 backInBlack()


radio_condition()

