import win32com.client as win32
import config

def send_alert(humidity_value, temperature_value):
    import win32com.client as win32
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = config['mail_to']

    if temperature_value >= temperatureMax and humidity_value >= humidityMax:
        mail.Subject = '!!!#SENSOR-ALERT[Temperature and Humidity]!!!'
        mail.Body = 'Values too high for Temperature and Humidity!'
        mail.HTMLBody = f"""
                        <h2>Values too high for Temperature and Humidity!</h2>
                        <br>
                        <p>Temperature: {temperature_value}°C</p>
                        <p>Humidity: {humidity_value}%</p>
                        """
    elif temperature_value >= temperatureMax:
        mail.Subject = '!!!SENSOR-ALERT [Temperature]!!!'
        mail.Body = 'The value of Temperature is too high!'
        mail.HTMLBody = f"""
                <h2>Value too high for Temperature!</h2>
                <br>
                <p>Temperature: {temperature_value}°C</p>
                <p>Humidity: {humidity_value}%</p>
                """
    else:
        mail.Subject = '!!!SENSOR-ALERT[Humidity]!!!'
        mail.Body = 'The value of Humidity is too high!'
        mail.HTMLBody = f"""
                        <h2>Value too high for Humidity!</h2>
                        <br>
                        <p>Temperature: {temperature_value}°C</p>
                        <p>Humidity: {humidity_value}%</p>
                        """
    mail.Send()
    print("The alert has been sent by email!")


