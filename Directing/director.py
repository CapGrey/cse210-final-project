from Casting.ships import Ships
from Shared.color import Color
import constants

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._stage = 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        self._reset_ships()
        while self._video_service.is_window_open():
            self.stage(cast)
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def get_color_stage(self):
        color = (0,0,0)
        match(self._stage):
            case 1:
                color = constants.BLUE
            case 2:
                color = constants.GREEN
            case 3:
                color = constants.YELLOW
            case 4:
                color = constants.WHITE
            case 5:
                color = constants.RED
        
        return color

    def _reset_ships(self):
        color = self.get_color_stage()
        for i in range(0, self._stage + 1):
            for j in range(0, 7):
                ship = Ships()
                ship.set_position([constants.MAX_X * i, constants.CELL_SIZE * j + j])
                ship.set_color(color)

    def stage(self, cast):
        ships = cast.get_actors("ships")
        if not ships:
            self._stage += 1
            self._reset_ships()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("player")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        player = cast.get_first_actor("player")
        ships = cast.get_actors("ships")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)
        
        for ship in ships:
            if player.get_position() == ship.get_position():
                ships.remove(ship)
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors) # Sent a list when it required singles
        self._video_service.flush_buffer()