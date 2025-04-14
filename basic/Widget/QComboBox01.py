import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from common.SampleBaseWindow import SampleBaseWindow as BaseWindow
from PySide6.QtWidgets import QApplication, QComboBox, QLabel, QPushButton, QWidget, QVBoxLayout

class MainWindow(BaseWindow):
    def __init__(self):

        super().__init__("QComboBox 예제")

        # 메인 컨테이너
        container = QWidget()
        self.setCentralWidget(container)

        # 레이아웃
        layout = QVBoxLayout()

        # 콤보박스 생성
        self.combobox = QComboBox()

        # 항목 추가
        self.combobox.addItem("옵션 1", userData="A001")  # userData: value 값처럼 사용
        self.combobox.addItem("옵션 2", userData="A002")
        self.combobox.addItem("옵션 3", userData="A003")
        
        # 동적 추가 
        comboData : list = [
            dict(code="A004", codeName="옵션4"),
            dict(code="A005", codeName="옵션5"),
            dict(code="A006", codeName="옵션6")
        ]
        
        for item in comboData:
            self.combobox.addItem(item["codeName"], userData=item["code"])        

        # 비활성화 항목 처리 (model 접근해서 처리)
        self.combobox.model().item(1).setEnabled(False)

        # 여러 항목 한 번에 추가
        self.combobox2 = QComboBox()
        self.combobox2.addItems(["옵션 7", "옵션 8", "옵션 9"])
        
        #사용 X
        self.combobox2.setEnabled(False)

        # 현재 선택된 값
        self.label = QLabel("선택된 옵션이 여기에 표시됩니다.")

        # 버튼: 선택된 옵션 확인
        button = QPushButton("선택된 옵션 확인")
        button.clicked.connect(self.show_selected_option)

        # 시그널 연결: 선택이 변경될 때마다 바로 표시
        self.combobox.currentIndexChanged.connect(self.combobox_changed)

        # 레이아웃 추가
        layout.addWidget(self.combobox)
        layout.addWidget(self.combobox2)        
        layout.addWidget(button)
        layout.addWidget(self.label)
        container.setLayout(layout)

        # 초기 선택 (인덱스로 선택)
        '''
            comboBox값 선택(지정)
            1. 인덱스로 지정 
             - combobox.setCurrentIndex(인덱스 번호)
             
            2. Value로 지정 
              - index = combobox.findData("A002") # Value 맞는 인덱스 Find
                combobox.setCurrentIndex(index)
        '''     
        #self.combobox.setCurrentIndex(1)  # "옵션 2"
        self.combobox.setCurrentIndex(self.combobox.findData("A002")) 

    # 콤보박스 선택 변경 시 실행되는 슬롯
    def combobox_changed(self, index):
        text = self.combobox.itemText(index)
        value = self.combobox.itemData(index)  # userData 가져오기
        self.label.setText(f"[변경됨] {text} (Value: {value})")

    # 버튼 클릭 시 선택된 옵션을 표시하는 슬롯
    def show_selected_option(self):
        index = self.combobox.currentIndex()  # 현재 선택된 인덱스
        text = self.combobox.currentText()  # 선택된 텍스트
        value = self.combobox.itemData(index)  # userData 값
        self.label.setText(f"선택된 옵션: {text} (Value: {value})")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
