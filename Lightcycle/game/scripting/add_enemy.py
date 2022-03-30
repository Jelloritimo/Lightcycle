from game.scripting.action import Action
from game.casting.snake import Snake
import constants
import os

class AddEnemy(Action):

    def __init__(self):
        self._add_enemy=True
        script_dir = os.path.dirname(__file__)
        rel_path2="../../assets/tronenemyk.png"
        abs_file_path2 = os.path.join(script_dir, rel_path2)
        self._enemy =abs_file_path2

    def execute(self, cast, script):
        score=cast.get_first_actor('scores')
        points=score.get_points()
        if points==5 and self._add_enemy:
            cast.add_actor('player2',Snake(int(constants.MAX_X / 2+90),15*0,self._enemy))
            self._add_enemy=False
        if points==6:
            self._add_enemy=True
        if points==10 and self._add_enemy:
            print('works?')
            cast.add_actor('player2',Snake(int(constants.MAX_X / 2-90),15*0,self._enemy))
            self._add_enemy=False