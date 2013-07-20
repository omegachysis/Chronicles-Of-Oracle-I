
from BanishmentBlade.engine import *
import BanishmentBlade

def start(data):
    while True:
        if data["area"] == 0:
            narrateVisual("""
You wake up in a solitary dark chamber.
The walls are wet, dripping and covered with overgrown plants.
""")

            while True:
                sep("&& ")
                action = chooserText("COMMAND:")

                if "look" in action:
                    narrateThought("""Let's take a look around...""")
                    narrateVisual("""
The walls are wet, dripping and covered with overgrown plants.
The room is empty, there are no visible doors or gates.
There are piles of broken rocks and crumbled structures.
""")
