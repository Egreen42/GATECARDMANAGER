import tkinter as tk
from tkinter import ttk



class GateCard:
    def __init__(self, card_number, card_id, checked_in):
        self.card_number = card_number
        self.card_id = card_id
        self.checked_in = checked_in

class GateCardGUI:
    def __init__(self, master, gate_cards):
        self.master = master
        self.master.title("Gate Card Check-In/Out")

        # Initialize variables
        self.gate_cards = gate_cards

        # Create widgets
        tk.Label(master, text="Card Number").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(master, text="Card ID").grid(row=0, column=1, padx=5, pady=5)
        tk.Label(master, text="Status").grid(row=0, column=2, padx=5, pady=5)

        # Display gate card data with separators
        for i, card in enumerate(self.gate_cards):
            tk.Label(master, text=card.card_number).grid(row=i * 2 + 1, column=0, padx=5, pady=5)
            tk.Label(master, text=card.card_id).grid(row=i * 2 + 1, column=1, padx=5, pady=5)
            tk.Label(master, text="Checked In" if card.checked_in else "Checked Out").grid(row=i * 2 + 1, column=2, padx=5, pady=5)

            # Add separator line
            ttk.Separator(master, orient="horizontal").grid(row=i * 2 + 2, column=0, columnspan=3, sticky="ew", pady=5)

        # Add buttons
        tk.Button(master, text="Add Card", command=self.add_card).grid(row=i * 2 + 3, column=0, pady=10)
        tk.Button(master, text="Remove Card", command=self.remove_card).grid(row=i * 2 + 3, column=1, pady=10)
        tk.Button(master, text="Search", command=self.search).grid(row=i * 2 + 3, column=2, pady=10)
        tk.Button(master, text="Show All", command=self.show_all).grid(row=i * 2 + 3, column=3, columnspan=3, pady=10)

    def add_card(self):
        # Implement logic for adding a new gate card
        pass

    def remove_card(self):
        # Implement logic for removing a gate card
        pass

    def search(self):
        # Implement logic for searching gate cards
        pass

    def show_all(self):
        # Open a new window for displaying all gate cards
        show_all_window = tk.Toplevel(self.master)
        show_all_window.title("Show All Gate Cards")

        # Display "Show All" text in the new window
        tk.Label(show_all_window, text="Show All").pack()


if __name__ == "__main__":
    # Sample gate card data

    '''
    THIS HERE IS WHERE THE DATA WILL BE FED INTO TO BE DISPLAYED
    NEEDS TO BE UPDATED TO PULL FROM THE DATABASE
    '''
    gate_cards_data = [
        GateCard("001", "ID001", True),
        GateCard("002", "ID002", False),
        GateCard("003", "ID003", True),
    ]

    root = tk.Tk()
    app = GateCardGUI(root, gate_cards_data)
    root.mainloop()
