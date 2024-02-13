import tkinter as tk
from tkinter import ttk
from databaseIntegration import readAll
from databaseIntegration import addToDB



class GateCard:
    def __init__(self, cardNumber, cardID, checkedIn):
        self.cardNumber = cardNumber
        self.cardID = cardID
        self.checkedIn = checkedIn
class AddCardWindow:
    def __init__(self, master, gate_cards):
        self.master = master
        self.gate_cards = gate_cards


    def add_gate_card(self):

        #the variables to store the card info
        card_number_var = tk.StringVar()
        card_id_var = tk.StringVar()
        checked_in_var = tk.StringVar()

        gateCards = readAll() #read all of the gate cards

        add_card_window = tk.Toplevel(self.master)
        add_card_window.title("Add new card")

        tk.Label(self.master, text="Card Number").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.master, text="Card ID").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.master, text="Checked In").grid(row=2, column=0, padx=5, pady=5)

        tk.Entry(self.master, textvariable=self.card_number_var).grid(row=0, column=1, padx=5, pady=5)
        tk.Entry(self.master, textvariable=self.card_id_var).grid(row=1, column=1, padx=5, pady=5)
        tk.Checkbutton(self.master, variable=self.checked_in_var).grid(row=2, column=1, padx=5, pady=5)

        tk.Button(self.master, text="Add Card", command=self.add_card(card_number_var, card_id_var, checked_in_var)).grid(row=3, column=0, columnspan=2, pady=10)


    def add_card(self, number, id, checked_in):
        gateCard = GateCard(number, id, checked_in)
        success = addToDB(gateCard) #add the card to the database
        #TODO Will return 1 if succedded, need to add an output for this


if __name__ == "__main__":
    root = tk.Tk()
    gate_cards_data = []  # Provide your gate card data here
    add_card_window = AddCardWindow(root, gate_cards_data)

    # Example: Call the show_all_gate_cards method
    add_card_window.add_gate_card()

    root.mainloop()




        