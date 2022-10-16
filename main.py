from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt
import sys

class Player(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon("player.ico"))
        self.setWindowTitle("Behaviour Capturer")
        self.setGeometry(350,100,700,500)

        p = self.palette()
        p.setColor(QPalette.Window, Qt.white)
        self.setPalette(p)

        self.create_player()

    def create_player(self):
        self.mediaPlayer = QMediaPlayer(None,QMediaPlayer.VideoSurface)
        videowidget = QVideoWidget()

        self.openBtn = QPushButton('Open Video')

        hbox = QHBoxLayout()
        hbox.setContentsMargins(0,0,0,0)

        hbox.addWidget(self.openBtn)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)

        self.setLayout(vbox)

app = QApplication(sys.argv)
player = Player()
player.show()
sys.exit(app.exec_())
