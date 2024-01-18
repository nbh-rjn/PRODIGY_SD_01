# PRODIGY_SD_TASK01
# NABIHA RAJANI
# TEMPERATURE CONVERSION PROGRAM

#import modules
import tkinter as tk
from tkinter import messagebox


def convert_temperature():
    try:
        # getting input values
        temperature_value = float(temperature_entry.get())
        selected_unit = unit_var.get()

        # applying range checks
        if selected_unit == "Celsius" and not (0 <= temperature_value <= 100):
            # celsius scale is from 0 to 100
            raise ValueError("Invalid input! Celsius temperature out of range.")
        elif selected_unit == "Kelvin" and not (0 < temperature_value <= 10**32):
            # 0 K is absolute zero, theoretical lowest possible temp
            # (10^32 K) is the highest known temp according to the standard model of particle physics
            raise ValueError("Invalid input! Kelvin temperature out of range.")
        elif selected_unit == "Fahrenheit" and not (32 <= temperature_value <= 212):
            # scale based on 32° for freezing and 212° for boiling point of water
            raise ValueError("Invalid input! Fahrenheit temperature out of range.")

        # conversions
        if selected_unit == "Celsius":
            converted_celsius = temperature_value
            converted_kelvin = temperature_value + 273.15
            converted_fahrenheit = (temperature_value * 9/5) + 32
        elif selected_unit == "Kelvin":
            converted_kelvin = temperature_value
            converted_celsius = temperature_value - 273.15
            converted_fahrenheit = (temperature_value - 273.15) * 9/5 + 32
        else:  # fahrenheit
            converted_fahrenheit = temperature_value
            converted_celsius = (temperature_value - 32) * 5/9
            converted_kelvin = (temperature_value - 32) * 5/9 + 273.15

        # displaying all results
        result_label.config(text=f" \n Celsius: {converted_celsius:.2f} °C \n"
                                 f" Kelvin: {converted_kelvin:.2f} °K \n"
                                 f" Fahrenheit: {converted_fahrenheit:.2f} °F")

    # error displayed if input temp is out of range
    except ValueError as e:
        messagebox.showerror("Error", str(e))


# creating window
root = tk.Tk()
root.title("Temperature Conversion")
root.geometry("400x300")

# entering temperature
tk.Label(root, text="Enter Temperature:").pack()
temperature_entry = tk.Entry(root)
temperature_entry.pack()

# selecting unit of measurement
unit_var = tk.StringVar()
unit_var.set("Celsius")  # set celsius as default
unit_options = ["Celsius", "Kelvin", "Fahrenheit"]
unit_menu = tk.OptionMenu(root, unit_var, *unit_options)
tk.Label(root, text="Select Unit: ").pack()
unit_menu.pack()

# convert button, the convert_temperature function is run when the button is clicked
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack()

# result label
result_label = tk.Label(root, text="")
result_label.pack()

# Run the Tkinter main loop
root.mainloop()
