from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QStyle, QSlider,QFileDialog
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl
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

        # Open video Button
        self.openBtn = QPushButton('Open Video')
        self.openBtn.clicked.connect(self.open_file())

        # Play Video Button
        self.playBtn = QPushButton('Play')
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)

        hbox = QHBoxLayout()
        hbox.setContentsMargins(0,0,0,0)

        hbox.addWidget(self.openBtn)
        hbox.addWidget(self.playBtn)
        hbox.addWidget(self.slider)

        vbox = QVBoxLayout()
        vbox.addWidget(videowidget)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self,"Open Video")

        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)

app = QApplication(sys.argv)
player = Player()
player.show()
sys.exit(app.exec_())
