import graph_engine
from level import level
from the_world import World
from graph_engine import Graphics
from platformer import PlatformerGame


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


class Montezuma(PlatformerGame, Graphics):
    player = 'monRev1.png'
    window_width = 1280
    window_height = 800

    def __init__(self):
        super().__init__()
        self.set_level(LevelCoridor(), 400, 300)


game = Montezuma()
game.run()


#for item in level:
 #  graph_engine.add_sprite(item['image'], item['x'], item['y'])

