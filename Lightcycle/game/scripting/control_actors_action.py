import constants
from game.scripting.action import Action
from game.shared.point import Point
import os
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
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
        self._direction = Point(0, -constants.CELL_SIZE)
        self._direction2 = Point(0, constants.CELL_SIZE)
        self.move_actors= MoveActorsAction()


    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        player=cast.get_first_actor('snakes')
        robot=cast.get_first_actor("player2")
        # enemy=robot.get_head()
        tron=player.get_head()
        script_dir = os.path.dirname(__file__)


        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
            rel_path='../../assets/tronplayer1.png'
            abs_file_path=os.path.join(script_dir,rel_path)            
            tron.set_text(abs_file_path)

        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
            rel_path='../../assets/tronplayerd.png'
            abs_file_path=os.path.join(script_dir,rel_path)            
            tron.set_text(abs_file_path)
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
            rel_path='../../assets/tronplayerw.png'
            abs_file_path=os.path.join(script_dir,rel_path)            
            tron.set_text(abs_file_path)
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
            rel_path='../../assets/tronplayers.png'
            abs_file_path=os.path.join(script_dir,rel_path)            
            tron.set_text(abs_file_path)

        # if self._keyboard_service.is_key_down('j'):
        #     self._direction2 = Point(-constants.CELL_SIZE, 0)
        #     rel_path='../../assets/tronenemyj.png'
        #     abs_file_path=os.path.join(script_dir,rel_path)            
        #     enemy.set_text(abs_file_path)

        # # right
        # if self._keyboard_service.is_key_down('l'):
        #     self._direction2 = Point(constants.CELL_SIZE, 0)
        #     rel_path='../../assets/tronenemyl.png'
        #     abs_file_path=os.path.join(script_dir,rel_path)            
        #     enemy.set_text(abs_file_path)
        # # up
        # if self._keyboard_service.is_key_down('i'):
        #     self._direction2 = Point(0, -constants.CELL_SIZE)
        #     rel_path='../../assets/tronenemyi.png'
        #     abs_file_path=os.path.join(script_dir,rel_path)            
        #     enemy.set_text(abs_file_path)
        # # down
        # if self._keyboard_service.is_key_down('k'):
        #     self._direction2 = Point(0, constants.CELL_SIZE)
        #     rel_path='../../assets/tronenemyk.png'
        #     abs_file_path=os.path.join(script_dir,rel_path)            
        #     enemy.set_text(abs_file_path)

        snake = cast.get_first_actor("snakes")
        snake.turn_head(self._direction)
        player2 =cast.get_first_actor("player2")
        player2.turn_head(self._direction2)