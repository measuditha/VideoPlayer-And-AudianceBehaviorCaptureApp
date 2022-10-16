from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
import sys

class Player(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon("player.ico"))






app = QApplication(sys.argv)
player = Player()
player.show()
sys.exit(app.exec_())
