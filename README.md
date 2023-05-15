# aws
Automatic weather station using Raspberry pi 4 model B. Attached peripheral is bmp180, rain gauge and dht11.

Firstly, flash your Raspbian OS (32-bit) and update the raspberry pi.

Now, install dht library using "pip install dht11"

To use BMP180 for Atmospheric Pressure, Temperature and Altitude, i2c pins should be enabled from Raspberry pi configuration.
To check if raspberry pi is detecting BMP180, use the following commands in terminal window:
sudo i2cdetect -y 1
sudo i2cdetect -y 0
