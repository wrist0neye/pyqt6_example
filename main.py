# 이렇게 하나씩 호출해도 좋지만..
# from PyQt6.QtWidgets import QMainWindow, QWidget, QDialog, QLabel, ...
# 그냥 아래 코드로 퉁쳐도 된다.
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QDoubleValidator, QFont


class CardDiv(QWidget) :
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Card Widget")
        self.init_layout()

    def init_layout(self):
        self.bglayout = QVBoxLayout(self)

        # Title쪽 구역 구현
        self.titlebar = QWidget()
        self.bglayout.addWidget(self.titlebar)

        self.titlelayout = QHBoxLayout(self.titlebar)

        self.title = QLabel("Class 1")
        self.title_hspacer = QWidget()
        self.title_hspacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)

        self.button = QPushButton('+')

        for elem in ["title", "title_hspacer", "button"] :
            self.titlelayout.addWidget(getattr(self, elem))


        # property 구현
        self.propertycontainer = QWidget()
        self.bglayout.addWidget(self.propertycontainer)

        self.propertylayout = QGridLayout(self.propertycontainer)

        for i in range(1,5) :
            setattr(self, f'prop{i}_value', QLabel(f'property{i}'))
            label = getattr(self, f'prop{i}_value')
            idx = i-1
            self.propertylayout.addWidget(label, idx//2, (idx%2)*2)

        #self.prop1_label = QLabel('property1')
        self.prop1_value = QLineEdit()
        self.prop1_value.setPlaceholderText("Type anything...")
        # self.propertylayout.addWidget(self.prop1_label, 0,0)
        self.propertylayout.addWidget(self.prop1_value, 0,1)

        #self.prop2_label = QLabel('property2')
        self.prop2_value = QSpinBox()
        # self.propertylayout.addwidget(self.prop2_label,0,2)
        self.propertylayout.addWidget(self.prop2_value,0,3)

        #self.prop3_label
        self.prop3_value = QDoubleSpinBox()
        self.propertylayout.addWidget(self.prop3_value,1,1)

        #self.prop4_label
        self.prop4_value = QComboBox()
        self.propertylayout.addWidget(self.prop4_value,1,3)


# 만약 이 파일이 메인 실행파일이라면 아래 코드를 실행
if __name__ == "__main__" :
    app = QApplication([]) # 보통은 sys.argv 값을 넣는다.
    win = CardDiv()
    win.show()
    app.exec()
