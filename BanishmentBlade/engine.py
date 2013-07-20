
from BanishmentBlade.printer import *
import sys

##def playMusic(music):
##    clip = mp3play.load(r"BanishmentBlade/music/" + music)
##    clip.play()

def gotoWorld(world, data):
    data["world"] = world
    exec ("from BanishmentBlade.worlds import " + \
          data["world"].replace(" ", ""))
    exec (data["world"].replace(" ", "") + ".start(data)")

def prompt():
    return sys.stdin.readline()

def narrateThought(text):
    texts = text.split("\n")
    for text in texts:
        if text:
            pprint("&& &w &@  ~ " + text)
        else:
            print("\n")
    fprint("&& ")
def narrateVisual(text):
    texts = text.split("\n")
    for text in texts:
        if text:
            pprint("&& &G &@  ~ " + text)
        else:
            print("\n")
    fprint("&& ")
def narrateObtain(itemName):
    pprint("&& &@ &P You obtained &Y " + itemName + "&P .")
    fprint("&& ")

def chooserText(prompt):
    mprint(prompt)
    fprint("&w ")
    sep()
    value = input(":: ")
    sep()

    return value
    
def chooserMC(title, prefix, choices):
    """ Chooser Multiple Choice """
    mprint(title)
    sep()
    inat = -1
    for choice in choices:
        inat += 1
        nprefix = prefix.replace("#", str(inat))
        if prefix:
            mprint(nprefix + choice)
    fprint("&w ")
    if prefix:
        sep()

    while(True):
        fprint("&w ")
        choice = input(":: ")
        sep()
        try:
            choice = int(choice)
            if choice >= 0:
                try:
                    option = choices[choice]
                    break
                except:
                    mprint("&R Please choose a number in the list.")
                    sep()
            else:
                mprint("&R Please type a positive number.")
        except:
            mprint("&R Please type a valid number.")
            sep()
    return choice

def chooserYN(title):
    """ Chooser Yes / No """
    mprint(title)
    sep()
    while(True):
        fprint("&w ")
        choice = input(":: ")
        choice = choice.lower()
        choice = choice.replace("!", "")
        choice = choice.replace(".", "")
        choice = choice.replace("?", "")
        choice = choice.replace("'", "")
        sep()
        if choice in ('yes', 'yeah', 'sure', 'ya', 'of course', 'course',
                      'go ahead', 'whatever', 'whatev', 'yep', 'definitely',
                      'go', 'y', 'absolutely'):
            choice = True
            break
        elif choice in ('no', 'nope', 'no way', 'nah', 'definitely not',
                        'idk', 'no way man', 'idk', 'i dont know',
                        'not sure', 'dont know', 'n', 'absolutely not'):
            choice = False
            break
        else:
            mprint("&R It's a &P yes&R  or &P no&R  question.")
            sep()
    return choice

def progress(text, beats):
    fprint(text)
    dprint("." * beats, 500)
