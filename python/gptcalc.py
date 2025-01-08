import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Continuous Calculator")

# Variable to store the current input and results
current_text = tk.StringVar(value="")  # Initializes the display with an empty string

# Variables to store the first operand and the current operator
first_value = None
operator = None

# Function to update the display with the clicked button's value
def append_to_display(value):
    current_text.set(current_text.get() + value)

# Function to store the first value and the operator when an operator is clicked
def set_operator(op):
    global first_value, operator
    if current_text.get():  # If there is something in the display
        if first_value is None:
            first_value = float(current_text.get())  # Set as the first value
        else:
            # Perform the current operation before updating the operator
            perform_calculation()

        operator = op  # Store the new operator
        current_text.set("")  # Clear the display for the next number

# Function to perform the calculation and display the result
def perform_calculation():
    global first_value, operator
    if operator and current_text.get():  # Check if an operator and second value are present
        second_value = float(current_text.get())
        
        # Perform the calculation based on the operator
        if operator == "+":
            first_value += second_value
        elif operator == "-":
            first_value -= second_value
        elif operator == "*":
            first_value *= second_value
        elif operator == "/":
            if second_value == 0:
                current_text.set("Error")  # Handle division by zero
                first_value = None
                operator = None
                return
            first_value /= second_value

        # Update display with result and reset the operator
        current_text.set(str(first_value))
        operator = None  # Reset the operator for further operations

# Function to clear the display and reset the calculator
def clear_display():
    global first_value, operator
    current_text.set("")
    first_value = None
    operator = None

# Create the display widget
display = tk.Entry(root, textvariable=current_text, font=("Arial", 24), justify="right", bd=10)
display.grid(row=0, column=0, columnspan=4)

# Define button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('pp', 4, 2), ('+', 4, 3)
]

# Add buttons to the GUI
for (text, row, col) in buttons:
    if text in '0123456789.':
        btn = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, 
                        command=lambda t=text: append_to_display(t))
    elif text == "=":
        btn = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, 
                        command=perform_calculation)
    else:
        btn = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, 
                        command=lambda op=text: set_operator(op))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Add a clear button
clear_button = tk.Button(root, text="C", font=("Arial", 18), width=5, height=2, command=clear_display)
clear_button.grid(row=4, column=2, padx=5, pady=5)

# Run the Tkinter main loop
root.mainloop()
