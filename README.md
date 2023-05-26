# aws
Automatic weather station using Raspberry pi 4 model B. Attached peripheral is bmp180, tipping bucket rain sensor and dht11.
![Schematic](https://github.com/abhijeetkan/aws/assets/62520532/5a0b1280-c815-48fa-933c-6c6f30140021)

Firstly, flash your Raspbian OS (32-bit) and update the raspberry pi.

Now, install dht library using "pip install dht11" in terminal editor

To use BMP180 for Atmospheric Pressure, Temperature and Altitude, i2c pins should be enabled from Raspberry pi configuration.
To check if raspberry pi is detecting BMP180, use the following commands in terminal window:
sudo i2cdetect -y 1
sudo i2cdetect -y 0
![pin diagram](https://github.com/abhijeetkan/aws/assets/62520532/07ff32b2-6ac5-4ff5-810e-05f75e86ed35)
