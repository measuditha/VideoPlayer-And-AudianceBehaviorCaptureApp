from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QStyle, QSlider, \
    QFileDialog
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl
import cv2
import sys


class Player(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("player.ico"))
        self.setWindowTitle("Behaviour Capturer")
        self.setGeometry(350, 100, 700, 500)

        p = self.palette()
        p.setColor(QPalette.Window, Qt.white)
        self.setPalette(p)
        self.create_player()

    def create_player(self):
        # Main Window
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videowidget = QVideoWidget()

        # Open video Button
        self.openBtn = QPushButton('Open Video')
        self.openBtn.clicked.connect(self.open_file)

        # Play Video Button
        self.playBtn = QPushButton('Play')
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)

        # Video Slider Bar
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)

        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)

        hbox.addWidget(self.openBtn)
        hbox.addWidget(self.playBtn)
        hbox.addWidget(self.slider)

        vbox = QVBoxLayout()
        vbox.addWidget(videowidget)
        vbox.addLayout(hbox)

        self.mediaPlayer.setVideoOutput(videowidget)

        self.setLayout(vbox)

        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")

        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)

    def capture(self):
        filename = 'footage.mp4'
        frames_per_seconds = 24.0
        res = '720p'

        def change_res(cap, width, height):
            cap.set(3,width)
            cap.set(4, height)

        STD_DIMENSIONS = {
            "720p":(640, 480)
        }

        def get_dims(cap, res='720p'):
            width, height = STD_DIMENSIONS['720p']
            if res in STD_DIMENSIONS:
                width, height = STD_DIMENSIONS[res]
            change_res(width, height)
            return width, height


        cap = cv2.VideoCapture(0)
        dims = get_dims(cap, res=res)

        while(True):
            ret, frame = cap.read()

            cv2.imshow('frame', frame)
            if cv2.waitkey(20) & 0xFF == ord('q'):
                    break
        cap.release()
        cv2.destroyAllWindows()

    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
            self.capture()
        else:
            self.mediaPlayer.play()
            self.capture()

    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))

        else:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def position_changed(self, position):
        self.slider.setValue(position)

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)


app = QApplication(sys.argv)
player = Player()
player.show()
sys.exit(app.exec_())
