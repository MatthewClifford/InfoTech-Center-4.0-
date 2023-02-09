# Programmer: Matthew Clifford
# Date: 2.8.23
# Program: Weather System Updates

# Import Libraries here
import random


# Create weather conditions in a list and choose it randomly
def weather():
    weather_forecast = ["Snowing", "Blizzard", "Raining", "Foggy", "Windy", "Icy", "Sunny"]
    weather_condition = random.choice(weather_forecast)
    return weather_condition


# Variable to call weather() once in our VRS)
weather_alert = weather()

print(weather_alert)

# VRS() to respond to the weather condition
def vehichle_response_system():
    print("Hello")
