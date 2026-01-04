import tkinter as tk

# Function to convert inches to centimeters
def convert_to_cm():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text=f"{inches} inches = {cm:.2f} cm")
    except ValueError:
        result_label.config(text="Please enter a valid number")

# Create main window
root = tk.Tk()
root.title("Inches to Centimeters Converter")
root.geometry("300x150")

# Label for instruction
instruction_label = tk.Label(root, text="Enter length in inches:")
instruction_label.pack(pady=5)

# Entry widget for user input
entry = tk.Entry(root)
entry.pack(pady=5)

# Button to trigger conversion
convert_button = tk.Button(root, text="Convert", command=convert_to_cm)
convert_button.pack(pady=5)

# Label to display result
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Run the application
root.mainloop()
