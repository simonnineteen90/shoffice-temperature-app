from flask import Flask
import time
from w1thermsensor import W1THermSensor
app = Flask(__name__)

@app.route('/')
def display_temperature():
    sensor = W1THermSensor()
    if sensor:
        temperature = sensor.get_temperature(W1THermSensor.Degrees_C)
        return f'<h1>The current temperature is {temperature} degrees celcius</h1>'
    else:
        return "Sensor is not available"

if __name__ == "__main__":
    app.run(debug=True, port=80, host='0.0.0.0')