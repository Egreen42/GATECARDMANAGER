import tkinter as tk
from tkinter import ttk


def showAllScreen(self):
    # Open a new window for displaying all gate cards
    show_all_window = tk.Toplevel(self.master)
    show_all_window.title("Show All Gate Cards")

    # Display "Show All" text in the new window
    tk.Label(show_all_window, text="Show All").pack()