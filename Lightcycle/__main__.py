from pathlib import Path, WindowsPath
import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.snake import Snake
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point
from game.scripting.grow import Grow
from game.scripting.auto_move import AutoMove
import os

def main():
    
    # create the cast
    cast = Cast()
    script_dir = os.path.dirname(__file__)
    rel_path1 = "assets/tronplayerw.png"
    rel_path2="assets/tronenemyk.png"
    abs_file_path1 = os.path.join(script_dir, rel_path1)
    abs_file_path2 = os.path.join(script_dir, rel_path2)
    tron = abs_file_path1
    enemy =abs_file_path2
    cast.add_actor("snakes", Snake(int(constants.MAX_X / 2),15*37,tron))
    cast.add_actor("scores", Score(Point(0, 0),'one'))
    cast.add_actor("player2", Snake(int(constants.MAX_X / 2),15*0,enemy))
    # cast.add_actor('score2', Score(Point(780, 0),'two'))
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("input", AutoMove())
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    script.add_action("update", Grow())
    
    director = Director(video_service,keyboard_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()