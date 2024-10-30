import requests
import json
from datetime import datetime
from tkinter import *

# Initialize Window
root = Tk()
root.geometry("400x400")  # Size of the window by default
root.resizable(0, 0)  # To make the window size fixed
root.title("Weather App")

# Function to fetch and display weather info
city_value = StringVar()

def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.strftime('%H:%M:%S')

def showWeather():
    api_key = "YOUR_API_KEY"  # Replace with your actual OpenWeatherMap API key
    city_name = city_value.get()

    # API URL
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

    # Get the response from the fetched URL
    try:
        response = requests.get(weather_url)
        weather_info = response.json()

        tfield.delete("1.0", "end")  # Clear the text field for new output

        if weather_info['cod'] == 200:
            kelvin = 273.15  # Value of kelvin
            # Storing the fetched values of weather of a city
            temp = int(weather_info['main']['temp'] - kelvin)
            feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
            pressure = weather_info['main']['pressure']
            humidity = weather_info['main']['humidity']
            wind_speed = weather_info['wind']['speed'] * 3.6  # Convert to km/h
            sunrise = weather_info['sys']['sunrise']
            sunset = weather_info['sys']['sunset']
            timezone = weather_info['timezone']
            cloudy = weather_info['clouds']['all']
            description = weather_info['weather'][0]['description']

            sunrise_time = time_format_for_location(sunrise + timezone)
            sunset_time = time_format_for_location(sunset + timezone)

            # Assigning values to display as output
            weather = (f"\nWeather of: {city_name}\n"
                       f"Temperature (Celsius): {temp}°\n"
                       f"Feels like (Celsius): {feels_like_temp}°\n"
                       f"Pressure: {pressure} hPa\n"
                       f"Humidity: {humidity}%\n"
                       f"Sunrise at {sunrise_time} and Sunset at {sunset_time}\n"
                       f"Cloud: {cloudy}%\n"
                       f"Info: {description.capitalize()}")
        else:
            weather = f"\n\tWeather for '{city_name}' not found!\n\tPlease enter a valid city name!"
    except requests.exceptions.RequestException as e:
        weather = "\n\tError fetching data! Please check your internet connection."
    except Exception as e:
        weather = "\n\tAn unexpected error occurred."

    tfield.insert(INSERT, weather)  # Display output in the Text Field

# Frontend part of the code - Interface
city_head = Label(root, text='Enter City Name', font='Arial 12 bold').pack(pady=10)
inp_city = Entry(root, textvariable=city_value, width=24, font='Arial 14 bold').pack()

Button(root, command=showWeather, text="Check Weather", font="Arial 10", bg='lightblue', fg='black',
       activebackground="teal", padx=5, pady=5).pack(pady=20)

# To show output
weather_now = Label(root, text="The Weather is:", font='Arial 12 bold').pack(pady=10)
tfield = Text(root, width=46, height=10)
tfield.pack()

root.mainloop()
