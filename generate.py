#!/usr/bin/python
import mechanize
import random
from Tweet_bot import Tweet_bot

#PURPOSE:: stores every single line of a given file
#RETURNS:: those lines in a list
def get_options(f):
    with open(f) as file:
        return file.readlines()
    
#PURPOSE:: chooses a random item in a given list, based on the size
#RETURNS:: the item which is randomly selected
def pick(options, size):
    return options[random.randint(0, size - 1)]

def generate_plot():
    jobs, cool_adjectives, names, personal, big, small = (get_options("jobs"),
        get_options("cool_adjectives"), 
        get_options("names"), 
        get_options("personal_plots"), 
        get_options("big_plots"), 
        get_options("small_plots"))

    #these are used twice, so I made them variables, so it does not have to generate
    #the length of these lists twice each (lines 37-41)
    adj_num = len(cool_adjectives)
    job_num = len(jobs)

    #They all come from files, so it was easier to strip the randomized option it chose 
    #rather than stripping every single option it takes in from every single file
    cool_adj_1 = pick(cool_adjectives, adj_num).rstrip("\n")
    work_1 = pick(jobs, job_num).rstrip("\n")

    cool_adj_2 = pick(cool_adjectives, adj_num).rstrip("\n")
    work_2 = pick(jobs, job_num).rstrip("\n")

    name = pick(names, len(names)).rstrip("\n")

    life_changing_event = pick(personal, len(personal)).rstrip("\n")

    first = pick(small, len(small)).rstrip("\n")
    second = pick(big, len(big)).rstrip("\n")
    
    with open("number", "r") as file:
        number = int(file.readline())
    
    plot = "Daily tweet #" + str(number) + ": After {}, {} (Dwayne Johnson), a {} {}, teams up with a {} {}. Together they must {}, in order to {}".format(
        life_changing_event, name, cool_adj_1, work_1, cool_adj_2, work_2, first, second)
    
    with open("number", "w") as file:
        file.seek(0)
        file.write(str(number + 1))
    
    return plot
    
#NOTE:: THIS LIST BELOW IS NOT USED ANYWHERE IN THE PROGRAM. 
#
#I made it as an idea for another part of the plot, but I forgot to use it.
#I have not commented this code out, so all it does is assemble this list.
#It took time to think of the options though, so I left in this unused list variable.
do_for_work = ["burn bridges to past ties", "assesses their financial options", 
    "assesses their security options",
    "solve mysteries", "balance the books of their company", 
    "create some new designs", "develop some new solutions",
    "create some radical balloon animals", "rob banks", "deal drugs", "commit insurance fraud",
    "cause car accidents", "pick up the mail", "go to the mall", "dress up", 
    "go to a meeting", "file some paper work", "sign some documents", "evacuate everyone",
    "negotiate", "stop terrorists", "clean", "get to their jobs", "move to another country", 
    "talk to his boss", "leave his job", "maintain the peace between two rival gangs", 
    "maintain the peace between two hostile groups of people", "delay the inevtiable"]

bot = Tweet_bot()
bot.login("@dwayne_2", "Plot!123")
plot = generate_plot()
print plot
bot.post_tweet(plot)
#bot.logout()

print "tweet submitted"