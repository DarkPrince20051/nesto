import requests
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

def get_weather():
    user_input = entry.get()
    if not user_input:
        messagebox.showerror("Error", "Please enter a city.")
        return

    if user_input.isdigit():  # Provjera je li unos broj
        messagebox.showerror("Error", "Please enter a valid city name.")
        return

    api_key = '30d4741c779ba94c470ca1f63045390a'
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

    if weather_data.json().get('cod') == '404':
        messagebox.showerror("Error", "No City Found")
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        description = weather_data.json()['weather'][0]['description']
        humidity = weather_data.json()['main']['humidity']
        pressure = weather_data.json()['main']['pressure']
        try:
            rain = weather_data.json()['rain']['1h']
        except KeyError:
            rain = 'N/A'
        try:
            wind_speed_m_s = weather_data.json()['wind']['speed']
            wind_speed_km_h = round(wind_speed_m_s * 3.6, 2)  # Convert m/s to km/h
        except KeyError:
            wind_speed_km_h = 'N/A'

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        messagebox.showinfo("Current Weather", f"City: {user_input}\n"
                                                f"Date: {current_time}\n"
                                                f"Weather: {weather} ({description})\n"
                                                f"Temperature: {temp}°C\n"
                                                f"Humidity: {humidity}%\n"
                                                f"Pressure: {pressure} hPa\n"
                                                f"Wind Speed: {wind_speed_km_h} km/h")

def reset():
    entry.delete(0, tk.END)

def close():
    if messagebox.askquestion("Exit", "Do you want to exit?") == 'yes':
        root.destroy()

root = tk.Tk()
root.title("Weather App")
root.geometry("400x250")

label = tk.Label(root, text="Enter city:")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Get Current Weather", command=get_weather, width=20)
get_weather_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset", command=reset, width=15)
reset_button.pack(pady=5)

close_button = tk.Button(root, text="Close", command=close, width=15)
close_button.pack(pady=5)

root.mainloop()
