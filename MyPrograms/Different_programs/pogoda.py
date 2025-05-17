from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

city = input('В каком городе Вас интересует погода?: ')

config_dict = get_default_config()                                    # перевод на русский
config_dict['language'] = 'ru'

owm = OWM('6c9f49e0216cfd05292f846f34a8d914')                         #видимость
mgr = owm.weather_manager()

obs = mgr.weather_at_place(city)                                     
visibility = obs.weather.visibility_distance
visibility_in_kms = obs.weather.visibility(unit='kilometers')



owm = OWM('6c9f49e0216cfd05292f846f34a8d914')                          #координаты
mgr = owm.geocoding_manager()


list_of_locations = mgr.geocode(city)
a_cor = list_of_locations[0]  
a_cor.lat #широта
a_cor.lon #долгота

owm = OWM('6c9f49e0216cfd05292f846f34a8d914')                           # погода
mgr = owm.weather_manager()


observation = mgr.weather_at_place(city)
w = observation.weather
temperature = w.temperature('celsius')['temp']

w.detailed_status         # 'clouds'
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain                    # {}
w.heat_index              # None
w.clouds                  # 75

print("В городе " + "сейчас температура " + str(temperature) + " по Цельсию.")
print("Также в этом городе " + str(w.detailed_status))
print("Влажность " + str(w.humidity) + ' %')
print(list_of_locations)
print("Видимость " + str(visibility_in_kms))