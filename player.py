from game_object import GameObject
from graphics import KEY_LEFT, KEY_RIGHT, KEY_UP
from skull import Skull
from the_world import World

class Player(GameObject):
    speed_x = 10
    speed_y = 25
    def __init__(self, world, sprite, key_pressed, pos_x, pos_y):
        """
        Инициализация объекта игрока.

        :param sprite: Спрайт игрока.
        :param key_pressed: Функция для проверки, какие клавиши нажаты.
        """
        super().__init__(world, sprite, 14, 19, pos_x, pos_y)
        self.key_pressed = key_pressed
        self.gravity = 7  # Значение гравитации


    def update(self):
        """
        Обновление состояния игрока на основе нажатых клавиш.

        """

        if self.key_pressed(KEY_UP) and not self.is_on_air:
            # self.is_jumping = True
            self.velocity_y = -self.speed_y  # Устанавливаем вертикальную скорость прыжка

        if self.key_pressed(KEY_LEFT):
            self.velocity_x = -self.speed_x
            self.sprite.flip_x = True
        elif self.key_pressed(KEY_RIGHT):
            self.velocity_x = self.speed_x
            self.sprite.flip_x = False
        #else:
        #    self.velocity_x = 0

        super().update()

    def handle_collision(self, other_object):
        """
        Определение поведения при столкновении с другим объектом GameObject.

        :param other_object: Другой объект GameObject, участвующий в столкновении.
        """
        if isinstance(other_object, Skull):
            # поведение при столкновении с Skull
            if other_object in self.world.objects:
                other_object.death()
            print("Игрок столкнулся с черепом!")

