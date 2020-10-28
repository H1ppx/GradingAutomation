from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)

import PyQt5
import sys

class WidgetGallery(QDialog):

    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

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
        self.setWindowTitle("Grading Automation")

    def modeGroupBox(self):
        self.modeGroupBox = QGroupBox("Mode")
        self.currentModeLabel = QLabel("Current Mode: Create")
        self.switchModeButton = QPushButton("Switch Mode")
        
        self.switchModeButton.clicked.connect(self.switchMode) 

        layout = QVBoxLayout() 
        layout.addWidget(self.currentModeLabel)
        layout.addWidget(self.switchModeButton)
        self.modeGroupBox.setLayout(layout)

    def switchMode(self):
        if(self.currentModeLabel.text() == "Current Mode: Create"):
            self.currentModeLabel.setText("Current Mode: Grade")
        else:
            self.currentModeLabel.setText("Current Mode: Create")

        
    def headerInfoGroupBox(self):
        self.headerInfoGroupBox = QGroupBox("Header")
        self.subjectLabel = QLabel("Subject:")
        self.subjectTextBox = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.subjectLabel)
        layout.addWidget(self.subjectTextBox)
        self.headerInfoGroupBox.setLayout(layout)

    def multipleChoiceGroupBox(self):
        self.multipleChoiceGroupBox = QGroupBox("Multiple Choice Question")
        self.counterMCQLabel = QLabel("Amount of MCQ's: 0")
        self.addMCQ = QPushButton("Add")
        self.editMCQ = QPushButton("Edit")
        self.deleteMCQ = QPushButton("Delete")     

        layout = QVBoxLayout()
        layout.addWidget(self.counterMCQLabel)
        layout.addWidget(self.addMCQ)
        layout.addWidget(self.editMCQ)
        layout.addWidget(self.deleteMCQ)
        self.multipleChoiceGroupBox.setLayout(layout)
        
        # TODO: Add functionality to Buttons

    def freeResponseGroupBox(self):
        self.freeResponseGroupBox = QGroupBox("Free-Response Question")
        self.counterFRQLabel = QLabel("Amount of FRQ's: 0")
        self.addFRQ = QPushButton("Add")
        self.editFRQ = QPushButton("Edit")
        self.deleteFRQ = QPushButton("Delete")     

        layout = QVBoxLayout()
        layout.addWidget(self.counterFRQLabel)
        layout.addWidget(self.addFRQ)
        layout.addWidget(self.editFRQ)
        layout.addWidget(self.deleteFRQ)
        self.freeResponseGroupBox.setLayout(layout)

        # TODO: Add functionality to Buttons
        
    def selectAnswerKeyGroupBox(self):
        # TODO
        print("TODO")

    def geCompletedTestGroupBox(self):
        # TODO
        print("TODO")


    def submitGroupBox(self):
        self.submitGroupBox = QGroupBox("Submit")
        self.submitButton = QPushButton("Submit")

        layout = QVBoxLayout()
        layout.addWidget(self.submitButton)
        self.submitGroupBox.setLayout(layout)

if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    app.exec_()