class Sprite:
    def __init__(self, image, pos_x, pos_y):
        """
        Инициализация спрайта.

        :param image: Изображение спрайта.
        :param pos_x: Начальная позиция по оси X.
        :param pos_y: Начальная позиция по оси Y.
        """
        self.image = image
        self.x = pos_x
        self.y = pos_y
