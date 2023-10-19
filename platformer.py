from the_world import World
from player import Player


class PlatformerGame:
    player = None

    def __init__(self):
        """
        Инициализация игры.

        """
        super().__init__()  # Вызов конструктора родительского класса
        #self.world = World()
        #self.player = self.Player(self.add_sprite(self.player), self.key_pressed)
        #self.player.x = 100
        #self.player.y = 100
        #self.world.add_object(self.player)

    def set_level(self, level, player_x, player_y):
        self.world = level
        self.world.tile_width = self.tile_width
        self.world.tile_height = self.tile_height
        #self.tiles = level.tile_map
        self.player = Player(self.world, self.add_sprite(self.player), self.key_pressed)
        self.player.x = player_x
        self.player.y = player_y
        self.world.add_object(self.player)
        self.set_tiles(level.tile_map, level.tiles)
    def run(self):
        """
        Запуск игрового цикла.
\
        """
        while True:
            if self.process_events():
                break
            self.world.update()
            self.draw_all()
        self.quit()
