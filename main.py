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


def b(self):
    """Затычка"""
    pass


class PlayList(QtWidgets.QMainWindow):
    '''Окно плейлиста (скорей библиотека со всеми треками)'''
    def __init__(self):
        super(PlayList, self).__init__()
        self.uiP = Ui_MainPlaylist()
        self.uiP.setupUi(self)
        self.init_ui()

    def init_ui(self):
        """Основная инициализация"""
        pass


class Settings(QtWidgets.QMainWindow):
    '''Окно настроек'''
    def __init__(self):
        super(Settings, self).__init__()
        self.uiS = Ui_MainSetting()
        self.uiS.setupUi(self)
        self.init_ui()

    def init_ui(self):
        """Основная инициализация"""
        self.uiS.confirm_button.setDisabled(1)
        self.uiS.activate_button.setDisabled(1)

        self.open_settings_txt()

        self.set_settings_in_lines()
        # кнопки изменения цветов
        self.uiS.left_red.clicked.connect(self.red_left)
        self.uiS.left_green.clicked.connect(self.green_left)
        self.uiS.left_blue.clicked.connect(self.blue_left)
        self.uiS.right_red.clicked.connect(self.red_right)
        self.uiS.right_green.clicked.connect(self.green_right)
        self.uiS.right_blue.clicked.connect(self.blue_right)
        # кнопки подтверждения/отмены
        self.uiS.cancel_button.clicked.connect(self.cancel)
        self.uiS.activate_button.clicked.connect(self.activate)
        self.uiS.confirm_button.clicked.connect(self.confirm)

        self.uiS.lineRed.textChanged.connect(self.activate_buttons)
        self.uiS.lineGreen.textChanged.connect(self.activate_buttons)
        self.uiS.lineBlue.textChanged.connect(self.activate_buttons)

    def open_settings_txt(self):
        '''Открытие файла с сохранёнными настройками'''
        setting_txt = open("settings.txt").read().split('\n')
        self.red = int(setting_txt[0][4:])
        self.green = int(setting_txt[1][6:])
        self.blue = int(setting_txt[2][5:])
        self.folder = setting_txt[3][7:]

    def cancel(self):
        self.close()

    def activate(self):
        settins_txt = open("settings.txt", 'w')
        settins_txt.write(f"red={self.red}\n"
                          f"green={self.blue}\n"
                          f"blue={self.green}\n"
                          f"folder={self.folder}")
        settins_txt.close()
        self.uiS.activate_button.setDisabled(1)
        self.uiS.confirm_button.setDisabled(1)

    def confirm(self):
        settins_txt = open("settings.txt", 'w')
        settins_txt.write(f"red={self.red}\n"
                          f"green={self.blue}\n"
                          f"blue={self.green}\n"
                          f"folder={self.folder}")
        settins_txt.close()
        self.uiS.activate_button.setDisabled(1)
        self.uiS.confirm_button.setDisabled(1)
        self.close()

    def activate_buttons(self):
        self.uiS.activate_button.setEnabled(1)
        self.uiS.confirm_button.setEnabled(1)
        self.color_changed()

    def set_settings_in_lines(self):
        '''Вставить параметры в строки'''
        self.uiS.lineRed.setText(str(self.red))
        self.uiS.lineBlue.setText(str(self.blue))
        self.uiS.lineGreen.setText(str(self.green))
        self.uiS.line_folder.setText(self.folder)

    def color_changed(self):
        self.red = int(self.uiS.lineRed.text())
        self.green = int(self.uiS.lineGreen.text())
        self.blue = int(self.uiS.lineBlue.text())

    def red_left(self):
        self.red -= 1
        self.uiS.lineRed.setText(str(self.red))

    def red_right(self):
        self.red += 1
        self.uiS.lineRed.setText(str(self.red))

    def green_left(self):
        self.green -= 1
        self.uiS.lineGreen.setText(str(self.green))

    def green_right(self):
        self.green += 1
        self.uiS.lineGreen.setText(str(self.green))

    def blue_left(self):
        self.blue -= 1
        self.uiS.lineBlue.setText(str(self.blue))

    def blue_right(self):
        self.blue += 1
        self.uiS.lineBlue.setText(str(self.blue))


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

    def open_parametr(self):
        '''Открывает окно с настройками'''
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
