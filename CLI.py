from __future__ import print_function, unicode_literals
import regex
import pyfiglet
import numpy as np
import pyqrcode
import zbar
import pdf2image
import tkinter as tk
import cv2

from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError, print_json
from pylatex import Document, Section, Subsection, Command, Figure
from pylatex.utils import italic, NoEscape
from pylatex.package import Package
from tkinter.filedialog import askopenfilename
from PIL import Image

style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})

def createOpenEndedQuestion(doc, question, spacing='2in'):
    doc.append(NoEscape(r'\question ' + question))
    doc.append(Command('vspace', spacing))

print(pyfiglet.figlet_format('Grading Automation'))

mode = [
    {
        'type': 'list',
        'name': 'mode',
        'message': 'Create or Grade:',
        'choices': ['Create', 'Grade']
    }
]

headerQuestions = [
    {
        'type': 'input',
        'name': 'course',
        'message': 'What is the course?'
    },

    {
        'type': 'input',
        'name': 'material',
        'message': 'What is the material being tested?'
    }
]

addQuestions = [
    {
        'type': 'confirm',
        'name': 'add',
        'message': 'Do you want to add a question?',
        'default': False
    }
]

questionType = [
    {
        'type': 'list',
        'name' : 'type',
        'message': 'What type of question would you like to add?',
        'choices': ['Open Ended', 'Multiple Choice']
    }
]

openEndedQuestion = [
    {
        'type': 'input',
        'name': 'question',
        'message': 'Enter Question:'
    },

    {
        'type': 'list',
        'name': 'spacing',
        'message': 'How much space is needed?',
        'choices': ['Small', 'Medium', 'Large']
    },
]

multipleChoiceQuestion = [
    {
        'type': 'input',
        'name': 'question',
        'message': 'Enter Question:'
    },

    {
        'type': 'input',
        'name': 'answer',
        'message': 'Enter Correct Answer:'
    }
]

wrongAnswerQuestions = [
    {
        'type': 'confirm',
        'name': 'add',
        'message': 'Do you want to add an incorrect answer?',
        'default': False
    },

    {
        'type': 'input',
        'name': 'answer',
        'message': 'Enter an incorrect answer:',
        'when': lambda answer: answer['add']
    }
]

if __name__ == '__main__':
    if prompt(mode)['mode'] == 'Create':

        header = prompt(headerQuestions, style=style)

        # Basic document
        doc = Document('basic')
        doc.documentclass = Command(
            'documentclass',
            options=['12pt'],
            arguments=['exam'],
        )

        doc.packages.append(Package('amsmath'))
        doc.preamble.append(Command('pagestyle', 'headandfoot'))
        doc.preamble.append(Command('firstpageheader', NoEscape(r"""%s : %s \\ \today}{}{Name: \underline{\hspace{2.5in}}""" % (header['course'], header['material']))))

        doc.append(Command('center', Command('fbox', Command('fbox', 'NO CALCULATORS OR EXTERNAL RESOURCES'))))
        doc.append(Command('begin', 'questions'))

        answerKey = np.array([])
        while True:
            if prompt(addQuestions)['add']:
                if prompt(questionType)['type'] == 'Multiple Choice':
                    question = prompt(multipleChoiceQuestion)
                    doc.append(NoEscape(r'\question ' + question['question']))
                    doc.append(Command('begin', 'checkboxes'))
                    doc.append(Command('choice', question['answer'])) # TODO: Randomize correct answer in MCQ
                    while True:
                        waq = prompt(wrongAnswerQuestions)
                        if waq['add']:
                            doc.append(Command('choice', waq['answer']))
                        else:
                            break
                    doc.append(Command('end', 'checkboxes'))
                    doc.append(Command('vspace', '1in'))
                    answerKey = np.append (answerKey, [1]) # TODO: Edit once MCQ becomes random


                else:
                    question = prompt(openEndedQuestion)
                    if question['spacing'] == 'Small':
                        spacing = '0.5in'
                    elif question['spacing'] == 'Med':
                        spacing = '1.5in'
                    else:
                        spacing = '2.5in'

                    doc.append(NoEscape(r'\question ' + NoEscape(question['question'])))
                    doc.append(Command('vspace', spacing))
                    answerKey = np.append(answerKey, [-1])
            else:
                break

        doc.append(Command('end', 'questions'))

        big_code = pyqrcode.create(np.array_str(answerKey) , mode='binary')
        print()
        big_code.png('code.png')

        with doc.create(Figure(position='b!')) as code:
            code.add_image('code.png', width='50px')

        doc.generate_pdf(clean_tex=False)
        doc.generate_tex()
    else:
        filename = askopenfilename()
        print(filename)
        # image = Image.open(filename)
        image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        scanner = zbar.Scanner()
        results = scanner.scan(image)
        for result in results:
            print(result.type, result.data, result.quality, result.position)

        image = cv2.imread(filename)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # detect circles in the image
        circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1.2, 100)
        # ensure at least some circles were found
        if circles is not None:
            # convert the (x, y) coordinates and radius of the circles to integers
            circles = np.round(circles[0, :]).astype("int")
            # loop over the (x, y) coordinates and radius of the circles
            for (x, y, r) in circles:
                # draw the circle in the output image, then draw a rectangle
                # corresponding to the center of the circle
                cv2.circle(image, (x, y), r, (0, 255, 0), 4)
                cv2.rectangle(image, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
            # show the output image
            cv2.imshow("output", image)
            cv2.waitKey(0)