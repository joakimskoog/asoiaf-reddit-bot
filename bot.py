'''
Created on 23 maj 2014

@author: Oakin
'''

import praw
import time
import configparser
import re
import database_handler


# ==========================
# Global variables
# ==========================

database = database_handler.DatabaseHandler()

#This will be included in the database when it's implemented.
answered_comments = set()

def initiate_bot():
    '''
    Initiates the bot by retrieving settings from the config file.
    :returns The reddit object
    '''

    config = configparser.ConfigParser()
    config.read('config.cfg')

    #Retrieve the reddit specific information from the config
    user_agent = config.get('Reddit', 'user_agent')
    username = config.get('Reddit', 'username')
    password = config.get('Reddit', 'password')

    #Use the information to login
    reddit = praw.Reddit(user_agent)
    reddit.login(username, password)

    return reddit

def get_comments(reddit):
    '''
    Retrieves all comments from /r/asoiaf. This should be fixed to only retrieve
    the X latest comments.
    :returns All comments from /r/asoiaf
    '''
    subreddit = reddit.get_subreddit('asoiaf')
    return subreddit.get_comments()


def get_house_from_search_term(text):
    possibleMatch = None
    result = re.search('!House\((.+?)\)', text)

    if result != None:
        possibleMatch = result.group(1)

    return possibleMatch

def has_not_been_answered_before(comment):
    return comment.id not in answered_comments

def reply_to_comment(comment, house):
    '''
    Replies to a comment with the information about the given house.
    This is ugly and should be fixed in later versions.
    '''
    columnList = []
    cellList = []

    if house.name != "":
        columnList.append('Name')
        cellList.append(house.name)
    if house.coat_of_arms != "":
        columnList.append('Coat of arms')
        cellList.append(house.coat_of_arms)
    if house.words != "":
        columnList.append('Words')
        cellList.append(house.words)
    if house.cadet_branch != "":
        columnList.append('Cadet branch')
        cellList.append(house.cadet_branch)
    if house.seat != "":
        columnList.append('Seat')
        cellList.append(house.seat)
    if house.current_lord != "":
        columnList.append('Current lord')
        cellList.append(house.current_lord)
    if house.region != "":
        columnList.append('Region')
        cellList.append(house.region)
    if house.title != "":
        columnList.append('Title')
        cellList.append(house.title)
    if house.heir != "":
        columnList.append('Heir')
        cellList.append(house.heir)
    if house.overlord != "":
        columnList.append('Overlord')
        cellList.append(house.overlord)
    if house.founder != "":
        columnList.append('Founder')
        cellList.append(house.founder)
    if house.founded != "":
        columnList.append('Founded')
        cellList.append(house.founded)

    reply = ""

    for column in columnList:
        reply = reply + column + '|'

    reply = reply + '\n'

    for i in range(0, len(columnList)):
        reply = reply + '---------|'

    reply = reply + '\n'

    for cell in cellList:
        reply = reply + cell + '|'


    reply = reply + '\n\n'+'For more information about me, visit: https://github.com/joakimskoog/ASOIAFBot' + '\n\nTo give feedback and/or report bugs, visit: https://github.com/joakimskoog/ASOIAFBot/issues'

    comment.reply(reply)


    print("Commented")
    answered_comments.add(comment.id)

def handle_comment(comment):
    if has_not_been_answered_before(comment):
        house = get_house_from_search_term(comment.body)
        if(house != None):
            houseObject = database.get_house(house)
            reply_to_comment(comment, houseObject)

def handle_comments(comments):
    for comment in comments:
        handle_comment(comment)


def main_loop(reddit):
    while True:
        comments = get_comments(reddit)
        handle_comments(comments)

        #Sleep for a while so we don't break the API rules.
        time.sleep(60)

if __name__ == '__main__':
    reddit = initiate_bot()
    main_loop(reddit)
