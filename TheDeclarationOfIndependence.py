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


# Gas Level Function
def gas_level_gauge():
    gas_level_list = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    current_gas_level = random.choice(gas_level_list)
    return current_gas_level


print(gas_level_gauge())


def list_of_gas_stations():
   gas_stations = ["Shell", "Costco". "Buc-ee's", "Speed Way", "Circle-K", "Meijer", "Marathon"]
   gas_station_nearby = random.choice(gas_stations)
   print(gas_station_nearby)
   return gas_sation_nearby

   
