import sqlite3 #import to use SQLite

conn = sqlite3.connect('gateCards.db') #open the gatecards database

c = conn.cursor() #allows SQL commands to be executed on the database

#c.execute("""CREATE TABLE gateCards (
#            Site integer,
#            Card integer,
#           Out integer
#            )""")

#c.execute("INSERT INTO gateCards VALUES(1,1234567,0)")

c.execute("SELECT * FROM gateCards where Card = 1234567")

print(c.fetchone()) #print out the value

conn.commit() #add the changes to the database

conn.close() #close the connection


'''
THANK YOU PAST ME FOR NOT COMMENTING THIS, 
WHAT DOES ALL OF THIS DO?
HOW DO I CHANGE THIS TO DO WHAT I WANT
'''