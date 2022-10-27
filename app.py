from flask import Flask
import time
from w1thermsensor import W1ThermSensor
app = Flask(__name__)

@app.route('/')
def display_temperature():
    sensor = W1ThermSensor()
    temperature = sensor.get_temperature(W1ThermSensor.DEGREES_C)
    high_temp = 0
    low_temp = 50

    if temperature > high_temp:
        high_temp = temperature

    if temperature < low_temp:
        low_temp = temperature
    
    return f'<h1>The current temperature is {temperature} degrees celcius</h1> \
    <br> <p>The highest temperature recorded so far is {high_temp}</p> \
    <p>The lowest temperature recorded so far is {low_temp}</p>'
    

if __name__ == "__main__":
    app.run(debug=True, port=80, host='0.0.0.0')