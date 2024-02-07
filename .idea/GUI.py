import tkinter as tk
from tkinter import ttk

from databaseIntegration import readAll

from showAllGateCards import ShowAllWindow


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
        for i, card in enumerate(self.gate_cards): #only display if card is checked out
            if(card.checked_in == 0):
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
        add_card_window = tk.Toplevel(self.master)
        add_card_window.title("Add New Gate Card")



    def remove_card(self):
        # Implement logic for removing a gate card
        pass

    def search(self):
        # Implement logic for searching gate cards
        pass

    def show_all(self):
        #Open a new window for displaying all gate cards
        ShowAllWindow.show_all_gate_cards(self)


if __name__ == "__main__":
    gate_cards_data = readAll() #get all of the gate cards from the database

    root = tk.Tk()
    app = GateCardGUI(root, gate_cards_data)
    root.mainloop()
