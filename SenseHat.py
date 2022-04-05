###https://pythonhosted.org/sense-hat/api/
from sense_hat import SenseHat

sense = SenseHat()

## Humedad
humidity = sense.get_humidity()
temp = sense.get_temperature()
pressure = sense.get_pressure()

print("Pressure: %s Millibars" % pressure)
print("Humidity: %s %% H" % humidity)
print("Temperature: %s C" % temp)


