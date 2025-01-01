import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Number Counter")

# Initialize a variable to hold the number
number = tk.IntVar(value=0)

# Define the event handlers for the buttons
def increment():
    number.set(number.get() + 1)

def decrement():
    number.set(number.get() - 1)

# Create and place a label to display the number
number_label = tk.Label(root, textvariable=number, font=("Helvetica", 24))
number_label.pack(pady=20)

# Create and place the "Up" button
up_button = tk.Button(root, text="Up", command=increment, width=10, bg="green", fg="white")
up_button.pack(side="left", padx=20, pady=20)

# Create and place the "Down" button
down_button = tk.Button(root, text="Down", command=decrement, width=10, bg="red", fg="white")
down_button.pack(side="right", padx=20, pady=20)

# Run the main loop
root.mainloop()
