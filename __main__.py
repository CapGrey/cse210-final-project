import os
import random
from Casting.player import Player

from Casting.ships import Ships
from Scripts.movingObjects import MovingObjects
from Casting.cast import Cast

from Directing.director import Director

from Services.keyboard import KeyboardService
from Services.display import VideoService

from Shared.color import Color
from Shared.location import Location

import constants


def main():
    keyboard_service = KeyboardService()
    video_service = VideoService(constants.CAPTION, constants.MAX_X, 
                                 constants.MAX_Y, constants.CELL_SIZE,
                                 constants.FRAME_RATE)
    director = Director(keyboard_service, video_service)
    
    # create the cast
    moving_objects = MovingObjects(keyboard_service, constants.MAX_X, constants.MAX_Y)
    cast = moving_objects.cast
    
    # create the robot
    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y / 2)
    position = Location(x, y)

    robot = Player() 
    robot.set_text("#")
    robot.set_font_size(constants.FONT_SIZE)
    robot.set_color(constants.WHITE)
    robot.set_position(position)
    cast.add_actor("player", robot)
    
    ships = Ships()
    cast.add_actor("ships", ships)
    
    # start the game
    director.start_game(cast)


if __name__ == "__main__":
    main()