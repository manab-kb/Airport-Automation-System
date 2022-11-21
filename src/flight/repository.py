import sqlite3
import logging

"""
The functions in this file are used as helper functions in order to modify and present search queries within
the database. The database created is based off of sqlite, all of whose operations - edit, entry, fetch, join; works on
SQL based commands. The constructor object is used to initiate and maintain a connection with the sqlite database
present in a directory within the project. THe functions allow for finding all flights and looking up a specific flight
based on the id. All functions have been bundled up in a class, which is imported in the main file to perform operations
"""

class FlightStg:
    def __init__(self):
        self.connection = sqlite3.connect("./faceRecognition.db")
        self.cursor = self.connection.cursor()

    def findAll(self):
        query = """select * from flight"""
        try:
            data = self.cursor.execute(query).fetchall()
            return data, None
        except Exception as error:
            logging.error(error)

            return None, error
        finally:
            self.connection.close()

    def findById(self, id):
        query = """select * from flight where idFlight = '{}'""".format(id)
        try:
            data = self.cursor.execute(query).fetchall()
            return data[0]
        except Exception as error:
            logging.error(error)
