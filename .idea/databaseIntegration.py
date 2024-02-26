'''
This file will contain the class and function to connect to the database, it will feed this information
to the GUI file to show the cards
'''


class GateCard: #gatecard class
    def __init__(self, card_number, card_id, checked_in):
        self.card_number = card_number
        self.card_id = card_id
        self.checked_in = checked_in

import sqlite3 #import to connect to the database

conn = sqlite3.connect('gateCards.db') #open the gatecards database
c = conn.cursor() #cursol allowing to navigate the database

def readAll():

    '''
    Will take the database as an input and output everything to the GUI file
    Output is in the form of a list
    '''
    gateCards = []  # list to hold all of the gatecards
    c.execute("SELECT * FROM gateCards")
    while True: #loop to get all of the Gate cards line by line
        row = c.fetchone()
        if row == None: #if the last row was reached
            break
        gateCards.append(GateCard(row[0], row[1], row[2])) #append the object to the list

    return gateCards #return the list

'''
FUNCTION IS TESTED WORKING
'''


def readCheckedOut():
    '''
    Will take the database as an input and output all checked out gate cards to the GUI file
    Output is in the form of a list
    '''

    gateCards = []  # list to hold all of the gatecards
    c.execute("SELECT * FROM gateCards")
    while True:  # loop to get all of the Gate cards line by line
        row = c.fetchone()
        if row == None:  # if the last row was reached
            break
        if row[2] == 1: #if the gatecard is reading as checked out
            gateCards.append(GateCard(row[0], row[1], row[2]))  # append the object to the list


    return gateCards  # return the list

    '''
    FUNCTION IS TESTED WORKING
    '''

def addToDB(gatecard):
    '''
    Will the the database and a gatecard object and add them to the database
    '''


    gatecards = readAll() #get all of the gate cards to check for existing ID
    for i in gatecards:
        if i.card_id == gatecard.cardID:
            print('Card Already Exists')
            #TODO This needs to have an error message outputted on the screen
            return 0 #return a value that means failed

    number = gatecard.card_number
    id = gatecard.card_id
    checked = gatecard.checked_in
    c.execute("INSERT INTO gateCards (Site, Card, Out) VALUES (?,?,?)", (number, id, checked))
    conn.commit() #commit to the database
    return 1 #return a value that means succeeded

'''
FUNCTION IS TESTED WORKING
'''

def removeFromDB(gatecard):
    '''
    Will take the database and a gatecard object and remove the gatecard from the database
    '''
    gateCards = readAll() #read the database
    for i in gateCards:
        if i.card_id == gatecard.card_id: #if the card ID is valid
            c.execute("DELETE FROM gateCards WHERE Card = ?", (i.card_id,)) #remove the card from the database
            conn.commit() #commit the change to the database
            return 1 #return a value that means succedded
    #TODO This needs to have an error message output on the screen
    return 0 #return a value that means failed

'''
FUNCTION IS TESTED WORKING
'''




