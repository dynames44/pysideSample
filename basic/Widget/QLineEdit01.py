import os
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 윈도우 타이틀 및 크기 설정
        self.setWindowTitle("QLineEdit 예제")
        self.setGeometry(100, 100, 400, 300)
        self.setFixedSize(400, 300)
        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        
        icon_path = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "icon.png")
        self.setWindowIcon(QIcon(icon_path))

        # 다른 위젯/레이아웃을 담아둘 컨테이너 (QWidget)
        container = QWidget()
        self.setCentralWidget(container)

        # 레이아웃 : 컨테이너 안에서 위젯들을 수직으로 배치하는 역할
        layout = QVBoxLayout()

        # 입력 박스 (QLineEdit): 텍스트 입력을 받을 위젯
        self.input_field = QLineEdit()

        # 출력용 라벨 (QLabel): 입력된 텍스트를 출력할 라벨
        self.output_label = QLabel("여기에 출력됩니다.")

        # 버튼 (QPushButton)
        button = QPushButton("입력값 출력")

        # 버튼 클릭 시 실행될 함수 연결 (Signal -> Slot 연결)
        button.clicked.connect(self.show_input_text)

        # 레이아웃에 위젯 추가 (위에서 아래 순서로)
        layout.addWidget(self.input_field)
        layout.addWidget(button)
        layout.addWidget(self.output_label)

        # 컨테이너에 레이아웃 설정
        container.setLayout(layout)

    # 버튼 클릭 시 실행될 함수 (슬롯)
    def show_input_text(self):
        # 입력된 텍스트를 읽어서 라벨에 출력
        text = self.input_field.text()
        self.output_label.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
