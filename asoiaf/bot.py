#!/usr/bin/env
# -*- coding: utf-8 -*-

import anapioficeandfire
import praw
import time


def _tick(comment):
    print('Tick')


def _loop(reddit):
    for comment in praw.helpers.comment_stream(reddit, 'asoiaf'):
        _tick(comment)


if __name__ == '__main__':
    print('Initiating bot...')
    reddit = praw.Reddit('asoiaf-reddit-bot')
    _loop(reddit)
    print('Exiting bot...')