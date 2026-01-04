import tkinter as tk
from tkinter import messagebox

# Function to check password strength
def check_strength():
    password = password_entry.get()
    
    if len(password) == 0:
        messagebox.showwarning("Input Error", "Please enter a password!")
        strength_label.config(text="")
    elif len(password) < 6:
        strength_label.config(text="Password Strength: Weak", fg="red")
    elif 6 <= len(password) < 10:
        strength_label.config(text="Password Strength: Medium", fg="orange")
    else:
        strength_label.config(text="Password Strength: Strong", fg="green")

# Create main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")

# Label and Entry for password
password_label = tk.Label(root, text="Enter Password:")
password_label.pack(pady=10)

password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Button to check strength
check_button = tk.Button(root, text="Check Strength", command=check_strength)
check_button.pack(pady=10)

# Label to display strength
strength_label = tk.Label(root, text="", font=("Helvetica", 12))
strength_label.pack(pady=10)

# Run the application
root.mainloop()
