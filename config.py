config{
	mail_to : "mail alert to" #The mail where you want to send mail alert
	thingspeak_api_key : "your api here" #yout api from https://thingspeak.com/
	arduino_uno_port : "your arduino port here"  #Ex: COM1, com2 etc. 
}
#ON/OFF - for Arduino Uno pins 
ON = 1
OFF = 0

#RGB led for temperature pins: Red = 5 | Geen = pin 6 | Blue = pin 7
T_LedPin_R = 5
T_LedPin_G = 6
T_LedPin_B = 7

#RGB led for humidity  pins: Red = pin 8 | Geen = pin 9 | Blue = pin 10
H_LedPin_R = 8
H_LedPin_G = 9
H_LedPin_B = 10

#Buzzer sensor pin : 11
BuzzerPin = 11

#Temperature values
temperatureMed = 26.5	# The med value of temperature
temperatureMax = 30	# The max value of temperature

#Humidity values
humidityMed = 70	# The med value of humidity
humidityMax = 90	# The max value of humidity
