##########################################
# BANISHMENT BLADE
#-----------------------
#  Designed to run on Python 3
#--------------------------------
#  ~ Matthew A. Robinson

from BanishmentBlade.printer import *
from BanishmentBlade.engine import gotoWorld
import textImages
import pickle
import glob

def saveGame(data):
    saveFile("saves/bb-game-" + data["name"] + ".sav", data)
    saveFile("saves/bb-saves.dat",
             {"latest" : "saves/bb-game-" + data["name"] + ".sav"})

def loadFile(filename):
    exists = True
    try:
        file = open(filename, "rb")
    except:
        exists = False
    if exists:
        data = pickle.load(file)
        file.close()
        return data
    else:
        return None
    
def saveFile(filename, data):
    file = open(filename, "wb")
    pickle.dump(data, file)
    file.close()

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


def introMenu():
    fprint("&C ")

    sep()

    title = textImages.chroniclesOfOracle

    fprint(title)

    sep()

    wait(1000)

def mainMenu():
    fprint("&R ")
    sep()

    subtitle = textImages.banishmentBlade

    fprint(subtitle)

    sep()

    wait(500)
    line()

    pprint("&& &@ Press enter to continue.")

    fprint("&Y ")
    sep()

    choices = ["Quit"]
    latest = loadFile("saves/bb-saves.dat")
    if latest:
        latest = latest["latest"]
    if latest:
        if loadFile(latest):
            choices.append("Continue")
    choices += ["Load Story", "New Story"]

    choice = chooserMC("&Y --- MAIN MENU --- ", "&& &@ # - ",
            choices)
    choice = choices[choice]

    def getSaveInfo(filename, index=0):
        sep("&& &B ")
        if index != 0:
            fprint("&& ")
            print (str(index) + ".")
            sep("&& &B ")
        fprint("&b-& ")
        save = loadFile(filename)
        print (save["name"])
        sep("&& &B ")
        fprint("&b-& ")
        print ("Level", str(save["level"]))
        print ("Diffulty:", ["Normal", "Hard"][save["difficulty"]-1])
        print (save["world"])

    if choice == "Quit":
        pass
    
    elif choice == "Continue":
        progress("&Y Loading latest saved story", 2)

        getSaveInfo(loadFile("saves/bb-saves.dat")["latest"])
        sep("&& &Y ")
        
        load = chooserYN("Load this story?")
        if load:
            data = loadFile(loadFile("saves/bb-saves.dat")["latest"])

            line(10)

            gotoWorld(data["world"], data)

            mainMenu()
        else:
            mainMenu()
        
    elif choice == "Load Story":
        progress("&Y Unloading saved stories", 2)

        saves = glob.glob("saves/bb-game-*.sav")
        inat = 0

        sep("&B ")
        print ("0. Cancel")
        sep("&B ")
        
        for save in saves:
            inat += 1
            getSaveInfo(save, inat)

        line(1)
        sep("&& ")
        choice = chooserMC("&& LOAD STORY", "", [0] + saves)

        if choice == 0:
            mainMenu()
        else:
            data = loadFile(saves[choice-1])

            line(10)

            gotoWorld(data["world"], data)

            mainMenu()
        
    elif choice == "New Story":
        progress("&Y Starting new story", 2)
        sep("&Y ")
        line(2)
        sep("&w ")

        data = {}
        
        while True:
            data["name"] = chooserText("&& &@ &C What is your name? ")
            if loadFile("saves/bb-game-" + data["name"] + ".sav"):
                choice = chooserYN(
                    "&& &R &@ This name already exists! \nYou must overwrite another save to do this.\nDo you really want to proceed?")
                if choice:
                    break
            else:
                break

        choice = chooserMC("&C Choose character gender", "&C &@ # - ",
            ("Male", "Female"))
        data["gender"] = ["male", "female"][choice]

        choice = chooserMC("&C Choose a difficulty.",
                           "&C &@ # - ", ("Normal", "Hard"))
        data["difficulty"] = [1, 2][choice]

        data["world"] = "Nova Shrine"
        data["area"] = 0
        
        data["level"] = 0
        data["status"] = {"Max Health" : 50, "Health" : 50,
                          "Max Mana" : 20, "Mana" : 20}
        
        data["skills"] = {"Strength" : 0, "Magic" : 0, "Speed" : 0,
                          "Capacity" : 100}
        
        data["persona"] = {"Charisma" : 50, "Speech" : 50, "Boldness" : 50,
                           "Intimidation" : 50, "Reflex" : 50, "Heroism" : 50,
                           "Happiness" : 50, "Wisdom" : 50, "Fitness" : 50,
                           "Excitment" : 50, "Compassion" : 50}
        
        data["abilities"] = []
        data["equipment"] = []
        data["items"] = []

        data["event"] = {}

        saveFile("saves/bb-game-" + data["name"] + ".sav", data)
        saveFile("saves/bb-saves.dat",
                 {"latest" : "saves/bb-game-" + data["name"] + ".sav"})

        line(10)

        gotoWorld(data["world"], data)

        mainMenu()

def main():
    introMenu()
    mainMenu()

if __name__ == "__main__":
    try:
        main()
    except Exception as errormsg:
        print ("Script errored!")
        print ("Error message: %s" % errormsg)
        print ("Traceback:")
        import traceback
        traceback.print_exc()
        print ("Press return to exit..")
        input()
