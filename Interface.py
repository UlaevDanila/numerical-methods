import PyQt5.QtWidgets
from PyQt5.QtWidgets import *
import sys
from FunctionalRealisation import main_calc

class Main(QWidget):
    
    def __init__(self):
        super().__init__()
        self.calc()

    def calc(self):
        self.qle1 = QLineEdit(self)
        self.qle1.setPlaceholderText('Введите a')
        self.qle2 = QLineEdit(self)
        self.qle2.setPlaceholderText('Введите b')
        self.qle3 = QLineEdit(self)
        self.qle3.setPlaceholderText('Введите epsilon')
        self.qle4 = QLineEdit(self)
        self.qle4.setPlaceholderText('Введите начальное значение y0')
        self.qle5 = QPlainTextEdit(self)
        self.qle5.setPlaceholderText('Результат')
        btn = QPushButton("Решить", self)
        btn.clicked.connect(self.btnclick)
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['x', 'y.приб', 'y.точн', 'погрешность'])
        

        lo = QVBoxLayout(self)

        lo.addWidget(self.qle1)
        lo.addWidget(self.qle2)
        lo.addWidget(self.qle3)
        lo.addWidget(self.qle4)
        lo.addWidget(self.qle5)
        lo.addWidget(btn)
        lo.addWidget(self.table)

    def btnclick(self):
        a = self.qle1.text()
        b = self.qle2.text()
        epsilon = self.qle3.text()
        y0 = self.qle4.text()
        try:
            if (a is not None) or (b is not None) or (epsilon is not None) or (y0 is not None):
                x, y, y1 = main_calc(float(a), float(b), float(epsilon), float(y0))
                delta = abs(y-y1)
                self.table.setRowCount(len(x))
                n = 0
                for i in x:
                    self.table.setItem(n, 0, QTableWidgetItem(str(round(i,8))))

                    n += 1
                n = 0
                for i in y:
                    self.table.setItem(n, 1, QTableWidgetItem(str(round(i,8))))
                    n += 1
                n = 0
                for i in y1:
                    self.table.setItem(n, 2, QTableWidgetItem(str(round(i,8))))
                    n += 1
                n = 0
                for i in delta:
                    self.table.setItem(n, 3, QTableWidgetItem(str(round(i,8))))
                    n += 1

                self.qle5.setPlainText(str(x))
            else:
                self.qle5.clear()
                self.qle5.setPlainText('Заполни все поля')
        except:
            self.qle1.clear()
            self.qle2.clear()
            self.qle3.clear()
            self.qle4.clear()
            self.qle5.clear()
            self.qle5.setPlainText('Введите числа')

        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MAIN = Main()
    MAIN.show()
    app.exec()
