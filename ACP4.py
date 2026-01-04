import tkinter as tk
from tkinter import messagebox

# Function to calculate SI and CI
def calculate_interest():
    try:
        # Get user inputs
        P = float(principal_entry.get())
        R = float(rate_entry.get())
        T = float(time_entry.get())
        
        # Calculate Simple Interest
        SI = (P * R * T) / 100
        
        # Calculate Compound Interest
        CI = P * ((1 + R/100) ** T) - P
        
        # Display results
        si_result_label.config(text=f"Simple Interest: {SI:.2f}")
        ci_result_label.config(text=f"Compound Interest: {CI:.2f}")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values!")

# Create main window
root = tk.Tk()
root.title("Interest Calculator App")
root.geometry("400x300")

# Principal amount
principal_label = tk.Label(root, text="Principal Amount:")
principal_label.pack(pady=5)
principal_entry = tk.Entry(root)
principal_entry.pack(pady=5)

# Rate of interest
rate_label = tk.Label(root, text="Rate of Interest (%):")
rate_label.pack(pady=5)
rate_entry = tk.Entry(root)
rate_entry.pack(pady=5)

# Time period
time_label = tk.Label(root, text="Time Period (years):")
time_label.pack(pady=5)
time_entry = tk.Entry(root)
time_entry.pack(pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate Interest", command=calculate_interest)
calculate_button.pack(pady=10)

# Labels to display results
si_result_label = tk.Label(root, text="")
si_result_label.pack(pady=5)
ci_result_label = tk.Label(root, text="")
ci_result_label.pack(pady=5)

# Run the application
root.mainloop()
