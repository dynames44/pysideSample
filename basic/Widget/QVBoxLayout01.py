import os
import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton,
    QLabel, QWidget, QVBoxLayout, QHBoxLayout, QFrame
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 메인 윈도우 설정
        self.setWindowTitle("PySide6 Layout")
        self.setGeometry(100, 100, 600, 400)
        
        container = QWidget() # 위젯 컨테이너
        main_layout = QVBoxLayout() # 컨테이너 내부의 전체 레이아웃 

        # 1번 레이아웃: QFrame 사용 (레이아웃 구분용)
        layout1_container = QFrame()
        layout1_container.setFrameShape(QFrame.Box)
        layout1_container.setLineWidth(1)  # 얇은 보더

        layout1 = QVBoxLayout(layout1_container)
        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setSpacing(0)

        label = QLabel("세로 레이아웃")
        button1 = QPushButton("세로 버튼")

        layout1.addWidget(label)
        layout1.addWidget(button1)

        # 2번 레이아웃: QFrame 사용
        layout2_container = QFrame()
        layout2_container.setFrameShape(QFrame.Box)
        layout2_container.setLineWidth(1)  # 얇은 보더

        layout2 = QHBoxLayout(layout2_container)
        layout2.setContentsMargins(0, 0, 0, 0)
        layout2.setSpacing(0)

        button2 = QPushButton("가로 버튼 1")
        button3 = QPushButton("가로 버튼 2")

        layout2.addWidget(button2)
        layout2.addWidget(button3)

        # 메인 레이아웃 구성
        main_layout.addWidget(layout1_container)
        main_layout.addWidget(layout2_container)

        main_layout.setStretch(0, 1)
        main_layout.setStretch(1, 1)

        container.setLayout(main_layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
