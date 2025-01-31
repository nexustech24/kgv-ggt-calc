import tkinter as tk
from tkinter import ttk
from math import gcd

# Function to calculate kgV
def calculate_kgv():
    try:
        num1 = int(entry_kgv1.get())
        num2 = int(entry_kgv2.get())
        
        if num1 == 0 or num2 == 0:
            result_kgv_label.config(text="Please enter non-zero numbers.")
            multiples_kgv_label.config(text="")
            return
        
        # Calculate kgV
        lcm = abs(num1 * num2) // gcd(num1, num2)
        result_kgv_label.config(text=f"The smallest common multiple (kgV) is: {lcm}")
        
        # Generate multiples
        multiples1 = [num1 * i for i in range(1, (lcm // num1) + 1)]
        multiples2 = [num2 * i for i in range(1, (lcm // num2) + 1)]
        
        # Highlight the smallest common multiple
        multiples_text = f"Multiples of {num1}: {', '.join(map(str, multiples1))}\n"
        multiples_text += f"Multiples of {num2}: {', '.join(map(str, multiples2))}\n"
        multiples_text += f"Smallest Common Multiple: {lcm}"
        
        multiples_kgv_label.config(text=multiples_text)
    except ValueError:
        result_kgv_label.config(text="Please enter valid integers.")
        multiples_kgv_label.config(text="")

# Function to calculate ggT
def calculate_ggt():
    try:
        num1 = int(entry_ggt1.get())
        num2 = int(entry_ggt2.get())
        
        if num1 == 0 or num2 == 0:
            result_ggt_label.config(text="Please enter non-zero numbers.")
            divisors_ggt_label.config(text="")
            return
        
        # Calculate ggT
        ggt_value = gcd(num1, num2)
        result_ggt_label.config(text=f"The greatest common divisor (ggT) is: {ggt_value}")
        
        # Generate divisors
        divisors1 = [i for i in range(1, num1 + 1) if num1 % i == 0]
        divisors2 = [i for i in range(1, num2 + 1) if num2 % i == 0]
        
        # Highlight the greatest common divisor
        divisors_text = f"Divisors of {num1}: {', '.join(map(str, divisors1))}\n"
        divisors_text += f"Divisors of {num2}: {', '.join(map(str, divisors2))}\n"
        divisors_text += f"Greatest Common Divisor: {ggt_value}"
        
        divisors_ggt_label.config(text=divisors_text)
    except ValueError:
        result_ggt_label.config(text="Please enter valid integers.")
        divisors_ggt_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("kgV and ggT Calculator")

# Create a notebook (tabbed interface)
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10)

# Frame for kgV
frame_kgv = ttk.Frame(notebook)
notebook.add(frame_kgv, text="kgV")

# kgV Input Fields
label_kgv1 = tk.Label(frame_kgv, text="Enter first number:")
label_kgv1.grid(row=0, column=0, padx=10, pady=10)

entry_kgv1 = tk.Entry(frame_kgv)
entry_kgv1.grid(row=0, column=1, padx=10, pady=10)

label_kgv2 = tk.Label(frame_kgv, text="Enter second number:")
label_kgv2.grid(row=1, column=0, padx=10, pady=10)

entry_kgv2 = tk.Entry(frame_kgv)
entry_kgv2.grid(row=1, column=1, padx=10, pady=10)

# kgV Calculate Button
calculate_kgv_button = tk.Button(frame_kgv, text="Calculate kgV", command=calculate_kgv)
calculate_kgv_button.grid(row=2, column=0, columnspan=2, pady=10)

# kgV Result Label
result_kgv_label = tk.Label(frame_kgv, text="")
result_kgv_label.grid(row=3, column=0, columnspan=2, pady=10)

# kgV Multiples Label
multiples_kgv_label = tk.Label(frame_kgv, text="", justify=tk.LEFT)
multiples_kgv_label.grid(row=4, column=0, columnspan=2, pady=10)

# Frame for ggT
frame_ggt = ttk.Frame(notebook)
notebook.add(frame_ggt, text="ggT")

# ggT Input Fields
label_ggt1 = tk.Label(frame_ggt, text="Enter first number:")
label_ggt1.grid(row=0, column=0, padx=10, pady=10)

entry_ggt1 = tk.Entry(frame_ggt)
entry_ggt1.grid(row=0, column=1, padx=10, pady=10)

label_ggt2 = tk.Label(frame_ggt, text="Enter second number:")
label_ggt2.grid(row=1, column=0, padx=10, pady=10)

entry_ggt2 = tk.Entry(frame_ggt)
entry_ggt2.grid(row=1, column=1, padx=10, pady=10)

# ggT Calculate Button
calculate_ggt_button = tk.Button(frame_ggt, text="Calculate ggT", command=calculate_ggt)
calculate_ggt_button.grid(row=2, column=0, columnspan=2, pady=10)

# ggT Result Label
result_ggt_label = tk.Label(frame_ggt, text="")
result_ggt_label.grid(row=3, column=0, columnspan=2, pady=10)

# ggT Divisors Label
divisors_ggt_label = tk.Label(frame_ggt, text="", justify=tk.LEFT)
divisors_ggt_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()