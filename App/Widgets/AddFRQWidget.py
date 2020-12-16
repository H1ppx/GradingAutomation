from PyQt5.QtWidgets import QGridLayout, QGroupBox, QLabel, QLineEdit,QVBoxLayout, QWidget

class AddFRQWidget(QWidget):

    def __init__(self, parent=None):
        super(AddFRQWidget, self).__init__(parent)

        self.promptGroupBox()

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.promptGroupBox, 0, 1)
        self.setLayout(mainLayout)

    def promptGroupBox(self):
        self.promptGroupBox = QGroupBox("Prompt")
        self.promptLabel = QLabel("Prompt:")
        self.promptTextBox = QLineEdit()
        
        layout = QVBoxLayout() 
        layout.addWidget(self.promptLabel)
        layout.addWidget(self.promptTextBox)
        self.promptGroupBox.setLayout(layout)