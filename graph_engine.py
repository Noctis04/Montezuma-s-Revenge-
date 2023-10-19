from sdl2 import *
import sdl2.ext
from sprite import Sprite

KEY_LEFT = sdl2.SDLK_LEFT
KEY_RIGHT = sdl2.SDLK_RIGHT
KEY_UP = sdl2.SDLK_UP

class Graphics:
    window_width = 1024
    window_height = 768
    sprites = []
    keys = {}
    tile_map = None
    tiles = None
    tile_width = 8
    tile_height = 8
    tiles_count_w = 0
    tiles_count_h = 0

    def __init__(self):
        """
        Инициализация окна и графики.

        """
        sdl2.ext.init()
        self.RESOURCES = sdl2.ext.Resources(__file__, "Images")
        self.window_render = sdl2.ext.Window("Platformer", size=(self.window_width, self.window_height))
        self.window_render.show()

    def set_tiles(self, tile_map, tiles):
        self.tile_map = tile_map
        self.tiles = sdl2.ext.load_image(self.RESOURCES.get_path(tiles))
        self.tiles_count_w = len(tile_map[0])
        self.tiles_count_h = len(tile_map)

    def add_sprite(self, file_name, pos_x=0, pos_y=0):
        """
        Добавляет спрайт на экран.

        :param file_name: Имя файла с изображением спрайта.
        :param pos_x: Начальная позиция по оси X.
        :param pos_y: Начальная позиция по оси Y.
        :return: Созданный спрайт.
        """
        image = sdl2.ext.load_image(self.RESOURCES.get_path(file_name))
        s = Sprite(image, pos_x, pos_y)
        self.sprites.append(s)
        return s

    def draw_all(self):
        """
        Отрисовывает все спрайты на экране.

        """
        window_surface = self.window_render.get_surface()
        if self.tile_map is not None:
            for y in range(self.tiles_count_h):
                for x in range(self.tiles_count_w):
                    cell = self.tile_map[y][x]
                    SDL_BlitSurface(self.tiles,
                                SDL_Rect(cell * self.tile_width, 0, self.tile_width, self.tile_height),
                                window_surface,
                                SDL_Rect(x * self.tile_width, y * self.tile_height,
                                         self.tile_width, self.tile_height))
        for sprite in self.sprites:
            SDL_BlitSurface(sprite.image, None, window_surface, SDL_Rect(sprite.x, sprite.y, 100, 100))
        SDL_UpdateWindowSurface(self.window_render.window)
        sdl2.SDL_Delay(30)

    def process_events(self):
        """
        Обрабатывает события SDL.

        :return: True, если событие SDL_QUIT обнаружено, в противном случае False.
        """
        for event in sdl2.ext.get_events():
            if event.type == sdl2.SDL_QUIT:
                return True
            elif event.type == sdl2.SDL_KEYDOWN:
                self.keys[event.key.keysym.sym] = True
            elif event.type == sdl2.SDL_KEYUP:
                self.keys[event.key.keysym.sym] = False

        return False

    def key_pressed(self, key):
        """
        Проверяет, нажата ли клавиша.

        :param key: Код клавиши.
        :return: True, если клавиша нажата, в противном случае False.
        """
        if key in self.keys:
            return self.keys[key]
        else:
            return False


    def quit(self):
        """
        Завершает работу графической подсистемы SDL.

        :return: None
        """
        sdl2.ext.quit()
