from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from PyQt5.QtCore import Qt 

from Widgets.AddFRQWidget import AddFRQWidget

class AddFRQWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AddFRQWindow, self).__init__(parent)

        self.setWindowModality(Qt.ApplicationModal)

        self.setWindowTitle("Add FRQ")

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
    
        self.addFRQWidget = AddFRQWidget(self)

        self.central_widget.addWidget(self.addFRQWidget)
