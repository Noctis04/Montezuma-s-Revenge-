from sprite import Sprite

class Animation(Sprite):
    def __init__(self, file_name, frames, pos_x, pos_y, speed=1, cycle=True, back=False):
        """
        Инициализирует объект анимации.

        :param file_name: Имя файла изображения.
        :param frames: Последовательность кадров анимации.
        :param pos_x: Начальная позиция по оси X.
        :param pos_y: Начальная позиция по оси Y.
        :param speed: Скорость смены кадров (по умолчанию 1).
        :param cycle: Флаг циклического воспроизведения анимации (по умолчанию True).
        :param back: Флаг воспроизведения анимации задом наперед (по умолчанию False).
        """
        super().__init__(file_name, 0, 0, 0, 0, pos_x, pos_y)
        self.speed = speed  # Устанавливаем скорость анимации
        self.counter = self.speed  # Инициализируем счетчик кадров
        self.frames = frames  # Устанавливаем последовательность кадров анимации
        self.frame = 0  # Устанавливаем текущий кадр
        self.cycle = cycle  # Определяем, будет ли анимация циклической
        self.back = back  # Определяем, будет ли анимация проигрываться задом наперед
        self.setup_frame()  # Инициализируем первый кадр

    def setup_frame(self):
        """
        Устанавливает параметры текущего кадра.
        """
        (self.start_x, self.start_y, self.width, self.height) = self.frames[self.frame]

    def update(self):
        """
        Обновляет состояние анимации.
        """
        self.counter -= 1  # Уменьшаем счетчик кадров
        if self.counter == 0:
            self.counter = self.speed  # Сбрасываем счетчик кадров до начального значения
            if self.back:
                self.frame -= 1  # Переключаемся на предыдущий кадр, если анимация идет задом наперед
            else:
                self.frame += 1  # Переключаемся на следующий кадр, если анимация идет вперед
            if self.frame == len(self.frames):
                self.frame = 0 if self.cycle else len(self.frames) - 1  # Обрабатываем циклическое воспроизведение
            elif self.frame < 0:
                self.frame = len(self.frames) - 1 if self.cycle else 0  # Обрабатываем циклическое воспроизведение задом наперед
        self.setup_frame()  # Обновляем параметры текущего кадра
