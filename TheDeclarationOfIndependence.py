# Programmer: Matthew Clifford
# Date: 2.8.23
# Program: Weather System Updates

# Import Libraries here
import random


# Create weather conditions in a list and choose it randomly
def weather():
    weather_forecast = ["Snowing", "Blizzard", "Rain", "Foggy", "Windy", "Icy", "Sunny"]
    weather_condition = random.choice(weather_forecast)
    return weather_condition


# Variable to call weather() once in our VRS)
weather_alert = weather()


# VRS() to respond to the weather condition
def vehichle_response_system():
    if weather_alert == "Snowing":
        print("\nNWS has changed your alarm by 15 minutes because of the weather forcast the", weather_alert + ".")
        print("VRS has been engaged only allowing your vehicle to go 45 MPH.")

    elif weather_alert == "Blizzard":
        print("\nNWS has changed your alarm by 30 minutes because of the weather forcast the", weather_alert + ".")
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


vehichle_response_system()
