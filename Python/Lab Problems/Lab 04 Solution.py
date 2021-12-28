temp = float(input('What is the temperature in Farenheit? '))
humid = float(input('What is the humidity in percentage? '))
wind_speed = float(input('What is the wind speed in mph? '))
temp_forecast = ''
humid_desc = ''
wind_speed_forecast = ''

# Temperature Description
if temp < 32:
    temp_forecast = 'Very Cold'
elif temp <= 49:
    temp_forecast = 'Cold'
elif temp <= 64:
    temp_forecast = 'Cool'
elif temp <= 79:
    temp_forecast = 'Moderate'
elif temp <= 94:
    temp_forecast = 'Hot'
else:
    temp_forecast = 'Very Hot'

# Humidity Description

if humid < 45:
    humid_desc = 'Confortable'
elif humid <= 65:
    humid_desc = 'Muggy'
else:
    humid_desc = 'Opresssive'
    
# Wind Speed Description

if wind_speed < 1:
    wind_speed_forecast = 'Calm'
elif wind_speed <= 7:
    wind_speed_forecast = 'Light Breeze'
elif wind_speed <= 18:
    wind_speed_forecast = 'Moderate Breeze'
elif wind_speed <= 31:
    wind_speed_forecast = 'Strong Breeze'
elif wind_speed <= 46:
    wind_speed_forecast = 'Moderate Gale'
elif wind_speed <= 63:
    wind_speed_forecast = 'Strong Gale'
elif wind_speed <= 73:
    wind_speed_forecast = 'Strong Storm'
else:
    wind_speed_forecast = 'Hurricane'

#Using .format
print("Today's temperature of {:.2f} is {}, with a {} humidity of {:.2f}%, and a {}-force wind at {:.2f}mph.".format(temp, temp_forecast, humid_desc, humid, wind_speed_forecast, wind_speed))

#Using printf
print(f'Today\'s temperature of {temp:.2f} is {temp_forecast}, with a {humid_desc} humidity of {humid:.2f}%, and a {wind_speed_forecast}-force wind at {wind_speed:.2f}mph.')



    