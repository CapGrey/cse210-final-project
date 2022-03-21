import constants
from Shared.location import Location
from Casting.player import player


class ControlActorsAction():
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.
    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """
        

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        
    def execute(self):
        """Executes the control actors action.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        # left
        if self._keyboard_service.is_key_down('a'):
            self._keyboard_service.set_direction(-constants.CELL_SIZE)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._keyboard_service.set_direction(constants.CELL_SIZE)
        
        # Space
        #if self._keyboard_service.is_key_down('space'):
            #player.shoot()
        
        # Change fire mode
        # if self._keyboard_service.is_key_down('w'):
        #     player.change_fire_mode()