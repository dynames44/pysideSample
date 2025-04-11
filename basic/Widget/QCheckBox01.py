import os
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QCheckBox, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QCheckBox 예제")
        self.setGeometry(100, 100, 400, 300)
        self.setFixedSize(400, 300)
        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        
        icon_path = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "icon.png")
        self.setWindowIcon(QIcon(icon_path))

        # 메인 컨테이너
        container = QWidget()
        self.setCentralWidget(container)

        self.checkbox = QCheckBox("체크!!!") # 체크박스 생성
        self.checkbox.setChecked(False)  #setChecked(bool): 체크박스를 체크/해제 상태로 설정 
        #self.checkbox.toggle()  #toggle(): 현재 상태를 반대로 토글 (체크 -> 해제, 해제 -> 체크) 
        self.checkbox.setEnabled(True)  #etEnabled(bool): 체크박스를 활성화/비활성화
        #self.checkbox.setDisabled(True) #setDisabled(bool): 비활성화 (setEnabled(False) 와 같음)
        self.checkbox.setTristate(False)  #setTristate(bool): 세 가지 상태(체크 / 해제 / 부분 체크) 활성화, (기본은 False = 2상태, True 로 하면 체크박스가 "부분 체크" 도 가능)
        # self.checkbox.setText("새 텍스트")   체크박스 라벨 텍스트 변경        
        
        checkbox2 = QCheckBox()
        checkbox2.setText("체크박스 비화성화")
        checkbox2.setEnabled(False)
        
        button = QPushButton("체크 여부 확인") # 버튼 생성
        button.clicked.connect(self.check_checkbox_state) # 버튼 클릭 시 함수 연결
        self.output_label = QLabel("체크 여부가 여기에 표시됩니다.") # 출력용 라벨

        # 레이아웃에 위젯 추가
        layout = QVBoxLayout() # 레이아웃
        layout.addWidget(self.checkbox)
        layout.addWidget(checkbox2)
        layout.addWidget(button)
        layout.addWidget(self.output_label)
        container.setLayout(layout)

    # 버튼 클릭 시 체크박스 상태를 확인하는 함수
    def check_checkbox_state(self):
        if self.checkbox.isChecked():
            self.output_label.setText("✅ 체크되었습니다!")
        else:
            self.output_label.setText("❌ 체크되지 않았습니다.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
