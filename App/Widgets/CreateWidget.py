from PyQt5.QtWidgets import (QGridLayout, QGroupBox, QLabel, QLineEdit,
        QPushButton, QVBoxLayout, QWidget)

from Windows.AddMCQWindow import AddMCQWindow
from Windows.AddFRQWindow import AddFRQWindow

from Utils.Exam import Exam

class CreateWidget(QWidget):

    def __init__(self, parent=None):
        super(CreateWidget, self).__init__(parent)

        self.modeGroupBox()
        self.headerInfoGroupBox()
        self.multipleChoiceGroupBox()
        self.freeResponseGroupBox()
        self.submitGroupBox()

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.modeGroupBox, 0, 0, 1, 2)
        mainLayout.addWidget(self.headerInfoGroupBox, 1, 0)
        mainLayout.addWidget(self.multipleChoiceGroupBox, 1, 1)
        mainLayout.addWidget(self.freeResponseGroupBox, 2, 0)
        mainLayout.addWidget(self.submitGroupBox, 2, 1)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        self.exam = Exam()

    def modeGroupBox(self):
        self.modeGroupBox = QGroupBox("Mode")
        self.currentModeLabel = QLabel("Current Mode: Create")
        self.switchModeButton = QPushButton("Switch Mode")
        
        layout = QVBoxLayout() 
        layout.addWidget(self.currentModeLabel)
        layout.addWidget(self.switchModeButton)
        self.modeGroupBox.setLayout(layout)
        
    def headerInfoGroupBox(self):
        self.headerInfoGroupBox = QGroupBox("Header")
        self.courseLabel = QLabel("Course:")
        self.subjectLabel = QLabel("Subject:")

        self.courseTextBox = QLineEdit()
        self.subjectTextBox = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.courseLabel)
        layout.addWidget(self.courseTextBox)
        layout.addWidget(self.subjectLabel)
        layout.addWidget(self.subjectTextBox)
        self.headerInfoGroupBox.setLayout(layout)

    def multipleChoiceGroupBox(self):
        self.multipleChoiceGroupBox = QGroupBox("Multiple Choice Question")
        self.counterMCQLabel = QLabel("Amount of MCQ's: 0")
        self.addMCQButton = QPushButton("Add")
        self.editMCQButton = QPushButton("Edit")
        self.deleteMCQButton = QPushButton("Delete")     

        self.addMCQButton.clicked.connect(self.addMCQAction)

        layout = QVBoxLayout()
        layout.addWidget(self.counterMCQLabel)
        layout.addWidget(self.addMCQButton)
        layout.addWidget(self.editMCQButton)
        layout.addWidget(self.deleteMCQButton)
        self.multipleChoiceGroupBox.setLayout(layout)
        
        # TODO: Add functionality to Buttons

    def freeResponseGroupBox(self):
        self.freeResponseGroupBox = QGroupBox("Free-Response Question")
        self.counterFRQLabel = QLabel("Amount of FRQ's: 0")
        self.addFRQButton = QPushButton("Add")
        self.editFRQButton = QPushButton("Edit")
        self.deleteFRQButton = QPushButton("Delete")     

        self.addFRQButton.clicked.connect(self.addFRQAction)

        layout = QVBoxLayout()
        layout.addWidget(self.counterFRQLabel)
        layout.addWidget(self.addFRQButton)
        layout.addWidget(self.editFRQButton)
        layout.addWidget(self.deleteFRQButton)
        self.freeResponseGroupBox.setLayout(layout)

        self.addMCQWindow = AddMCQWindow(self)
        self.addFRQWindow = AddFRQWindow(self)
        # TODO: Add functionality to Buttons

    def addMCQAction(self):
        self.addMCQWindow.show()

    def addFRQAction(self):
        self.addFRQWindow.show()

    def submitGroupBox(self):
        self.submitGroupBox = QGroupBox("Finish")
        self.saveButton = QPushButton("Save")
        self.downloadButton = QPushButton("Download")

        self.downloadButton.clicked.connect(self.downloadButtonAction) 

        layout = QVBoxLayout()
        layout.addWidget(self.saveButton)
        layout.addWidget(self.downloadButton)
        self.submitGroupBox.setLayout(layout)

    def downloadButtonAction(self):
        self.exam.course = self.courseTextBox.text()
        self.exam.subject = self.subjectTextBox.text()
        self.exam.generateExam()