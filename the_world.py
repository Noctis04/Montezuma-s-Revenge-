import graphics as g

class World:
    objects = []
    count_w = 0
    count_h = 0
    tile_map = []
    tile_width = 0
    tile_height = 0

    def add_object(self, game_object):
        """
        Добавить игровой объект в мир.
        """
        self.objects.append(game_object)

    def remove_object(self, game_object):
        """
        Удалить игровой объект из мира.
        """
        if game_object in self.objects:
            self.objects.remove(game_object)

    def update(self):
        """
        Обновить состояние всех объектов в мире.
        """
        for game_object in self.objects:
            game_object.update()

    def get_tile(self, x, y):
        if x >= 0 and y >= 0 and x < self.count_w * self.tile_width and y < self.count_h * self.tile_height:
            return self.tile_map[int(y / self.tile_height)][int(x / self.tile_width)]
        else:
            return None