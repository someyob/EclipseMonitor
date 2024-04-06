Just for a lark, wanted to grab some data regarding the April 8 2024 solar eclipse, which will only be partial in my area.

The device reads the voltage generated by a nominal 6v photovoltaic solar cell (with a resistor divider),
10 readings, once a second, averages those and sends them out to my MQTT broker. 

I have a raspberry pi that subcribes to that topic, and logs the readings to a file for graphing purposes.

The numbers are not calibrated to anything meaningful, it's just showing relative strength of the light hitting the cell.
