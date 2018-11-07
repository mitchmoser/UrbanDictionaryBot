#!/usr/bin/env python3
import requests
import random
from bs4 import BeautifulSoup
import time
import html
import markovify
import tweepy
import re


# credentials to login to twitter api
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

# login to twitter account api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
tp = tweepy.API(auth)

today = time.strftime("%Y-%m-%d")
url = "https://www.urbandictionary.com/yesterday.php?date=" + today

r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

# all words are in a list under 'no-bullet' class
noBullet = soup.find_all(attrs={'class':'no-bullet'})

newWords = []

# iterate through each word in list
for i in noBullet:
    # each word is inside <li> tags  
    words = i.find_all('li')
    for word in words:
        newWords.append(word.get_text().strip())

newDef = None

while newDef is None:
    try:
        # get definitions of random new word
        randomWord = random.choice(newWords)

        url = "https://www.urbandictionary.com/define.php?term=" + randomWord
        r = requests.get(url)

        soup = BeautifulSoup(r.text, "html.parser")

        meaning = soup.find_all(attrs={'class':'meaning'})

        mark = ""

        for i in meaning:
            definition = i.get_text()
            definition = html.unescape(definition)
            definition = definition.strip()
            # some definitions have lists in 1. 2. format
            # that mess up markov chains; use regex to remove period
            definition = re.sub('((\d+)[\.])(?!([\d]+))','\g<2>',definition)
            mark += (definition + " ")

        text_model = markovify.Text(mark)

        newDef = text_model.make_short_sentence(140)

    except KeyError:
        # this seems like the error when a word doesn't have
        # enough input for a the markov generator
        # we want to try again w/o any output at this point
        continue

# tweet markov-generated sentence
tweet = "#" + randomWord.replace(" ", "") + "\n" + newDef + "\n#UrbanDictionary"
tp.update_status(tweet)
