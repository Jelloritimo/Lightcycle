from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        self._video_service.clear_buffer()

        score = cast.get_first_actor("scores")
        # score2 = cast.get_first_actor("score2")
        snake = cast.get_first_actor("snakes")
        player2=cast.get_first_actor("player2")
        enemy_list=cast.get_actors("player2")
        if len(enemy_list)>1:
            segments3=enemy_list[1].get_segments()
            self._video_service.draw_actors(segments3)
        if len(enemy_list)>2:
            print('drawcorrect')
            segments4=enemy_list[2].get_segments()
            self._video_service.draw_actors(segments4)      
        segments2=player2.get_segments()
        segments = snake.get_segments()
        messages = cast.get_actors("messages")

        
        self._video_service.draw_actors(segments)
        self._video_service.draw_actors(segments2)
        self._video_service.draw_actor(score)
        # self._video_service.draw_actor(score2)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()