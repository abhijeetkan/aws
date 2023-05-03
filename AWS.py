import requests
import time
import RPi.GPIO as GPIO
from gpiozero import LED
from time import sleep
import dht11
from gpiozero import Button
import bmpsensor
import urllib.request

while True:
    time.sleep(5)
    try:
        urllib.request.urlopen('http://google.com')
        print("Connected to internet.")
        break
    except:
        print("No internet connection. Retryingin 5 seconds...")
        time.sleep(5)

write_key = 'KC17Q0YLO5JLWSC6'
THINGSPEAK_API_ENDPOINT = f"https://api.thingspeak.com/update?api_key={write_key}&field1=%s&field2=%s&field3=%s&field4=%s&field5=%s&field6=%s&field7=%s"
dht_pin = 14
BUCKET_SIZE = 0.2794 
rain_sensor = Button(6)
total_rainfall = 0
API_KEY = 'e965a98b20ac08f3fa45cf8b274badc0'

def bucket_tipped():
    global total_rainfall
    total_rainfall += BUCKET_SIZE

rain_sensor.when_pressed = bucket_tipped

def read_dht11():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    dht_sensor = dht11.DHT11(pin=dht_pin)
    result = dht_sensor.read()
    if result.is_valid():
        temperature = result.temperature
        humidity = result.humidity
        return temperature, humidity
    else:
        return None, None

def get_weather_data():
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=Rohru&appid={API_KEY}')
    data = response.json()
    wind_speed = data['wind']['speed']
    speed = wind_speed*3.6
    wind_direction = data['wind']['deg']
    return speed, wind_direction

while True:
    pressure, altitude = bmpsensor.readBmp180()
    rainfall = total_rainfall
    total_rainfall = 0
    temperature, humidity = read_dht11()
    if temperature is not None and humidity is not None:
        speed, wind_direction = get_weather_data()
        url = THINGSPEAK_API_ENDPOINT % (temperature, humidity, rainfall, speed, wind_direction, pressure, altitude)
        response = requests.get(url)
        try: #response.status_code == 200:
            print("Data sent to ThingSpeak")
        except:
            print("Failed to send data to ThingSpeak")
    time.sleep(15)
