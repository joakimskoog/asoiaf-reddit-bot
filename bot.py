
import praw
import time
import configparser
import handlers
from database_handler import DatabaseHandler


# ==========================
# Global variables
# ==========================

#This will be included in the database when it's implemented.
database = DatabaseHandler()

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
    return subreddit.get_comments(limit = 100)


def reply_to_comment(comment, handler):
    reply = handler.get_reply()

    reply += '\n_____\n'
    reply += '[^([More information])] (https://github.com/joakimskoog/ASOIAFBot) '
    reply += '[^([Bugs/Feedback])] (https://github.com/joakimskoog/ASOIAFBot/issues)'

    comment.reply(reply)

    print("Commented")
    print(comment.id)
    database.set_comment_as_answered(comment.id)

def handle_comment(comment):
    print(comment)
    if not database.is_comment_answered(comment.id):
        handler = handlers.factory(comment.body, database)

        if handler != None:
            reply_to_comment(comment, handler)

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
