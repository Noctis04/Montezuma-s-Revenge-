from the_world import World
from platformer import PlatformerGame
from skull import Skull
from player import Player
from sprite import Sprite
from graphics import key_pressed, window_width, window_height, init


class Level(World):
    tiles = 'tileMap1.png'
    def __init__(self, count_w, count_h):
        self.count_w = count_w
        self.count_h = count_h
        self.tile_map = [[0 for x in range(count_w)] for y in range(count_h)]

    def fill(self, cell, start_x = 0, start_y = 0, count_x = None, count_y =None):
        for y in range(start_y, start_y + count_y if count_y is not None else self.count_h):
            for x in range(start_x, start_x + count_x if count_x is not None else self.count_w):
                self.tile_map[y][x] = cell


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
        self.add_object(Player(self.world, Sprite('GameObject.png', 0, 0, 19, 11, 400, 300),
                                     key_pressed, 400, 300))
        self.add_object(Skull(self.world, 660, 550))
       # self.add_object(Skull(self.world, 260, 550))




game = Montezuma()
game.run()


#for item in level:
 #  graph_engine.add_sprite(item['image'], item['x'], item['y'])

