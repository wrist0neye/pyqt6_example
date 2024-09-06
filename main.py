# 이렇게 하나씩 호출해도 좋지만..
# from PyQt6.QtWidgets import QMainWindow, QWidget, QDialog, QLabel, ...
# 그냥 아래 코드로 퉁쳐도 된다.
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QDoubleValidator, QFont


class firstapp(QWidget) :
    def __init__(self):
        super().__init__() # 파이썬 상속 class 초기화
        self.init_layout() # 레이아웃 초기화

    def init_layout(self):
        layout = QVBoxLayout(self) #QVBoxLayout(parent = self)

        # Scorll Area
        QScroll = QScrollArea()
        QScroll.setWidgetResizable(True)
        widget = QWidget()
        QScroll.setWidget(widget)
        main_layout = QVBoxLayout(widget)
        layout.addWidget(QScroll)

        #QLabel
        label = QLabel("This is QLabel")
        label.setFont(QFont("Inter", 14, QFont.Weight.Bold, False))
        main_layout.addWidget(label)

        #QLineEdit
        ## 일반적인 경우
        string_input = QLineEdit()
        string_input.setPlaceholderText("아무 문자열 넣어도 입력이 가능합니다.")
        main_layout.addWidget(string_input)

        ## 실수형 LineEdit()
        real_num_input = QLineEdit()
        real_num_input.setValidator(QDoubleValidator(self))
        real_num_input.setPlaceholderText("실수 값만 입력이 됩니다.")
        real_num_input.textChanged.connect(lambda x : string_input.setText(str(real_num_input.text())))
        main_layout.addWidget(real_num_input)

        ## 비밀번호 받기
        password_input = QLineEdit()
        password_input.setPlaceholderText("password here")
        password_input.setEchoMode(QLineEdit.EchoMode.Password) # PyQt6 문법
        password_input.textEdited.connect(lambda x : print(password_input.text()))
        main_layout.addWidget(password_input)

        #QPushbutton
        btn = QPushButton("click!")
        btn.clicked.connect(lambda x : print("Button is clicked"))
        main_layout.addWidget(btn)

        #QSpinbox
        intspinbox = QSpinBox() # QSpinBox는 기본적으로 0 ~ 100 사이 범위를 가진다. step = 1
        intspinbox.setMaximum(1000) # 최대 범위를 1000으로
        intspinbox.setMinimum(50) # 최소 범위를 50
        intspinbox.setSingleStep(5) # 버튼 클릭당 5씩 값 변화
        main_layout.addWidget(intspinbox)

        #QDoubleSpinbox
        doublebox = QDoubleSpinBox()
        doublebox.setMaximum(31.4135)
        doublebox.setMinimum(-10)
        doublebox.setSingleStep(0.2)
        main_layout.addWidget(doublebox)


# 만약 이 파일이 메인 실행파일이라면 아래 코드를 실행
if __name__ == "__main__" :
    app = QApplication([]) # 보통은 sys.argv 값을 넣는다.
    win = firstapp()
    win.show()
    app.exec()
