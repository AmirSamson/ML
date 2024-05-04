# this is for using the APIs and the API keys we got from "Openweathermap.org"
# we also are covering a situation where we do not have internet and a way to receive meaningful errors.
# the solution is to use " Try: and Expect: " functions. 

# how to install "requests" ?

import requests
import time

# try:
#     response = requests.get("https://api.openweathermap.org/data/2.5/weather?units=metric&lat=35.6764&lon=139.6500&appid=6443b6aa7b0bd1e006c4c9b950fc4100")

# except : 
#     print("Seems like you are out of internet  connections. :(")

# response_json = response.json()

# temp = response_json["main"]["temp"] # this will get the info on "main" key on the JSON response we got from the API. 
#                                      # since the JSON is actually a dictionary. And we use ["temp"] to get exactly the value for temperature.
# temp_min = response_json["main"]["temp_min"]
# temp_max = response_json["main"]["temp_max"]

# print(f"In Tehran, it is currently {temp} C.")
# print(f"And highest temperature will be {temp_max} C.")
# print(f"and the lowest temperature will be {temp_min} C.")

# ----------------------------------------------------------------------------------------------------------

#   to separate all the data and make it easier we can make classes for all the other Cities!

class City:
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):

        try:
             response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=6443b6aa7b0bd1e006c4c9b950fc4100")

        except : 
            print("Seems like you are out of internet  connections. :(")

        response_json = response.json()

        self.temp = response_json["main"]["temp"]          
        self.temp_min = response_json["main"]["temp_min"]
        self.temp_max = response_json["main"]["temp_max"]
    
    def temp_print(self):
        unit_symbol = "C"
        if self.units == "imperial":
            unit_symbol = "F"
        
        print("-----------------------------------------------------")
        print(f"In {self.name}, it is currently {self.temp}° {unit_symbol}.")
        print(f"And highest temperature will be {self.temp_max}° {unit_symbol}.")
        print(f"and the lowest temperature will be {self.temp_min}° {unit_symbol}.")
        print("------------------------------------------------------")


    # this is (`name`,    `lat`,    `lon` )
my_city = City("Tehran", 35.6764, 139.6500)
my_city.temp_print()

#### Now we can add other cities!!!!!

vacation_city = City("Dezful", 32.3840, 48.3996, "imperial")
vacation_city.temp_print()

Mosaferat = City("Shirez", 33.5332, 47.6066)
Mosaferat.temp_print()


Shahr = City("Oslo", 59.9139, 10.7522)
Shahr.temp_print()

time.sleep(30)