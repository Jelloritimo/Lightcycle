import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
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
        self._direction = Point(constants.CELL_SIZE, 0)
        self._direction2 = Point(constants.CELL_SIZE, 0)


    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        player=cast.get_first_actor('snakes')
        robot=cast.get_first_actor("player2")
        enemy=robot.get_head()
        tron=player.get_head()
        
        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
            tron.set_text('C:/Users/USER/Desktop/Python/group/tron/Lightcycle/Lightcycle/assets/tronplayer1.png')
            
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
            tron.set_text('C:/Users/USER/Desktop/Python/group/tron/Lightcycle/Lightcycle/assets/tronplayerd.png')
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
            tron.set_text('C:/Users/USER/Desktop/Python/group/tron/Lightcycle/Lightcycle/assets/tronplayerw.png')

        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
            tron.set_text('C:/Users/USER/Desktop/Python/group/tron/Lightcycle/Lightcycle/assets/tronplayers.png')
        if self._keyboard_service.is_key_down('j'):
            self._direction2 = Point(-constants.CELL_SIZE, 0)
            enemy.set_text('C:/Users/USER/Desktop/Python/group/tron/Lightcycle/Lightcycle/assets/tronenemyj.png')
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction2 = Point(constants.CELL_SIZE, 0)
            enemy.set_text('C:/Users/USER/Desktop/Python/group/tron/Lightcycle/Lightcycle/assets/tronenemyl.png')
        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction2 = Point(0, -constants.CELL_SIZE)
            enemy.set_text('C:/Users/USER/Desktop/Python/group/tron/Lightcycle/Lightcycle/assets/tronenemyi.png')
        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction2 = Point(0, constants.CELL_SIZE)
            enemy.set_text('C:/Users/USER/Desktop/Python/group/tron/Lightcycle/Lightcycle/assets/tronenemyk.png')
        snake = cast.get_first_actor("snakes")
        snake.turn_head(self._direction)
        player2 =cast.get_first_actor("player2")
        player2.turn_head(self._direction2)