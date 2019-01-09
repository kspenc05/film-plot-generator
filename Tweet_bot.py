#!/usr/bin/python
import mechanize
import random

#PURPOSE:: establish a connection for the twitter bot
#NOTE:: it is separate from the twitter bot, since it can work for
#other mechanize connections rather than just twitter bots
def set_connection(br):
    br.set_handle_robots(False)
    br.set_handle_refresh(False)
    br.addheaders = [('User-agent', 
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    br.open("http://www.twitter.com/login")
    return br

class Tweet_bot(object):
    connection = mechanize.Browser()

    def __init__(self):
        set_connection(self.connection)

    #PURPOSE:: finds the name of a link and then follows it. May search based on
    #the name of the link of the url of the link
    #ARGUMENTS:: the self, the string to search for, and the search mode which
    #would indicate which attribute to look for
    def find_n_follow(self, search_term, mode):
        if(mode == "url"):
            link = self.connection.find_link(url = search_term)
                
        elif(mode == "text"):
            link = self.connection.find_link(text = search_term)
        
        self.connection.follow_link(link)

    #PURPOSE:: logs the twitter bot into twitter, using its given username 
    #and password
    #PRE-CONDITIONS:: username and password must be set using __init__() before
    #it can log in
    def login (self, user, password):
        self.connection.select_form(nr = 1)
        login = self.connection.forms()[1]
        login.controls[1].readonly = False
        login.controls[1].value = user
        login.controls[2].value = password
        login.controls[5].readonly = False
        self.connection.submit()

    #PURPOSE:: post a tweet after logging in
    #ARGUMENTS:: self, and the tweet as a string
    #PRE-CONDITIONS:: twitter bot must be logged in, tweet must be a string
    def post_tweet(self, tweet):
        self.find_n_follow("/compose/tweet", "url")
        self.connection.select_form(nr = 1)
        compose_tweet = self.connection.forms()[1]
        compose_tweet.controls[1].value = tweet
        compose_tweet.controls[3].readonly = False
        self.connection.submit()

    #PURPOSE:: logs out the twitter bot
    def logout(self):
        self.find_n_follow("Sign out", "text")
        self.connection.select_form(nr = 0)
        self.connection.forms()[0].controls[1].readonly = False
        self.connection.submit()
