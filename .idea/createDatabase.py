import sqlite3 #import to use SQLite

conn = sqlite3.connect('gateCards.db') #open the gatecards database

c = conn.cursor() #allows SQL commands to be executed on the database

'''
This next block of code will be run for first time setup only, will not be run again

This will populate the database, WILLNOT create the database if it doesn't exist

It will error if it is attempted to be run without an existing database
'''

siteNumber = int(input('Enter site number: ')) #get the initial site number

while(siteNumber != 0): #loop while 0 is not entered as the site number
    cardID = int(input('Enter the card id'))  # THIS IS TEMPORARY, WILL BE SCANNER WITH SCANNER ONCE SETUP
    c.execute("INSERT INTO gateCards VALUES(siteNumber,cardID,0)") #insert the site number, and card ID into the database, set to 0
    conn.commit() #commit to the database
    print('Enter 0 to exit')
    siteNumber = int(input('Enter Site number'))

conn.close() #close connection to the database