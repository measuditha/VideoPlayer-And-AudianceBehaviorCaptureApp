from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon, QPalette
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





app = QApplication(sys.argv)
player = Player()
player.show()
sys.exit(app.exec_())
