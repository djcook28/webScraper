import sqlite3

connection = sqlite3.connect("events.db")
cursor = connection.cursor()

def load_previous_extracted():
    #with open("data.txt", "r") as file:
    #   return file.read()
    cursor.execute("SELECT * FROM events")
    return (cursor.fetchall())

def store_extracted(data_tuple):
    #with open("data.txt", "a") as file:
    #    file.write(extracted+"\n")
    cursor.execute("INSERT INTO events VALUES (?, ?, ?)", data_tuple)
    connection.commit()