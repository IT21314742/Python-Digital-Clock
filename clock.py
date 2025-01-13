import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(800, 500, 500, 500)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        # Corrected Alignment Enum
        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size: 150px;"
                                      "font-family: Arial;"
                                      "color: hsl(111,100%, 50%);")
        self.setStyleSheet("background-color: black;")

        def update_time(self):
            current_time = QTime.currentTime().toString("hh:mm:ss")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
