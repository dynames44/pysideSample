import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QSpinBox, QLabel, QPushButton, QWidget, QVBoxLayout
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSpinBox 예제")
        self.setGeometry(100, 100, 400, 200)
        self.setFixedSize(400, 200)  # 창 크기 고정
        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)  # 최대화 비활성화

        container = QWidget()
        self.setCentralWidget(container)
        layout = QVBoxLayout()

        # QSpinBox 생성
        self.spinbox = QSpinBox()

        # 최소값 / 최대값 설정
        self.spinbox.setMinimum(0)
        self.spinbox.setMaximum(100)

        # 초기값 설정
        self.spinbox.setValue(10)

        # 증가/감소 간격
        self.spinbox.setSingleStep(5)  # 기본은 1씩 증감
        
        # 접두사 / 접미사 추가
        #self.spinbox.setPrefix("수량: ")
        self.spinbox.setSuffix(" 개")
        
        self.spinbox2 = QSpinBox()
        self.spinbox2.setValue(3)
        self.spinbox2.setSuffix(" 개")
        self.spinbox2.setEnabled(False) # 객체 Disable

        # 값 변경 시 호출될 함수 연결
        self.spinbox.valueChanged.connect(self.spinbox_value_changed)

        # 출력용 라벨
        self.label = QLabel("선택된 숫자가 여기에 표시됩니다.")

        # 현재 값 확인용 버튼
        button = QPushButton("현재 값 확인")
        button.clicked.connect(self.show_spinbox_value)

        layout.addWidget(self.spinbox)
        layout.addWidget(self.spinbox2)
        layout.addWidget(button)
        layout.addWidget(self.label)
        container.setLayout(layout)

    # 값 변경 시 자동 실행 함수
    def spinbox_value_changed(self, value):
        self.label.setText(f"[변경됨] {value}")

    # 버튼 클릭 시 현재 값 출력
    def show_spinbox_value(self):
        value = self.spinbox.value()
        self.label.setText(f"현재 선택된 값: {value}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
