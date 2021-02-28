from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Downloader(QDialog):
    def __init__(self):
        QDialog.__init__(self)


        layout = QFormLayout()

        line = QLineEdit()
        file = QLineEdit()
        progressbar = QProgressBar()
        OK = QPushButton("OK")

        layout.addWidget(line)
        layout.addWidget(file)
        layout.addWidget(progressbar)
        layout.addWidget(OK)

        line.setPlaceholderText("url")
        file.setPlaceholderText("file")

        self.setLayout(layout)
        self.setWindowTitle("App")

        OK.clicked.connect(self.close)

app = QApplication(sys.argv)
downloader = Downloader()
downloader.show()
app.exec_()