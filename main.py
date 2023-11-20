import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from myplaylist import Ui_MainPlaylist
from myplayer import Ui_MainWindow  # импорт нашего сгенерированного файла
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog, QAction
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl


class PlayList(QtWidgets.QMainWindow):
    def __init__(self):
        super(PlayList, self).__init__()
        self.uiP = Ui_MainPlaylist()
        self.uiP.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.connection = sqlite3.connect("base.sqlite")

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # подключаем интерфейс
        self.init_ui()

    def init_ui(self):

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)  # создаём проигрыватель

        self.playing = False

        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile('Eye Of The_Storm.mp3')))  # временно

        self.ui.openVideo.clicked.connect(self.open_file)
        self.ui.playlist.triggered.connect(self.open_playlists)
        self.ui.playButton.clicked.connect(self.pause_music)

    def b(self):
        pass

    def open_playlists(self):  # открыть окно с плейлистом
        self.application = PlayList()
        self.application.show()

    def pause_music(self):  # воспроизведение музыки
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()  # остановить
            self.ui.playButton.setText('Play')
        else:
            self.mediaPlayer.play()  # продолжить
            self.ui.playButton.setText('Stop')

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open music")
        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()
sys.exit(app.exec())
