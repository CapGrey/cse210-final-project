from Casting.cast import Cast
from Casting.player import Player
"""
This class needs to control movment for every object in the game"""

class MovingObjects:
    def __init__(self, keyboard, max_x, max_y):
        """
        No Arguments.
        Set up variables that don't need to be modified.
        Reterns nothing."""
        self._player_velocity = 2
        self.cast = Cast()
        self._keyboard_service = keyboard
        self._player = Player()
        self._max_x = max_x
        self._max_y = max_y
        
    
    def Move_Objects(self):
        """
        Argument: max_y, get the position equal to the bottom of the screen.
        Uses the lists in cast to move objects down.
        Returns nothing."""
        """
        Move invaders based on thier volocity. When they hit the edge of the screen move them down once and reverse the volocity.
        """
        ship_list = self.cast.get_actors("ships")
        self._ship_speed = round(15 / len(ship_list)) #returns an int to help keep the ships on the grid.
        for ship in ship_list:
            ship.move_next(self, self._max_x, self._max_y)
            ship_location = ship.get_position()
            if ship_location > self._max_y:
                self.cast.remove_actor("ships", ship)
        
    
        
    def Move_Player(self):
        """
        No Argument
        Sets the player volocity based on keyboard action/
        Reterns nothing"""
        velocity = self._keyboard_service.get_direction() #I found it would be just easier for the player object to move itself and just modify the velocity here
        self._player.set_velocity(velocity)
        self._player.move_next(self, self._max_x, self._max_y)
        

