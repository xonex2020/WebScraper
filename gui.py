import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

w = QWidget()
w.setGeometry(50,50,700,400)
w.setWindowTitle("Fuel-oil Web-Scraper")
w.setWindowIcon(QIcon("heatingoil-icon.png"))

w.show()

sys.exit(app.exec())
