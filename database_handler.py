
from objects import House
import sqlite3

class DatabaseHandler(object):
    '''
    classdocs
    '''


    def __init__(self):
        self.__database__ = 'example.db'

    def get_house(self, houseName):
        connection = sqlite3.connect(self.__database__)

        #Encapsulate the rows so we can index with strings later on
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        #Create a tuple so we can use the safe ?-method
        t = (houseName,)
        cursor.execute('SELECT* FROM house WHERE name=?', t)

        #We do fetchone() since we only expect to receive one row as a result. This may change in the future, look further into this later on.
        row = cursor.fetchone()

        house = None

        if row != None:
            house = House()
            house.name = row['name']
            house.coat_of_arms = row['coat_of_arms']
            house.words = row['words']
            house.cadet_branch = row['cadet_branch']
            house.seat = row['seat']
            house.current_lord = row['current_lord']
            house.region = row['region']
            house.title = row['title']
            house.heir = row['heir']
            house.overlord = row['overlord']
            house.founder = row['founder']
            house.founded = row['founded']

        connection.close()

        return house