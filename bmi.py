
# Import necessary libraries
import tkinter as tk 
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi(weight, height):
    # Convert height from cm to m
    height_in_m = height / 100 
    # Calculate BMI using formula: weight / (height^2)
    return weight / (height_in_m ** 2)

# Function to classify BMI category
def classify_bmi(bmi):
    # Underweight: BMI < 18.5
    if bmi < 18.5: 
        return "Underweight"
    # Normal weight: 18.5 <= BMI < 24.9
    elif 18.5 <= bmi < 24.9: 
        return "Normal weight"
    # Overweight: 25 <= BMI < 29.9
    elif 25 <= bmi < 29.9: 
        return "Overweight"
    # Obesity: BMI >= 30
    else: 
        return "Obesity"

# Function to validate user input
def validate_input():
    # Get weight and height from input fields
    weight = weight_entry.get()
    height = height_entry.get()
    
    # Check if both fields are filled
    if not weight or not height:
        # Display error message if not filled
        messagebox.showerror("Input Error", "Please enter both weight and height.")
        return False
    
    # Check if input contains non-numeric characters
    if not weight.replace('.', '', 1).isdigit() or not height.isdigit():
        # Display error message if non-numeric
        messagebox.showerror("Input Error", "Weight and height must be numbers.")
        return False
    
    # Check if input values are positive
    if float(weight) <= 0 or int(height) <= 0:
        # Display error message if not positive
        messagebox.showerror("Input Error", "Weight and height must be positive numbers.")
        return False
    
    # Return True if input is valid
    return True

# Function to calculate and display BMI
def calculate():
    # Validate user input
    if validate_input():
        # Get weight and height from input fields
        weight = float(weight_entry.get())
        height = int(height_entry.get())
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        # Classify BMI category
        category = classify_bmi(bmi)
        
        # Display result
        result_label.config(text=f"Your BMI is: {bmi:.2f}\nCategory: {category}")

# Create main window
root = tk.Tk()
root.title("BMI Calculator")

# Create weight label and input field
tk.Label(root, text="Weight (kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

# Create height label and input field
tk.Label(root, text="Height (cm):").pack()
height_entry = tk.Entry(root)
height_entry.pack()

# Create calculate button
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate)
calculate_button.pack()

# Create result label
result_label = tk.Label(root, text="")
result_label.pack()

# Start main loop
root.mainloop()
