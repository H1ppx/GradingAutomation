from __future__ import print_function, unicode_literals
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QMainWindow, QStackedWidget, QMessageBox)

from PyQt5 import QtCore

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
import os

from Widgets.CreateWidget import CreateWidget
from Widgets.GradeWidget import GradeWidget


class Controller(QMainWindow):

    def __init__(self, parent=None):
        super(Controller, self).__init__(parent)
    
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
    
        self.createWidget = CreateWidget(self)
        self.gradeWidget = GradeWidget(self)

        self.createWidget.switchModeButton.clicked.connect(self.switch)
        self.gradeWidget.switchModeButton.clicked.connect(self.switch)
        
        self.central_widget.addWidget(self.createWidget)
        self.central_widget.addWidget(self.gradeWidget)

        self.central_widget.setCurrentWidget(self.createWidget)
        self.gradeMode = False

        self.setWindowTitle("Grading Automation")

    def switch(self):
        if(self.gradeMode):
            self.central_widget.setCurrentWidget(self.createWidget)
            self.gradeMode = False
        else:
            self.central_widget.setCurrentWidget(self.gradeWidget)
            self.gradeMode = True

if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    gallery = Controller()
    gallery.show()
    app.exec_()