from PyQt5.QtWidgets import (QGridLayout, QGroupBox, QLabel,
        QPushButton, QVBoxLayout, QWidget)

class GradeWidget(QWidget):

    def __init__(self, parent=None):
        super(GradeWidget, self).__init__(parent)

        self.modeGroupBox()
        self.answerKeyGroupBox()
        self.completedTestGroupBox()
        self.gradeGroupBox()

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.modeGroupBox, 0, 0, 1, 2)
        mainLayout.addWidget(self.answerKeyGroupBox, 1, 0)
        mainLayout.addWidget(self.completedTestGroupBox, 1, 1)
        mainLayout.addWidget(self.gradeGroupBox, 2, 0)
        self.setLayout(mainLayout)

    def modeGroupBox(self):
        self.modeGroupBox = QGroupBox("Mode")
        self.currentModeLabel = QLabel("Current Mode: Grade")
        self.switchModeButton = QPushButton("Switch Mode")

        layout = QVBoxLayout() 
        layout.addWidget(self.currentModeLabel)
        layout.addWidget(self.switchModeButton)
        self.modeGroupBox.setLayout(layout)

    def answerKeyGroupBox(self):
        self.answerKeyGroupBox = QGroupBox("Answer Key")
        self.uploadAnsKeyButton = QPushButton("Upload from Desktop")
        self.downloadAnsKeyButton = QPushButton("Download from Cloud")

        layout = QVBoxLayout() 
        layout.addWidget(self.uploadAnsKeyButton)
        layout.addWidget(self.downloadAnsKeyButton)
        self.answerKeyGroupBox.setLayout(layout)

    def completedTestGroupBox(self):
        self.completedTestGroupBox = QGroupBox("Student Exam(s)")
        self.uploadStudentButton = QPushButton("Upload from Desktop")
        self.downloadStudentButton = QPushButton("Download from Cloud")

        layout = QVBoxLayout() 
        layout.addWidget(self.uploadStudentButton)
        layout.addWidget(self.downloadStudentButton)
        self.completedTestGroupBox.setLayout(layout)
    
    def gradeGroupBox(self):
        self.gradeGroupBox = QGroupBox("Grading")
        self.gradeButton = QPushButton("Grade w/o Free Response")
        self.gradeWithFRQButton = QPushButton("Grade w/ Free Response")

        layout = QVBoxLayout() 
        layout.addWidget(self.gradeButton)
        layout.addWidget(self.gradeWithFRQButton)
        self.gradeGroupBox.setLayout(layout)