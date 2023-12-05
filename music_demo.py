from pygame import mixer  # мой микшер, без него не будет музыки(

import sys

from PyQt5 import uic  # Импортируем uic (надо)
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('interface.ui', self)  # Загружаем дизайн
        self.pausing = False
        self.flag = False
        self.init_mixer()
        self.startMusic.clicked.connect(self.start_music)  # старт музыки по кнопке
        self.slider.valueChanged.connect(self.set_position)  #
        self.musicvolume.valueChanged.connect(self.change_volume)  # ползунок громкости
        self.pauseMusic.clicked.connect(self.pause_music)

    @staticmethod
    def init_mixer():
        mixer.init()  # запуск проигрывателя (иначе вылет от каждого чиха)
        mixer.music.set_volume(0.25)  # установка НОРМАЛЬНОЙ громкости
        song = 'Eye Of The_Storm.mp3'  # заглушка в виде моего любимого трека)
        mixer.music.load(song)  # загрузка трека (иначе вылет)

    def start_music(self):  # запуск сначала
        mixer.music.play()
        self.flag = True
        self.pausing = True

    def pause_music(self):  # остановка и продолжение
        if self.pausing:
            mixer.music.pause()
            self.pauseMusic.setText('Continue')
            self.pausing = False
        else:
            mixer.music.unpause()
            self.pauseMusic.setText('Pause')
            self.pausing = True

    @staticmethod  # PEP8 жалуется
    def change_volume(volume):  # изменение громкости ползунком
        mixer.music.set_volume(volume / 100)

    def set_position(self, position):  # перематывание трека (BETA ver.)
        if self.flag:  # заглушка чтобы не вылетало
            mixer.music.set_pos(position)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
