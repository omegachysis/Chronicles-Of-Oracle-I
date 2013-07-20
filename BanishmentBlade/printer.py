
from colorama import init, Fore, Back, Style
import sys
from time import sleep

init( autoreset = False )

def wait(milliseconds):
    sleep(milliseconds / 1000)

def line(lines=1):
    print ("\n" * lines)

class Colors:
    red = Style.BRIGHT + Fore.RED
    yellow = Style.BRIGHT + Fore.YELLOW
    green = Style.BRIGHT + Fore.GREEN
    blue = Style.BRIGHT + Fore.BLUE
    pink = Style.BRIGHT + Fore.MAGENTA
    cyan = Style.BRIGHT + Fore.CYAN
    white = Style.BRIGHT + Fore.WHITE
    black = Fore.BLACK

    bred = Style.BRIGHT + Back.RED
    byellow = Style.BRIGHT + Back.YELLOW
    bgreen = Style.BRIGHT + Back.GREEN
    bblue = Style.BRIGHT + Back.BLUE
    bpink = Style.BRIGHT + Back.MAGENTA
    bcyan = Style.BRIGHT + Back.CYAN
    bwhite = Style.BRIGHT + Back.WHITE
    bblack = Back.BLACK

class ColorsDark:
    red = Style.DIM + Fore.RED
    yellow = Style.DIM + Fore.YELLOW
    green = Style.DIM + Fore.GREEN
    blue = Style.DIM + Fore.BLUE
    pink = Style.DIM + Fore.MAGENTA
    cyan = Style.DIM + Fore.CYAN
    white = Style.DIM + Fore.WHITE
    black = Style.DIM + Fore.BLACK

    bred = Style.DIM + Back.RED
    byellow = Style.DIM + Back.YELLOW
    bgreen = Style.DIM + Back.GREEN
    bblue = Style.DIM + Back.BLUE
    bpink = Style.DIM + Back.MAGENTA
    bcyan = Style.DIM + Back.CYAN
    bwhite = Style.DIM + Back.WHITE
    bblack = Style.DIM + Back.BLACK

def cprint(text, keepStyle=True, end="\n"):
    text = text.replace("&& ", Colors.white + Colors.bblack)

    text = text.replace("&R ", Colors.red)
    text = text.replace("&Y ", Colors.yellow)
    text = text.replace("&G ", Colors.green)
    text = text.replace("&B ", Colors.blue)
    text = text.replace("&P ", Colors.pink)
    text = text.replace("&C ", Colors.cyan)
    text = text.replace("& ", Colors.white)
    text = text.replace("&B ", Colors.black)

    text = text.replace("&R-", Colors.bred)
    text = text.replace("&Y-", Colors.byellow)
    text = text.replace("&G-", Colors.bgreen)
    text = text.replace("&B-", Colors.bblue)
    text = text.replace("&P-", Colors.bpink)
    text = text.replace("&C-", Colors.bcyan)
    text = text.replace("&-", Colors.bblack)
    text = text.replace("&W-", Colors.bwhite)

    text = text.replace("&r ", ColorsDark.red)
    text = text.replace("&y ", ColorsDark.yellow)
    text = text.replace("&g ", ColorsDark.green)
    text = text.replace("&b ", ColorsDark.blue)
    text = text.replace("&p ", ColorsDark.pink)
    text = text.replace("&c ", ColorsDark.cyan)
    text = text.replace("&w ", ColorsDark.white)
    text = text.replace("&b ", ColorsDark.black)

    text = text.replace("&r-", ColorsDark.bred)
    text = text.replace("&y-", ColorsDark.byellow)
    text = text.replace("&g-", ColorsDark.bgreen)
    text = text.replace("&b-", ColorsDark.bblue)
    text = text.replace("&p-", ColorsDark.bpink)
    text = text.replace("&c-", ColorsDark.bcyan)
    text = text.replace("&b-", ColorsDark.bblack)
    text = text.replace("&w-", ColorsDark.bwhite)

    if not keepStyle:
        print("%s%s%s" % (Colors.bblack, Colors.white, text), end=end)
    else:
        print(text, end=end)

def flush():
    sys.stdout.flush()

def fprint(text):
    cprint(text, end="")
    flush()

def dprint(text, delay=30, end="\n"):
    delay = delay / 1000
    inat = -1
    ignore = 0
    for i in text:
        inat += 1
        if ignore == 0:
            if i != "&":
                fprint(i)
                sleep(delay)
            else:
                mark = text[inat:inat+3]
                fprint(mark)
                ignore = 2
        else:
            ignore -= 1
    print (end, end="")

def mprint(text, delay=25, end="\n"):
    formats = {
    "&! " : "f",
    "&@ " : "d",
    }

    text = "&! " + text

    part = "f"
    parts = []

    inat = -1
    ignore = 0

    for letter in text:
        inat += 1
        if ignore == 0:
            if letter != "&":
                part += letter
            else:
                mark = text[inat:inat+3]
                if mark in formats:
                    format = formats[mark]
                    parts.append(part)
                    part = format
                    ignore = 2
                else:
                    part += letter
        else:
            ignore -= 1

    parts.append(part)

    for part in parts:
        if part[0] == "f":
            fprint(part[1:])
        elif part[0] == "d":
            dprint(part[1:], delay, end="")
            
    print(end, end="")

def pprint(text, delay=25):
    mprint(text, delay, end="")
    input()

def sep(prefix="", width=70, char="-", delay=0):
    fprint(prefix)
    if delay:
        dprint(char*width, delay)
    else:
        fprint(char*width)
    print()

def main():
    fprint("&& ")
    pprint("&@ &P Hello World!  && This is simple sample text!")
    pprint("&@ && This should proceed in a very simple manner, &P just like a conversation!")
    pprint("&@ && This function is &P easy to use && and &P very straight-forward!")
    pprint("&@ && Just use the formatting marks to chose which parts of the conversation...")
    pprint("&@ && ...are displayed &! &Y Immediately! && &@ ...............")
    pprint("&@ && ...and which parts are displayed more gradually like this sentence.")

if __name__ == "__main__":
    main()
