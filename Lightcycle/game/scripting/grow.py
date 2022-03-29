from pickle import TRUE
from game.scripting.action import Action
import constants
from game.services.keyboard_service import KeyboardService

class Grow(Action):
    def __init__(self):
        self._start=False

    def execute(self, cast, script):
        """gets the two players"""
        snake = cast.get_first_actor("snakes")
        player2 = cast.get_first_actor("player2")
        enemy_list = cast.get_actors('player2')
        if len(enemy_list)>1:
            enemy2=enemy_list[1]
        """makes the tails grow in their respective colors (if the game
        is still going)"""
        keys=['a','w','s','d']
        for i in keys:
            if KeyboardService().is_key_down(i):
                self._start=True
        if self._start:
            snake.grow_tail(1,constants.TRON)
            player2.grow_tail(1,constants.ENEMY)
            if len(enemy_list)>1:
                enemy2.grow_tail(1,constants.ENEMY)
