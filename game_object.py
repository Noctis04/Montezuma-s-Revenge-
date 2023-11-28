from state import State

class GameObject(State):
    G = 9.8 / 5
    T = 3.0

    def __init__(self, world, sprite, width, height, pos_x=0, pos_y=0, velocity_x=0, velocity_y=0, fly=False):
        """

        Инициализирует объект GameObject.

        :param world: Экземпляр класса, представляющий мир, в котором находится объект.
        :param sprite: Спрайт, связанный с объектом.
        :param width: Ширина объекта.
        :param height: Высота объекта.
        :param pos_x: Начальная позиция по оси X.
        :param pos_y: Начальная позиция по оси Y.
        :param velocity_x: Начальная скорость по оси X.
        :param velocity_y: Начальная скорость по оси Y.
        :param fly: Флаг, указывающий, может ли объект летать (по умолчанию False).
        """
        super().__init__()
        self.world = world
        self.sprite = sprite
        self.width = width
        self.height = height
        self.x = pos_x
        self.y = pos_y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.fly = fly
        self.is_on_air = False

    def update(self):
        """
        Обновляет состояние объекта GameObject.

        """
        self.run_state()
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
        if self.velocity_x != 0:
            self.collision_with_wall()
        #if not self.is_on_air:
        if not self.fly:
            self.put_on_floor()
            self.apply_friction()
        self.sprite.x = int(self.x)
        self.sprite.y = int(self.y)
        for game_object in self.world.objects:
            if game_object != self:  # Проверяем столкновение с другими объектами, исключая самого себя
                if self.check_collision(game_object):
                    self.handle_collision(game_object)



    def apply_gravity(self):
        """
          Применяет гравитацию к объекту.
        """
        self.velocity_y += self.G

    def on_ground(self):
        """
          Проверяет, находится ли объект на земле.
        """
        x = self.x + self.width / 2
        y = self.y + self.height
        return self.world.get_tile(x, y) != 0

    def put_on_floor(self):
        """
         Ставит объект на землю(обработка столкновения с сземлёй).
        """
        x = self.x + self.width / 2
        y = int(self.y + self.height)
        tile = self.world.get_tile(x, y)
        while tile != 0:
            y -= 1
            tile = self.world.get_tile(x, y)
        self.y = y - self.height + 1

    def check_collision(self, other_object):
        """
        Проверяет столкновение с другим объектом GameObject.

        :param other_object: Другой объект GameObject для проверки столкновения.
        :return: True, если есть столкновение, в противном случае - False..
        """
        if (
                self.x < other_object.x + other_object.width
                and self.x + self.width > other_object.x
                and self.y < other_object.y + other_object.height
                and self.y + self.height > other_object.y
        ):
            return True
        return False

    def handle_collision(self, other_object):
        """
        Определение поведения при столкновении с другим объектом GameObject.

        :param other_object: Другой объект GameObject, участвующий в столкновении.
        """
        pass  # Переопределяем этот метод в подклассах

    def collision_with_wall(self):
        """
        Обрабатывает столкновение с стеной.
        """
        x_right = int(self.x + self.width)
        x_left = int(self.x)
        y_bottom = int(self.y + self.height / 2)
        if not self.is_on_air:
            if self.velocity_x > 0 and self.world.get_tile(x_right, y_bottom) != 0:  # Движение вправо
                while self.world.get_tile(x_right, y_bottom) != 0:
                    x_right -= 1
                self.x = x_right - self.width
                self.velocity_x = 0
            elif self.velocity_x < 0 and self.world.get_tile(x_left, y_bottom) != 0:  # Движение влево
                while self.world.get_tile(x_left, y_bottom) != 0:
                    x_left += 1
                self.x = x_left + 1  # Изменено на x_left + 1


    def apply_friction(self):
        """
        Применяет трение к объекту.
        """
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
