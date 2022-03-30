from game.scripting.action import Action
import random
from game.scripting.control_actors_action import ControlActorsAction
from game.services.keyboard_service import KeyboardService
import constants
from game.shared.point import   Point
import os

class AutoMove(Action):

    def __init__(self):
        self._direction=Point(0, constants.CELL_SIZE)
        self._start_moving_position=0
        self._start_adding=False
        self._direction2=Point(0, constants.CELL_SIZE)
        self._direction3=Point(0, constants.CELL_SIZE)

    def execute(self, cast, script):
        number=random.randint(0,50)
        player2 = cast.get_first_actor("player2")
        enemys_lsit=cast.get_actors('player2')

        if len(enemys_lsit)>1:
            enemy2=enemys_lsit[1].get_head()
        if len(enemys_lsit)>2:
            enemy3=enemys_lsit[2].get_head()       
        enemy=player2.get_head()
        print(number)
        keys=['a','w','s','d']
        for i in keys:

            if KeyboardService().is_key_down(i):
                self._start_adding=True
        if self._start_adding:
            self._start_moving_position+=1
        if self._start_moving_position>5:
            script_dir = os.path.dirname(__file__)

             #Moves to the left
            if number== 1:
                self._direction=Point(-constants.CELL_SIZE, 0)
                rel_path='../../assets/tronenemyj.png'
                abs_file_path=os.path.join(script_dir,rel_path)            
                enemy.set_text(abs_file_path)
                #Moves to the right
            elif number== 2:
                self._direction=Point(constants.CELL_SIZE, 0)
                rel_path='../../assets/tronenemyl.png'
                abs_file_path=os.path.join(script_dir,rel_path)            
                enemy.set_text(abs_file_path)
                #Moves up
            elif number== 3:
                self._direction=Point(0, -constants.CELL_SIZE)
                rel_path='../../assets/tronenemyi.png'
                abs_file_path=os.path.join(script_dir,rel_path)            
                enemy.set_text(abs_file_path)
                # Moves down
            elif number== 4:
                self._direction=Point(0, constants.CELL_SIZE)
                rel_path='../../assets/tronenemyk.png'
                abs_file_path=os.path.join(script_dir,rel_path)            
                enemy.set_text(abs_file_path)
                #Moves to the left
            elif number==5:
                self._direction2=Point(-constants.CELL_SIZE, 0)
                rel_path='../../assets/tronenemyj.png'
                abs_file_path=os.path.join(script_dir,rel_path)            
                if len(enemys_lsit)>1:
                    enemy2.set_text(abs_file_path)

                #Moves to the right
            elif number==6:
                self._direction2=Point(constants.CELL_SIZE, 0)
                rel_path='../../assets/tronenemyl.png'
                abs_file_path=os.path.join(script_dir,rel_path)            
                if len(enemys_lsit)>1:
                    enemy2.set_text(abs_file_path)                #Moves up
            elif number==7:
                self._direction2=Point(0, -constants.CELL_SIZE)  
                rel_path='../../assets/tronenemyi.png'
                abs_file_path=os.path.join(script_dir,rel_path)            
                if len(enemys_lsit)>1:
                    enemy2.set_text(abs_file_path)
                #Moves down             
            elif number==8:
                self._direction2=Point(0, constants.CELL_SIZE)
                rel_path='../../assets/tronenemyk.png'
                abs_file_path=os.path.join(script_dir,rel_path)            
                if len(enemys_lsit)>1:
                    enemy2.set_text(abs_file_path)
                    
            elif number==9:
                self._direction3=Point(-constants.CELL_SIZE, 0)
                rel_path='../../assets/tronenemyj.png'
                abs_file_path=os.path.join(script_dir,rel_path)            
                if len(enemys_lsit)>2:
                    enemy3.set_text(abs_file_path)

                #Moves to the right
            elif number==10:
                self._direction3=Point(constants.CELL_SIZE, 0)
                rel_path='../../assets/tronenemyl.png'
                abs_file_path=os.path.join(script_dir,rel_path)            
                if len(enemys_lsit)>2:
                    enemy3.set_text(abs_file_path)                #Moves up
            elif number==11:
                self._direction3=Point(0, -constants.CELL_SIZE)  
                rel_path='../../assets/tronenemyi.png'
                abs_file_path=os.path.join(script_dir,rel_path)            
                if len(enemys_lsit)>2:
                    enemy3.set_text(abs_file_path)
                #Moves down             
            elif number==12:
                self._direction3=Point(0, constants.CELL_SIZE)
                rel_path='../../assets/tronenemyk.png'
                abs_file_path=os.path.join(script_dir,rel_path)            
                if len(enemys_lsit)>2:
                    enemy3.set_text(abs_file_path)

        # player2 =cast.get_first_actor("player2")
        player2.turn_head(self._direction)
        if len(enemys_lsit)>1:
            enemys_lsit[1].turn_head(self._direction2)
        if len(enemys_lsit)>2:
            enemys_lsit[2].turn_head(self._direction3)