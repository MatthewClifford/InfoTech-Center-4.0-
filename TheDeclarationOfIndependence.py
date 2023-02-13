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


print(Fore.RED + "\n\nWelcome - InfoTech Center 4.0\n")
sleep(2)

x = 0
a = 0

while x != 9:
    x += 1
    b = (Fore.BLUE + "InfoTech Center 4.0 OS is Loading" + "." * a)
    a = a + 1
# so `b` is printed on top of the previous line.
    sys.stdout.write('\r'+b)

    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 20:
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
        print("***WARNING YOU ARE ON EMPTY ***")
        sleep(1)
        print("Calling Emergency Contact")

    elif gas_level_indicator == "Low":
        print("***Warning***")
        sleep(1)
        print("Gas tank is very low, checking Google Maps for the closest gas station.")
        sleep(1)
        print("The closest gas station is", list_of_gas_stations(), "which is", miles_to_gas_station_low, "miles away")
        
    elif gas_level_indicator == "Quarter Tank":
        print("***Warning***")
        sleep(1)
        print("Gas tank is only a quarter full and the closest gas station is", list_of_gas_stations(), "which is", miles_to_gas_station_quarter, "miles away.")

    elif gas_level_indicator == 'Half Tank':
        print("Gas Tank is only Half Full. You have enough fuel to make it to your destination.")

    elif gas_level_indicator == "Three Quarter Tank":
        print("Gas tank is Three Quarters Full. You have enough fuel to make it to your destination.")

    else:
        print("Gas tank is Full. You have enough fuel to make it to your destination.")



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
        print("VRS has been engaged only allowing your vehicle to go 45 MPH.")

    elif weather_alert == "Blizzard":
        print("\nNWS has changed your alarm by 30 minutes because of the weather forcast:", weather_alert + ".")
        print("VRS has been engaged only allowing your vehicle to go 35 MPH.")

    elif weather_alert == "Rain":
        print("\nNWS is calling for", weather_alert + ", please drive with caution.")

    elif weather_alert == "Foggy":
        print("\nNWS is calling for", weather_alert + "conditions, please drive with caution.")

    elif weather_alert == "Windy":
        print("\nNWS is calling for", weather_alert + "conditions, please drive with caution.")

    elif weather_alert == "Icy":
        print("\nNWS is calling for", weather_alert + "conditions, please drive with caution")
        print("VRS has been engaged only allowing your vehicle to go 25 MPH.")

    else:
        print("\nNWS is calling for some", weather_alert + "skies. Dirve salfely and have a wonderful day!")


# Call Function Here

vehicle_response_system()
gas_level_alert()


