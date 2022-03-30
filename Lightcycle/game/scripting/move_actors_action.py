from game.scripting.action import Action
from game.services.keyboard_service import KeyboardService

class MoveActorsAction(Action):
    """
    An update action that moves all the actors.
    
    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """
    def __init__(self):
        self._start=False
        self._stop=True

    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        
        actors = cast.get_all_actors()
        keys=['a','w','s','d']
        score=cast.get_first_actor('scores')
        for i in keys:
            if KeyboardService().is_key_down(i):
                self._start=True
        if self._start:
            if score.get_points()<8:
                for actor in actors:
                    if actor!=actors[0]:
                        actor.move_next()
                    else:
                        if self._stop:
                            actor.move_next()
                            self._stop=False
                        else:
                            self._stop=True
            else:
                for actor in actors:
                    actor.move_next()
