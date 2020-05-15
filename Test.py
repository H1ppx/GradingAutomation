from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape
from pylatex.package import Package

def createOpenEndedQuestion(doc, question, spacing='2in'):
    doc.append(NoEscape(r'\question ' + question))
    doc.append(Command('vspace', spacing))


def createMultipleChoiceQuestion(doc, question, *answers):
    doc.append(NoEscape(r'\question ' + question))
    doc.append(Command('begin', 'checkboxes'))
    for x in answers:
        doc.append(Command('choice', x))
    doc.append(Command('end', 'checkboxes'))
    doc.append(Command('vspace', '1in'))

if __name__ == '__main__':
    # Basic document
    doc = Document('basic')
    doc.documentclass = Command(
        'documentclass',
        options=['12pt'],
        arguments=['exam'],
    )

    # Adding AMSMATH to packages
    doc.packages.append(Package('amsmath'))

    # Create Header
    doc.preamble.append(Command('pagestyle', 'headandfoot'))
    doc.preamble.append(Command('firstpageheader', NoEscape(r'Sample Exam \\ Sample Course \\ \today}{}{Name: '
                                                            r'\underline{\hspace{2.5in}}')))
    doc.preamble.append(Command('firstpagefooter', NoEscape(r'}{}{')))
    doc.append(Command('center', Command('fbox', Command('fbox', 'NO CALCULATORS OR EXTERNAL RESOURCES'))))

    # Begin Questions
    doc.append(Command('begin', 'questions'))

    # Create Sample FRQ
    createOpenEndedQuestion(doc, NoEscape(r'This is an example of an open ended math problem: $$\text{Compute }\int_{'
                                          r'0}^{\infty}\frac{\sin(x)\cos(x)}{x}dx$$'))

    # Create Sample MCQ
    createMultipleChoiceQuestion(doc,
                                 NoEscape(r'This is an example of a multiple choice question: Which of these famous '
                                          r'physicists published a paper on Brownian Motion?'), 'Stephen Hawking',
                                 'Albert Einstein', 'Emmy Noether', 'None of the Above')

    # End Questions
    doc.append(Command('end', 'questions'))

    doc.generate_pdf(clean_tex=False)
    doc.generate_tex()
