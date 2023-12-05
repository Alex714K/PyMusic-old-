import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from myplayer import Ui_MainWindow  # импорт всего сгенерированного файла
from myplaylist import Ui_MainPlaylist
from mysetting import Ui_MainSetting
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog, QAction

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl
# почти все импорты временны и большая часть убирётся


class PlayList(QtWidgets.QMainWindow):
    def __init__(self):
        super(PlayList, self).__init__()
        self.uiP = Ui_MainPlaylist()
        self.uiP.setupUi(self)
        self.init_ui()

    def init_ui(self):
        pass





class Settings(QtWidgets.QMainWindow):
    def __init__(self):
        super(Settings, self).__init__()
        self.uiS = Ui_MainSetting()
        self.uiS.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.open_settings_txt()
        self.set_color()

        self.uiS.left_red.clicked.connect(self.red_left)
        self.uiS.left_green.clicked.connect(self.green_left)
        self.uiS.left_blue.clicked.connect(self.blue_left)
        self.uiS.right_red.clicked.connect(self.red_right)
        self.uiS.right_green.clicked.connect(self.green_right)
        self.uiS.right_blue.clicked.connect(self.blue_right)

    def open_settings_txt(self):
        setting_txt = open("settings.txt").read().split('\n')
        self.red = setting_txt[0][4:]
        self.green = setting_txt[1][5:]
        self.blue = setting_txt[2][6:]
        self.folder = setting_txt[3][7:]

    def set_color(self):
        self.uiS.lineRed.setText(self.red)
        self.uiS.lineBlue.setText(self.blue)
        self.uiS.lineGreen.setText(self.green)

    def red_left(self):
        self.red -= 1

    def red_right(self):
        self.red += 1

    def green_left(self):
        self.blue -= 1

    def green_right(self):
        self.blue += 1

    def blue_left(self):
        self.green -= 1

    def blue_right(self):
        self.green += 1


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # подключаем интерфейс
        self.init_ui()

    def init_ui(self):
        """Основная инициализация"""
        # создаём проигрыватель
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        # флажки
        self.playing = False

        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile('Eye Of The_Storm.mp3')))  # временно

        self.ui.openAudio.clicked.connect(self.open_file)
        self.ui.playlist.triggered.connect(self.open_playlists)
        self.ui.playButton.clicked.connect(self.pause_music)
        self.ui.win_options.triggered.connect(self.open_parametr)

    def b(self):
        """затычка"""
        pass

    def open_parametr(self):
        self.wpar = Settings()
        self.wpar.show()
    def open_playlists(self):
        '''Открывает окно с библиотекой'''
        self.wplay = PlayList()
        self.wplay.show()

    def pause_music(self):
        '''Остановить или воспроизвести музыку'''
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()  # остановить
            self.ui.playButton.setText('Play')
        else:
            self.mediaPlayer.play()  # продолжить
            self.ui.playButton.setText('Stop')

    def open_file(self):
        """Открыть окно для выбора файла"""
        filename, _ = QFileDialog.getOpenFileName(self, "Open music")
        print(filename)
        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.ui.playButton.setText("Play")


if __name__ == "__main__":
    import sys

app = QtWidgets.QApplication(sys.argv)
application = MyWindow()
application.show()
sys.exit(app.exec())
