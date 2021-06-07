import serial
import time
import pyfirmata
import requests
import mail
import config


def sensor_func():
    global my_senzor_list
    arduino = serial.Serial(config[arduino_uno_port], 57600)
    print('Established serial connection to Arduino')
    arduino_data = arduino.readline()
    arduino_data = arduino_data[46:(len(arduino_data)-2)]
    decoded_values = str(arduino_data.decode("utf-8"))
    list_values = decoded_values.split('x')

    for item in list_values:
        list_in_floats.append(float(item))
    humidity_value = list_in_floats[0]
    temperature_value = list_in_floats[1]
    print(f'Humidity: {humidity_value}%')
    print(f'Temperature: {temperature_value}°C')

    try:
        my_link = "https://api.thingspeak.com/update?api_key=" + config[thingspeak_api_key] + "&field1=" + str(humidity_value) + "&field2=" + str(temperature_value)
        requests.get(my_link)
    except:
        print("The connection to api.thingspeak is lost!")
    arduino_data = 0
    my_sensor_list = list_in_floats.copy()
    list_in_floats.clear()
    list_values.clear()
    arduino.close()
    print('Connection closed')
    print('<----------------------------->')
    return my_senzor_list

def check_semnal(humidity_value, temperature_value):
    board = pyfirmata.Arduino(config[arduino_uno_port])
    it = pyfirmata.util.Iterator(board)
    it.start()
    if temperature_value >= temperatureMax:
        board.digital[BuzzerPin].write(ON)
        board.digital[T_LedPin_R].write(ON)
        board.digital[T_LedPin_G].write(OFF)
        board.digital[T_LedPin_B].write(OFF)
        print("The Value of temperature is too high!")
        mail.send_alert(humidity_value, temperature_value)

    elif temperature_value >= temperatureMed:
        board.digital[T_LedPin_R].write(ON)
        board.digital[T_LedPin_G].write(OFF)
        board.digital[T_LedPin_B].write(ON)

    else:
        board.digital[T_LedPin_R].write(OFF)
        board.digital[T_LedPin_G].write(ON)
        board.digital[T_LedPin_B].write(OFF)

    if humidity_value >= humidityMax:
        board.digital[BuzzerPin].write(ON)
        board.digital[H_LedPin_R].write(ON)
        board.digital[H_LedPin_G].write(OFF)
        board.digital[H_LedPin_B].write(OFF)
        print("The Value of humidity is too high!")
        mail.send_alert(humidity_value, temperature_value)
    elif humidity_value >= humidityMed:
        board.digital[H_LedPin_R].write(ON)
        board.digital[H_LedPin_G].write(OFF)
        board.digital[H_LedPin_B].write(ON)
    else:
        board.digital[H_LedPin_R].write(OFF)
        board.digital[H_LedPin_G].write(ON)
        board.digital[H_LedPin_B].write(OFF)

    time.sleep(2)
    board.exit()

# ----------------------------------------Main Code------------------------------------
print('Program started')
while True:
    sensori_DHT = sensor_func()
    humidity_value = sensori_DHT[0]
    temperature_value = sensori_DHT[1]
    check_semnal(humidity_value,temperature_value)
    time.sleep(1)
    my_senzor_list.clear()