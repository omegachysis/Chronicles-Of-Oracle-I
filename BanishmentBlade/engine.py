
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
        pprint("&& &w &@  ~ " + text)
def narrateVisual(text):
    texts = text.split("\n")
    for text in texts:
        pprint("&& &G &@  ~ " + text)
def narrateObtain(itemName):
    pprint("&& &@ &P You obtained &Y " + itemName + "&P .")
