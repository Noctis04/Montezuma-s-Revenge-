
class GameObject:
    G = 9.8 / 5
    T = 3.0
    def __init__(self, world, sprite, pos_x=0, pos_y=0, velocity_x=0, velocity_y=0, fly=False):
        """
        Инициализация объекта GameObject.

        :param sprite: Спрайт, связанный с объектом.
        :param pos_x: Начальная позиция по оси X.
        :param pos_y: Начальная позиция по оси Y.
        :param velocity_x: Начальная скорость по оси X.
        :param velocity_y: Начальная скорость по оси Y.
        """
        self.world = world
        self.sprite = sprite
        self.x = pos_x
        self.y = pos_y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.fly = fly
        self.is_on_air = False

    def update(self):
        """
        Обновляет состояние объекта GameObject путем обновления его позиции на основе скорости.

        """
        if not self.fly:
            if not self.on_ground():
                self.is_on_air = True
                self.apply_gravity()
            else:
                if self.is_on_air:
                    self.velocity_y = 0
                    self.is_on_air = False
        self.x += self.velocity_x
        self.y += self.velocity_y
        # if self.velocity_x != 0:
        self.put_on_wall()
        # if not self.is_on_air:
        self.put_on_floor()
        self.apply_friction()
        self.sprite.x = int(self.x)
        self.sprite.y = int(self.y)

    def apply_gravity(self):
        self.velocity_y += self.G

    def on_ground(self):
        x = self.x + self.sprite.image.w / 2
        y = self.y + self.sprite.image.h
        return self.world.get_tile(x, y) != 0

    def put_on_floor(self):
        x = self.x + self.sprite.image.w / 2
        y = int(self.y + self.sprite.image.h)
        tile = self.world.get_tile(x, y)
        while tile != 0:
            y -= 1
            tile = self.world.get_tile(x, y)
            print(2)
        self.y = y - self.sprite.image.h + 1



    def put_on_wall(self):
        x_right = int(self.x + self.sprite.image.w)  # Получаем крайнюю правую координату x
        x_left = int(self.x)  # Получаем крайнюю левую координату x
        y_bottom = int(self.y + self.sprite.image.h / 2)  #

        if self.velocity_x > 0:  # Движение вправо
            while self.world.get_tile(x_right, y_bottom) != 0:
                x_right -= 1
                print(4)
            self.x = x_right - self.sprite.image.w

        elif self.velocity_x < 0:  # Движение влево
            while self.world.get_tile(x_left, y_bottom) != 0:
                x_left += 1
                print(3)
            self.x = x_left


    def apply_friction(self):
        if not self.is_on_air:
            if self.velocity_x > 0:  # Движение вправо
                self.velocity_x -= self.T
                if self.velocity_x < 0:
                    self.velocity_x = 0
            elif self.velocity_x < 0:  # Движение влево
                self.velocity_x += self.T
                if self.velocity_x > 0:
                    self.velocity_x = 0

    def __str__(self):
        """
        Возвращает строковое представление объекта GameObject.

        :return: Строковое представление объекта.
        """
        return f'GameObject x = {self.x}, y = {self.y}'
