# Programmer: Matthew Clifford
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
# Import Libraries Here
import random
from time import sleep


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


gas_level_alert()

