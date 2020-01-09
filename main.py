import random
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication

from py_ui import Ui_MainWindow


class MainW(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.circles = []
        self.draw = False
        self.pushButton.clicked.connect(self.random_circle)

    def random_circle(self):
        self.draw = True
        self.circles.append([(random.randrange(0, 800), random.randrange(0, 500)), random.randrange(10, 300),
                             (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))])
        self.update()

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            for el in self.circles:
                qp.setBrush(QColor(*el[2]))
                self.draw_circle(qp, el)
            qp.end()

    def draw_circle(self, qp, params):
        qp.drawEllipse(*params[0], params[1], params[1])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_w = MainW()
    main_w.show()
    sys.exit(app.exec())
