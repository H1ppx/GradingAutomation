from PyQt5.QtWidgets import QGridLayout, QGroupBox, QLabel, QLineEdit,QVBoxLayout, QWidget, QPushButton

class AddMCQWidget(QWidget):

    def __init__(self, parent=None):
        super(AddMCQWidget, self).__init__(parent)

        self.promptGroupBox()
        self.answerChoiceGroupBox()
        self.addGroupBox()

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.promptGroupBox, 1, 0)
        mainLayout.addWidget(self.answerChoiceGroupBox, 2, 0)
        mainLayout.addWidget(self.addGroupBox, 3, 0)

        self.setLayout(mainLayout)

    def promptGroupBox(self):
        self.promptGroupBox = QGroupBox("Prompt")
        self.promptLabel = QLabel("Prompt:")
        self.promptTextBox = QLineEdit()
        
        layout = QVBoxLayout() 
        layout.addWidget(self.promptLabel)
        layout.addWidget(self.promptTextBox)
        self.promptGroupBox.setLayout(layout)

    def answerChoiceGroupBox(self):
        self.answerChoiceGroupBox = QGroupBox("Answer Choices")
        self.correctLabel = QLabel("Correct Answer")
        self.correctTextBox = QLineEdit()
        self.wrong1Label = QLabel("Incorrect Answer 1")
        self.wrong1TextBox = QLineEdit()
        self.wrong2Label = QLabel("Incorrect Answer 2")
        self.wrong2TextBox = QLineEdit()
        self.wrong3Label = QLabel("Incorrect Answer 3")
        self.wrong3TextBox = QLineEdit()
        self.wrong4Label = QLabel("Incorrect Answer 4")
        self.wrong4TextBox = QLineEdit()

        layout = QVBoxLayout() 
        layout.addWidget(self.correctLabel)
        layout.addWidget(self.correctTextBox)
        layout.addWidget(self.wrong1Label)
        layout.addWidget(self.wrong1TextBox)
        layout.addWidget(self.wrong2Label)
        layout.addWidget(self.wrong2TextBox)
        layout.addWidget(self.wrong3Label)
        layout.addWidget(self.wrong3TextBox)
        layout.addWidget(self.wrong4Label)
        layout.addWidget(self.wrong4TextBox)
        self.answerChoiceGroupBox.setLayout(layout)

    def addGroupBox(self):
        self.addGroupBox = QGroupBox("Submit")
        self.saveButton = QPushButton("Save")
        self.cancelButton = QPushButton("Cancel")
        
        layout = QVBoxLayout() 
        layout.addWidget(self.saveButton)
        layout.addWidget(self.cancelButton)
        self.addGroupBox.setLayout(layout)