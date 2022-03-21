from Casting.player import Player
from Shared.color import Color
import random
import constants

class Ships(Player):

    def __init__(self):
        super().__init__
        self.set_text("o")
        self.set_color(Color(0,0,0))
        self.set_position([0,0])
        self.set_velocity([0,-1])
