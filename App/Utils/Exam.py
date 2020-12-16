import numpy as np
from pylatex import Document, Command, Figure
from pylatex.utils import NoEscape
from pylatex.package import Package

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