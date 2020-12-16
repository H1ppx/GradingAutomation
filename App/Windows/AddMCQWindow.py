from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from PyQt5.QtCore import Qt 

from Widgets.AddMCQWidget import AddMCQWidget

class AddMCQWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AddMCQWindow, self).__init__(parent)

        self.setWindowModality(Qt.ApplicationModal)

        self.setWindowTitle("Add MCQ")

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
    
        self.addMCQWidget = AddMCQWidget(self)

        self.central_widget.addWidget(self.addMCQWidget)
