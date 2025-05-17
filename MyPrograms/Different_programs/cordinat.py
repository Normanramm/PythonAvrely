from pyowm.owm import OWM

city = input('Координаты какого города Вам нужны?: ')

owm = OWM('6c9f49e0216cfd05292f846f34a8d914')
mgr = owm.geocoding_manager()


list_of_locations = mgr.geocode(city)
a_cor = list_of_locations[0]  
a_cor.lat
a_cor.lon 

print(list_of_locations)