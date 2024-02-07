import tkinter as tk
from tkinter import ttk
from databaseIntegration import readAll

class ShowAllWindow:
    def __init__(self, master, gate_cards):
        self.master = master
        self.gate_cards = gate_cards

    def show_all_gate_cards(self):

        gateCards = readAll() #get the gate cards from the database

        show_all_window = tk.Toplevel(self.master)
        show_all_window.title("Show All Gate Cards")

        # Create widgets
        tk.Label(show_all_window, text="Card Number").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(show_all_window, text="Card ID").grid(row=0, column=1, padx=5, pady=5)
        tk.Label(show_all_window, text="Status").grid(row=0, column=2, padx=5, pady=5)

        # Display gate card data with separators
        for i, card in enumerate(gateCards):
            tk.Label(show_all_window, text=card.card_number).grid(row=i * 2 + 1, column=0, padx=5, pady=5)
            tk.Label(show_all_window, text=card.card_id).grid(row=i * 2 + 1, column=1, padx=5, pady=5)
            tk.Label(show_all_window, text="Checked In" if card.checked_in else "Checked Out").grid(row=i * 2 + 1,
                                                                                                    column=2,
                                                                                                    padx=5, pady=5)

            # Add separator line
            ttk.Separator(show_all_window, orient="horizontal").grid(row=i * 2 + 2, column=0, columnspan=3, sticky="ew",
                                                                     pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    gate_cards_data = []  # Provide your gate card data here
    show_all_window = ShowAllWindow(root, gate_cards_data)

    # Example: Call the show_all_gate_cards method
    show_all_window.show_all_gate_cards()

    root.mainloop()
