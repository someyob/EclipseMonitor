"""
Eclipse watcher
"""
from machine import Pin, ADC
import network
import time
from umqtt.simple import MQTTClient

# Fill in your WiFi network name (ssid) and password here:
wifi_ssid = "MySSID"
wifi_password = "MySuperSecurePassword"

led = Pin("LED", machine.Pin.OUT)

led.on()
time.sleep(0.5)
led.off()
time.sleep(0.1)
led.on()
time.sleep(0.5)
led.off()

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi_ssid, wifi_password)
while wlan.isconnected() == False:
    print('Waiting for connection...')
    time.sleep(1)
print("Connected to WiFi")

mqtt_host = "xxx.xxx.xxx.xxx"
mqtt_username = ""  
mqtt_password = ""  
mqtt_publish_topic = "Wx2/insolation"

mqtt_client_id = "solareclipse"

mqtt_client = MQTTClient(
        client_id=mqtt_client_id,
        server=mqtt_host,
        user=mqtt_username,
        password=mqtt_password)

mqtt_client.connect()

solar = ADC(Pin(26))

led.on()
time.sleep(0.5)
led.off()
time.sleep(0.1)
led.on()
time.sleep(0.5)
led.off()

counter = 60
average = 0.0
try:
    while True:
        for counter in range(10):
            insolation = solar.read_u16()
            print(f'{counter:d} Voltage= {insolation:d}')
            time.sleep(1)
            average += insolation/6553.0
        average /= 10.0
        mqtt_client.publish(mqtt_publish_topic, str(average))
        average = 0.0

except Exception as e:
    print(f'Failed to publish message: {e}')
finally:
    mqtt_client.disconnect()

