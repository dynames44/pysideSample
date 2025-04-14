import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from common.SampleBaseWindow import SampleBaseWindow as BaseWindow
from PySide6.QtWidgets import QApplication, QPushButton, QMessageBox

class MainWindow(BaseWindow):
    def __init__(self):

        super().__init__("QPushButton 예제")

        # QPushButton 생성
        button = QPushButton("클릭!!")

        # 버튼 크기 지정
        button.setFixedSize(120, 25)

        # 버튼 스타일 적용
        button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 5px;
                font-size: 10px;
                border-radius: 5px;
            }
            
            QPushButton:hover {
                background-color: #2980b9;
            }
            
            QPushButton:pressed {
                background-color: #1c5980;
            }
            
        """)

        # 버튼 클릭 시 실행할 함수 연결
        button.clicked.connect(self.button_clicked)

        # 메인 윈도우 중앙에 버튼 배치
        self.setCentralWidget(button)

    # 버튼 클릭 시 실행될 함수
    def button_clicked(self):
        QMessageBox.information(self,"알림","버튼 클릭!!")

# 앱 실행
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
