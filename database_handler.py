'''
Created on 23 maj 2014

@author: Oakin
'''

from objects import House

class DatabaseHandler(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''

    def get_house(self, houseName):
        house = House()
        house.name = houseName
        house.coat_of_arms = "Sable, a three headed dragon breathing flames gules"
        house.words = "Fire and Blood"
        house.cadet_branch = "Blackfyre, Baratheon"
        house.seat = "Red Keep (formerly), Dragonstone (formerly), Summerhall (formerly)"
        house.current_lord = "Queen Daenerys Targaryen"
        house.region = "King's Landing, Dragonstone, Valyria"
        house.title = "King of the Seven Kingdoms, Lord of the Andals, the Rhoynar and the First Men, Prince of Dragonstone (heir apparent)"
        house.heir = "Testing"
        house.overlord = "None"
        house.founder = "Wutwut"
        house.founded = "House Targaryen: >114BC, House Targaryen of King's Landing:0AC"

        return house