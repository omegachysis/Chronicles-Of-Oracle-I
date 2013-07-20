
from BanishmentBlade.engine import *

def start(data):
    while True:
        if data["area"] == 0:
            narrateThought("""I thought my time was up.
I thought I was done...""")

            narrateVisual("""You wake up in a solitary dark chamber.
The walls are wet, dripping and covered with overgrown plants.""")

