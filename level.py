from the_world import World
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