from game_object import GameObject
from graph_engine import KEY_LEFT, KEY_RIGHT, KEY_UP

class Player(GameObject):
    speed_x = 10
    speed_y = 25
    def __init__(self, world, sprite, key_pressed):
        """
        Инициализация объекта игрока.

        :param sprite: Спрайт игрока.
        :param key_pressed: Функция для проверки, какие клавиши нажаты.
        """
        super().__init__(world, sprite)
        self.key_pressed = key_pressed
        self.gravity = 7  # Значение гравитации

    def check_collision(self, tiles):
        tile_height = 8
        player_height = 181

        for y, row in enumerate(tiles):
            for x, tile in enumerate(row):
                if tile != 0:
                    if (self.y + player_height > (y * tile_height) - self.gravity * 1.1
                            and self.y < (y + 1) * tile_height):
                        if self.velocity_y > 0:  # При падение игрока
                            self.velocity_y = 0
                            self.y = y * tile_height - player_height - self.gravity
                            self.is_jumping = False
                        elif self.velocity_y < 0:  # При прыжок игрока
                            self.velocity_y = 0
                            self.y = (y + 2) * tile_height

        # Добавляем гравитацию
        self.velocity_y += self.gravity

    def update(self):
        """
        Обновление состояния игрока на основе нажатых клавиш.

        """
        # добавить коллизию
        # self.check_collision(self.tiles)

        if self.key_pressed(KEY_UP) and not self.is_on_air:
            # self.is_jumping = True
            self.velocity_y = -self.speed_y  # Устанавливаем вертикальную скорость прыжка

        if self.key_pressed(KEY_LEFT):
            self.velocity_x = -self.speed_x
        elif self.key_pressed(KEY_RIGHT):
            self.velocity_x = self.speed_x
        #else:
        #    self.velocity_x = 0

        super().update()