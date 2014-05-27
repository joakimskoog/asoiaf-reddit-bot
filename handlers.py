
from database_handler import DatabaseHandler
import re


def factory(comment, database_handler):
    class HouseHandler(object):
        '''
        Handler for the house search term. It's responsibility is to retrieve the correct
        house object from the database and then format the reply in a nice way.
        '''

        def __init__(self, name_of_house, database_handler):
            self.__columnHeaders__ = ['Name', 'Coat of arms', 'Words', 'Cadet branch', 'Seat', 'Current lord',
                                      'Region', 'Title', 'Heir', 'Overlord', 'Founder', 'Founded']
            self.__database_handler__ = database_handler
            self.name_of_house = name_of_house

        def __get_house__(self):
            return self.__database_handler__.get_house(self.name_of_house)

        def __get_formatted_reply__(self, house):
            reply = ''
            valueList = []

            valueList.append(house.name)
            valueList.append(house.coat_of_arms)
            valueList.append(house.words)
            valueList.append(house.cadet_branch)
            valueList.append(house.seat)
            valueList.append(house.current_lord)
            valueList.append(house.region)
            valueList.append(house.title)
            valueList.append(house.heir)
            valueList.append(house.overlord)
            valueList.append(house.founder)
            valueList.append(house.founded)

            for i in range(0, len(self.__columnHeaders__)):
                if valueList[i] != '':
                    reply += self.__columnHeaders__[i] + '|'

            reply += '\n'

            for header in self.__columnHeaders__:
                reply += '---------|'

            reply += '\n'

            for value in valueList:
                if value != '':
                    reply += value + '|'

            return reply


        def get_reply(self):
            house = self.__get_house__()

            if house != None:
                return self.__get_formatted_reply__(house)
            else:
                return 'Error |\n ---------|\n The given house "' + self.name_of_house + '" does not exist.|'


    def get_house_from_comment(comment):
        possibleMatch = None

        result = re.search('!House\((.+?)\)', comment)

        if result != None:
            possibleMatch = result.group(1)

        return possibleMatch


    house = get_house_from_comment(comment)
    if house != None: return HouseHandler(house, database_handler)


