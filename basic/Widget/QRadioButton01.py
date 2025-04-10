import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QRadioButton, QLabel, QPushButton, QWidget, QVBoxLayout, QButtonGroup

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.defaultRadio = "A022"
        self.setWindowTitle("QRadioButton 예제")
        self.setGeometry(100, 100, 400, 300)

        # 메인 컨테이너
        container = QWidget()
        self.setCentralWidget(container)
        layout = QVBoxLayout() # 레이아웃 생성

        #라디오 버튼 생성
        self.radio1 = QRadioButton("옵션 1")
        self.radio1.setChecked(False) #기본 선택 상태 설정 : True / False
        self.radio2 = QRadioButton("옵션 2")
        self.radio3 = QRadioButton("옵션 3")
        self.radio4 = QRadioButton()
        self.radio4.setEnabled(False) # 활성화/비활성화 : True / False
        self.radio4.setText("다른 옵션") # 텍스트 변경
        # isChecked() # 선택 여부 반환 (True / False)
        # text = self.radio1.text() #텍스트 가져오기
        
        #라디오 버튼에 프로퍼티 추가 
        self.radio1.setProperty("value", "A001")
        self.radio2.setProperty("value", "A002")
        self.radio3.setProperty("value", "A003")
        self.radio4.setProperty("value", "A004")

        # QButtonGroup으로 묶기 (라디오버튼 객체)
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.radio1)
        self.button_group.addButton(self.radio2)
        self.button_group.addButton(self.radio3)
        self.button_group.addButton(self.radio4)        

        self.label = QLabel("선택된 옵션이 여기에 표시됩니다.")

        # 상태 출력용 버튼
        button = QPushButton("선택된 옵션 확인")
        button.clicked.connect(self.selectRadio)
        
        # 버튼그룹을 클릭하면 이벤트 발생 
        self.button_group.buttonClicked.connect(self.selectRadioGroup)

        # 레이아웃에 추가
        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)
        layout.addWidget(self.radio3)
        layout.addWidget(self.radio4)        
        layout.addWidget(button)
        layout.addWidget(self.label)
        container.setLayout(layout)
        self.radioInit()

    # 그룹 클릭 시 바로 반응하는 슬롯
    def selectRadioGroup(self, button):
        value = button.property("value")
        self.label.setText(f"선택: {button.text()}, value: {value}")

    # 버튼 클릭 시 현재 선택된 옵션을 확인하는 슬롯
    def selectRadio(self):
        checkedRadio = self.button_group.checkedButton()  #선택된 버튼 가져오기 : 버튼그룹에서 가지고 온다
        
        if checkedRadio:
            value = checkedRadio.property("value")  # 버튼 Property Value
            self.label.setText(f"선택: {checkedRadio.text()}, value: {value}")
        else:
            self.label.setText("선택된 옵션 없음")

    #self.defaultRadio따라 최초 선택값 지정             
    def radioInit(self) : 
        for button in self.button_group.buttons():
            if button.property("value") == self.defaultRadio:
                value = button.property("value")
                button.setChecked(True)
                print(button.text())
                self.label.setText(f"선택: {button.text()}, value: {value}")
                break        
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
