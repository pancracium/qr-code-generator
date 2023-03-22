"""Main file."""

#########################################
# QR CODE GENERATOR [v0.3 (22-03-2023)] #
#########################################

#Import necessary modules
import tkinter as tk
from app import QrCodeGeneratorApp

#Create a window
root = tk.Tk()
app = QrCodeGeneratorApp(master=root, width=800, height=600)
app.master.mainloop()