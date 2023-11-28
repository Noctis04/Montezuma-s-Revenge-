from graphics import *
class PlatformerGame:
    player = None
    skull = None

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

    def set_level(self, level):

        self.world = level
        self.world.tile_width = tile_width
        self.world.tile_height = tile_height
        #self.tiles = level.tile_map
       # self.player = Player(self.world, self.add_sprite(self.player), self.key_pressed)
        #self.player.x = player_x
        #self.player.y = player_y
       # self.world.add_object(self.player)
        set_tiles(level.tile_map, level.tiles)

    def add_object(self, obj):
        obj.sprite_id = add_sprite(obj.sprite)
        self.world.add_object(obj)

    def run(self):
        """
        Запуск игрового цикла.

        """
        while True:
            if process_events():
                break
            self.world.update()
            draw_all()
        quit()
