import os
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow

# 경로 처리 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

class SampleBaseWindow(QMainWindow):
    def __init__(self,title):
        super().__init__()

        # 공통 윈도우 설정
        self.setWindowTitle(title)
        self.setGeometry(100, 100, 400, 300)
        self.setFixedSize(400, 300)
        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

        icon_path = os.path.join(os.path.dirname(__file__), "..", "assets", "icon.png")
        self.setWindowIcon(QIcon(icon_path))