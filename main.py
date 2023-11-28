from the_world import World
from platformer import PlatformerGame
from skull import Skull
from player import Player
from sprite import Sprite
from graphics import key_pressed, window_width, window_height, init
from level import Level


class LevelAllBricks(Level):
    def __init__(self):
        super().__init__(160,100)
        self.fill(1)


class LevelCoridor(LevelAllBricks):
    def __init__(self):
        super().__init__()
        self.fill(0, 0, 20, None, 50)
        self.fill(0, 50, 40, 20, 50)
        self.fill(0, 120, 40, 20, 50)


class Montezuma(PlatformerGame):
   # player = 'monRev1.png'
    window_width = 1280
    window_height = 800


    def __init__(self):
        init(self.window_width, self.window_height)
        super().__init__()
        self.set_level(LevelCoridor())
        self.add_object(Player(self.world, Sprite('GameObject.png',  400, 300,0, 0, 19, 11,),
                                     key_pressed, 400, 300))
        self.add_object(Skull(self.world, 660, 550))
       # self.add_object(Skull(self.world, 260, 550))




game = Montezuma()
game.run()


#for item in level:
 #  graph_engine.add_sprite(item['image'], item['x'], item['y'])

