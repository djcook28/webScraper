import sqlite3

connection = sqlite3.connect("events.db")
cursor = connection.cursor()


def format_date(extracted):
    extracted_tuple = tuple(extracted.split(","))
    return [item.strip() for item in extracted_tuple]

def load_previous_extracted(data_tuple):
    #with open("data.txt", "r") as file:
    #   return file.read()
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", data_tuple)
    return (cursor.fetchall())

def store_extracted(data_tuple):
    #with open("data.txt", "a") as file:
    #    file.write(extracted+"\n")
    cursor.execute("INSERT INTO events VALUES (?, ?, ?)", data_tuple)
    connection.commit()