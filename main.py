import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()

        self.setWindowTitle("MyCalculator")

        self.hbox_line = QHBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox_res = QHBoxLayout()
        self.vbox = QVBoxLayout()

        self.vbox.addLayout(self.hbox_line)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox_res)

        self.line = QLineEdit(self)
        self.line.setEnabled(False)

        self.b_1 = QPushButton("1", self)
        self.b_2 = QPushButton("2", self)
        self.b_3 = QPushButton("3", self)
        self.b_add = QPushButton("+", self)
        self.b_res = QPushButton("=", self)
        self.b_4 = QPushButton("4", self)
        self.b_5 = QPushButton("5", self)
        self.b_6 = QPushButton("6", self)
        self.b_sub = QPushButton("-", self)
        self.b_mult = QPushButton("*", self)
        self.b_7 = QPushButton("7", self)
        self.b_8 = QPushButton("8", self)
        self.b_9 = QPushButton("9", self)
        self.b_0 = QPushButton("0", self)
        self.b_div = QPushButton("/", self)
        self.b_clear = QPushButton("C", self)
        self.b_dot = QPushButton(".", self)
        self.b_backspace = QPushButton("BS", self)


        self.hbox_line.addWidget(self.line)
        self.hbox1.addWidget(self.b_1)
        self.hbox1.addWidget(self.b_2)
        self.hbox1.addWidget(self.b_3)
        self.hbox1.addWidget(self.b_add)
        self.hbox1.addWidget(self.b_sub)
        self.hbox1.addWidget(self.b_res)
        self.hbox2.addWidget(self.b_4)
        self.hbox2.addWidget(self.b_5)
        self.hbox2.addWidget(self.b_6)
        self.hbox2.addWidget(self.b_mult)
        self.hbox2.addWidget(self.b_div)
        self.hbox2.addWidget(self.b_clear)
        self.hbox3.addWidget(self.b_7)
        self.hbox3.addWidget(self.b_8)
        self.hbox3.addWidget(self.b_9)
        self.hbox3.addWidget(self.b_0)
        self.hbox3.addWidget(self.b_dot)
        self.hbox3.addWidget(self.b_backspace)

        self.setLayout(self.vbox)

        self.b_1.clicked.connect(lambda: self.addText("1"))
        self.b_2.clicked.connect(lambda: self.addText("2"))
        self.b_3.clicked.connect(lambda: self.addText("3"))
        self.b_add.clicked.connect(lambda: self.operation("+"))
        self.b_res.clicked.connect(self.result)
        self.b_4.clicked.connect(lambda: self.addText("4"))
        self.b_5.clicked.connect(lambda: self.addText("5"))
        self.b_6.clicked.connect(lambda: self.addText("6"))
        self.b_sub.clicked.connect(lambda: self.operation("-"))
        self.b_mult.clicked.connect(lambda: self.operation("*"))
        self.b_7.clicked.connect(lambda: self.addText("7"))
        self.b_8.clicked.connect(lambda: self.addText("8"))
        self.b_9.clicked.connect(lambda: self.addText("9"))
        self.b_0.clicked.connect(lambda: self.addText("0"))
        self.b_div.clicked.connect(lambda: self.operation("/"))
        self.b_clear.clicked.connect(lambda: self.clearText())
        self.b_dot.clicked.connect(lambda: self.addText("."))
        self.b_backspace.clicked.connect(lambda: self.backspace())

    def addText(self, param):
        line = self.line.text()
        self.line.setText(line + param)

    def operation(self, param):
        self.check = self.line.text()
        if self.check:
            self.num1 = self.line.text()
            self.line.setText("")
            self.op = param
        else:
            pass

    def result(self):
        self.num2 = self.line.text()
        try:
            self.num1
        except AttributeError:
            return
        try:
             float(self.num1)
             float(self.num2)
        except ValueError:
            self.line.setText("Error")
            return
        if self.op == "+":
            self.line.setText(str(float(self.num1) + float(self.num2)))
        if self.op == "-":
            self.line.setText(str(float(self.num1) - float(self.num2)))
        if self.op == "*":
            self.line.setText(str(float(self.num1) * float(self.num2)))
        if self.op == "/":
            try:
                self.line.setText(str(float(self.num1) / float(self.num2)))
            except ZeroDivisionError:
                self.line.setText("Error")
        else:
            pass

    def clearText(self):
        self.line.setText("")

    def backspace(self):
        self.edit = self.line.text()
        if self.edit:
            try:
                float(self.edit)
            except ValueError:
                self.line.setText("Error")
                return
            self.edit = list(self.edit)
            self.edit.pop()
            self.edit = ''.join(self.edit)
            self.line.setText(self.edit)
        else:
            pass

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Plus:
            self.operation("+")
        if e.key() == Qt.Key_Minus:
            self.operation("-")
        if e.key() == Qt.Key_Enter:
            self.result()
        if e.key() == Qt.Key_Equal:
            self.result()
        if e.key() == Qt.Key_Slash:
            self.operation("/")
        if e.key() == Qt.Key_Asterisk:
            self.operation("*")
        if e.key() == Qt.Key_1:
            self.addText("1")
        if e.key() == Qt.Key_2:
            self.addText("2")
        if e.key() == Qt.Key_3:
            self.addText("3")
        if e.key() == Qt.Key_4:
            self.addText("4")
        if e.key() == Qt.Key_5:
            self.addText("5")
        if e.key() == Qt.Key_6:
            self.addText("6")
        if e.key() == Qt.Key_7:
            self.addText("7")
        if e.key() == Qt.Key_8:
            self.addText("8")
        if e.key() == Qt.Key_9:
            self.addText("9")
        if e.key() == Qt.Key_0:
            self.addText("0")
        if e.key() == Qt.Key_Period:
            self.addText(".")
        if e.key() == Qt.Key_Delete:
            self.clearText()
        if e.key() == Qt.Key_Backspace:
            self.backspace()

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("MyFirstApp")
        self.first_label = QLabel(self)

        self.button = QPushButton("Push me", self)

        self.first_label.setText("Hello")
        self.vbox = QVBoxLayout(self)
        self.hbox = QHBoxLayout()
        self.vbox.addWidget(self.first_label)
        self.vbox.addLayout(self.hbox)

        self.button.clicked.connect(self.changeText)

    def changeText(self):
        self.first_label.setText("Привет")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec_()) 