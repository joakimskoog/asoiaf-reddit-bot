#!/usr/bin/env
# -*- coding: utf-8 -*-

import anapioficeandfire
import praw
import time
import re


def _parse_book(comment):
    result = re.search('!Book\((.+?)\)', comment.body)
    if result is not None:
        return result.group(1).strip()

    return None


def _parse_character(comment):
    result = re.search('!Character\((.+?)\)', comment.body)
    if result is not None:
        return result.group(1).strip()

    return None


def _parse_house(comment):
    result = re.search('!House\((.+?)\)', comment.body)
    if result is not None:
        return result.group(1).strip()

    return None


def _tick(comment):
    book = _parse_book(comment)
    character = _parse_character(comment)
    house = _parse_house(comment)

    if not book:
        print(book) #Send request to /api/books here
    if not character:
        print(character) #Send request to /api/characters here
    if not house:
        print(house) #Send request to /api/houses here


def _loop(reddit):
    for comment in praw.helpers.comment_stream(reddit, 'asoiaf'):
        _tick(comment)


if __name__ == '__main__':
    print('Initiating bot...')
    reddit = praw.Reddit('asoiaf-reddit-bot')
    _loop(reddit)
    print('Exiting bot...')