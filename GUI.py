from __future__ import print_function, unicode_literals
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QMainWindow, QStackedWidget, QMessageBox)

import PyQt5
import sys

import numpy as np
import pyqrcode
import tkinter as tk
import cv2
import random
from numpy.lib.function_base import append

from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError, print_json
from pylatex import Document, Section, Subsection, Command, Figure
from pylatex.utils import italic, NoEscape
from pylatex.package import Package
from tkinter.filedialog import askopenfilename
from PIL import Image


class Controller(QMainWindow):

    def __init__(self, parent=None):
        super(Controller, self).__init__(parent)
    
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
    
        self.createWindow = CreateWindow(self)
        self.gradeWindow = GradeWindow(self)

        self.createWindow.switchModeButton.clicked.connect(self.switch)
        self.gradeWindow.switchModeButton.clicked.connect(self.switch)
        
        self.central_widget.addWidget(self.createWindow)
        self.central_widget.addWidget(self.gradeWindow)

        self.central_widget.setCurrentWidget(self.createWindow)
        self.gradeMode = False

        self.setWindowTitle("Grading Automation")

    def switch(self):
        if(self.gradeMode):
            self.central_widget.setCurrentWidget(self.createWindow)
            self.gradeMode = False
        else:
            self.central_widget.setCurrentWidget(self.gradeWindow)
            self.gradeMode = True

class CreateWindow(QWidget):

    def __init__(self, parent=None):
        super(CreateWindow, self).__init__(parent)

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

        self.addFRQWindow = AddFRQWindow(self)
        # TODO: Add functionality to Buttons

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
        
class GradeWindow(QWidget):

    def __init__(self, parent=None):
        super(GradeWindow, self).__init__(parent)

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
       
class AddFRQWindow(QMainWindow):

    def __init__(self, parent=None):
        super(AddFRQWindow, self).__init__(parent)

        # self.promptGroupBox()

        mainLayout = QGridLayout()
        # mainLayout.addWidget(self.promptGroupBox, 0, 1)
        self.setLayout(mainLayout)

    def promptGroupBox(self):
        self.promptGroupBox = QGroupBox("Prompt")
        self.promptLabel = QLabel("Prompt:")
        self.promptTextBox = QLineEdit()
        
        layout = QVBoxLayout() 
        layout.addWidget(self.promptLabel)
        layout.addWidget(self.promptTextBox)
        # self.promptGroupBox.setLayout(layout)
        

class MCQ():

    def __init__(self, prompt, correctAnswer, *incorrectAnswers):
        self.prompt = prompt
        self.correctAnswer = correctAnswer
        self.answers = incorrectAnswers.append(correctAnswer)
        random.shuffle(self.answers)

class FRQ():

    def __init__(self, prompt,spacing=2):
        self.prompt = prompt
        self.spacing = spacing

class Exam():

    def __init__(self, course=None, subject=None):
        self.course = course
        self.subject = subject
        self.mcqs = []
        self.frqs = []
        self.answerKey = np.array([])
    

    def addMCQ(self, mcq):
        self.mcqs.append(mcq)

    def addFRQ(self, frq):
        self.frqs.append(frq)

    def generateExam(self):

        # Basic document
        doc = Document('basic')
        doc.documentclass = Command(
            'documentclass',
            options=['12pt'],
            arguments=['exam'],
        )

        doc.packages.append(Package('amsmath'))
        doc.preamble.append(Command('pagestyle', 'headandfoot'))
        doc.preamble.append(Command('firstpageheader', NoEscape(r"""%s : %s \\ \today}{}{Name: \underline{\hspace{2.5in}}""" % (self.course, self.subject))))

        doc.append(Command('center', Command('fbox', Command('fbox', 'NO CALCULATORS OR EXTERNAL RESOURCES'))))
        doc.append(Command('begin', 'questions'))

        for mcq in self.mcqs:
            doc.append(NoEscape(r'\question ' + mcq.prompt))
            doc.append(Command('begin', 'checkboxes'))
            for ans in mcq.answers:
                doc.append(Command('choice', ans))

        for frq in self.frqs:
            doc.append(NoEscape(r'\question ' + NoEscape(frq.prompt)))
            doc.append(Command('vspace', frq.spacing+'in'))

        doc.append(Command('end', 'questions'))

        big_code = pyqrcode.create(np.array_str(self.answerKey) , mode='binary')
        big_code.png('code.png')

        with doc.create(Figure(position='b!')) as code:
            code.add_image('code.png', width='50px')

        doc.generate_pdf(clean_tex=False,compiler='pdfLaTeX')
        doc.generate_tex()

if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    gallery = Controller()
    gallery.show()
    app.exec_()