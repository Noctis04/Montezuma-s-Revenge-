
class Sprite:
    def __init__(self, file_name, pos_x=0, pos_y=0, start_x=0, start_y=0, height=None, width=None):
        """

        Инициализирует объект Sprite.

        :param file_name: Имя файла изображения.
        :param start_x: Начальная позиция по оси X на изображении.
        :param start_y: Начальная позиция по оси Y на изображении.
        :param height: Высота спрайта.
        :param width: Ширина спрайта.
        :param pos_x: Начальная позиция спрайта по оси X.
        :param pos_y: Начальная позиция спрайта по оси Y.
        """
        self.image = None
        self.file_name = file_name
        self.x = pos_x
        self.y = pos_y
        self.start_x = start_x
        self.start_y = start_y
        self.height = height
        self.width = width
        self.flip_x = False

    def update(self):
        pass
#[(0, 0, 14, 10), (20, 0, 20, 20)]
