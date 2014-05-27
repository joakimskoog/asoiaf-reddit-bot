
import praw
import time
import configparser
import handlers


# ==========================
# Global variables
# ==========================

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
    subreddit = reddit.get_subreddit('asoiafbottest')
    return subreddit.get_comments()

def has_not_been_answered_before(comment):
    return comment.id not in answered_comments

def reply_to_comment(comment, handler):
    reply = handler.get_reply()
    reply += '\n\n'+'For more information about me, visit: https://github.com/joakimskoog/ASOIAFBot' + '\n\nTo give feedback and/or report bugs, visit: https://github.com/joakimskoog/ASOIAFBot/issues'

    comment.reply(reply)

    print("Commented")
    answered_comments.add(comment.id)

def handle_comment(comment):
    if has_not_been_answered_before(comment):
        handler = handlers.factory(comment.body)

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
