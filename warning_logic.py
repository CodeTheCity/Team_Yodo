import requests
import time

class ConditionsWarning():

    cold = 15 # defined by RNLI
    blowy = 10*1000/(60*60)
    gale = 40*1000/(60*60)

    def __init__(self, lat, long, weather_api, tide_station):
        self.lat = lat
        self.long = long
        self.wapi = weather_api
        self.station_code = tide_station
        self.weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.long}&appid={self.wapi}&units=metric"
        self.tide_url = f"http://environment.data.gov.uk/flood-monitoring/id/stations/{self.station_code}"
        self.tide_history_url = None
        self.last_tide = 2.137
        self.previous_tide_risk = 0
        self.high = 2.5 # We need a general way to generate this from an arbitrary location
        self.risk_level = {0:"low", 1:"medium", 2:"high", 3:"very high"}

    def get_weather(self):
        response = requests.get(self.weather_url)
        if response.status_code == 200:
            weather_data = response.json()
            return weather_data['main']['temp'], weather_data['wind']['speed']
        else:
            print(f"Error fetching tide data: {response.status_code}.")
            return None

    def get_tide(self):
        response = requests.get(self.tide_url)
        if response.status_code == 200:
            tide_data = response.json()
            tide_level = tide_data["items"]["measures"]['latestReading']['value']
            return tide_level
        else:
            print(f"Error fetching tide data: {response.status_code}.")
            return None
        
    def get_tide_previous(self):
        pass
      
    def get_risk_level(self):
        depth = self.get_tide()
        temp, wind_speed = self.get_weather()
        return self.risk_function(depth, temp, wind_speed)
    
    def temp_risk(self, temp):
        if temp > 15:
            return 0
        elif temp < 1:
            return 1
        else:
            return 1/temp

    def tide_risk(self, tide_diff):
        if tide_diff < 0.01:
            return 1
        else:
            return 0.01*(1/tide_diff)

    def wind_risk(self, wind_speed):
        if wind_speed < ConditionsWarning.blowy:
            return 0
        elif wind_speed > ConditionsWarning.gale:
            return 1
        else:
            return ((wind_speed - ConditionsWarning.blowy)/(ConditionsWarning.gale-ConditionsWarning.blowy))**2
        

    def risk_function(self, depth, temp, wind_speed):
        score = 0
        score += self.wind_risk(wind_speed)*0.5
        score += self.temp_risk(temp)*0.3
        score += self.tide_risk(abs(2.379-2.137))
        return score
        

if __name__ == "__main__":
    sample_time = 600
    iterations = 4
    lat, long = 57.0837, 2.0553
    weather_api = "02fadf78366ed16f7e79f0bf27ed4ba0"
    tide_station = "E70724"
    warning_system = ConditionsWarning(lat, long, weather_api, tide_station)
    index = 1
    while True:
        risk_factor = warning_system.get_risk_level()
        print("Risk factor:", risk_factor)
        time.sleep(sample_time)
        index += 1
        if index > iterations:
            break