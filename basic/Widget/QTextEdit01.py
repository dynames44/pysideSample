import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from common.SampleBaseWindow import SampleBaseWindow as BaseWindow
from PySide6.QtWidgets import QApplication, QTextEdit, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout







class MainWindow(BaseWindow):
    def __init__(self):
        super().__init__("test")


        container = QWidget()
        layout = QVBoxLayout()
        self.setCentralWidget(container)

        # QTextEdit 생성 (멀티라인 입력 박스)
        label1 = QLabel("TextEdit #1 입력 가능")
        label1.setFixedHeight(15)
        
        label2 = QLabel("TextEdit #2 입력 불가")
        label2.setFixedHeight(15)
        
        #텍스트 에디터 추가 
        self.text_edit = QTextEdit()

        # 플레이스홀더 텍스트 (힌트)
        self.text_edit.setPlaceholderText("여기에 텍스트를 입력하세요...")
        
        # 높이 지정 (예: 100픽셀)
        self.text_edit.setFixedHeight(50)  
        #최소/최대 높이
        #self.text_edit.setMinimumHeight(50)
        #self.text_edit.setMaximumHeight(150)                
        
        #텍스트 워프   
        #self.text_edit.setLineWrapMode() # QTextEdit.NoWrap : 줄바꿈 없음 / QTextEdit.WidgetWidth : 위젯 너비 기준 줄바꿈 (기본)
        
        #스크롤바 
        #self.text_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)  # 수평 스크롤 항상
        #self.text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)  # 수직 스크롤 항상

        # 텍스트 변경 시 실행할 함수 연결
        self.text_edit.textChanged.connect(self.text_edit_changed)

        text_edit2 = QTextEdit()
        text_edit2.setMinimumHeight(50)

        # 초기 텍스트 설정
        text_edit2.setText("기본 텍스트입니다.")

        # 읽기 전용으로 설정 (뷰어로 사용 시)
        text_edit2.setReadOnly(True)

        # 출력용 라벨
        self.label = QLabel("입력된 텍스트가 여기에 표시됩니다.")
        self.label.setFixedHeight(50)

        # 버튼: 텍스트 가져오기
        button = QPushButton("텍스트 가져오기")
        button.clicked.connect(self.show_text_edit_content)

        btnReset = QPushButton("초기화")
        btnReset.clicked.connect(self.text_edit_Reset)

        layout.addWidget(label1)
        layout.addWidget(self.text_edit)        
        layout.addWidget(label2)
        layout.addWidget(text_edit2)
        
        # 버튼을 가로로 표현위에 버튼만 들어가는 레이아웃 추가 
        button_layout = QHBoxLayout()
        button_layout.addWidget(button)
        button_layout.addWidget(btnReset)

        #layout.addWidget(button)
        #layout.addWidget(btnReset)        
        #본판 레이아웃에 추가한 버튼 레이아웃 add
        layout.addLayout(button_layout)
        
        layout.addWidget(self.label)
        container.setLayout(layout)

    # 텍스트 변경 시 자동 실행 함수
    def text_edit_changed(self):
        text = self.text_edit.toPlainText()  # 순수 텍스트 가져오기
        self.label.setText(f"[변경됨] {text}")

    # 버튼 클릭 시 텍스트 가져오기
    def show_text_edit_content(self):
        text = self.text_edit.toPlainText()
        self.label.setText(f"입력된 텍스트: {text}")

    # 초기화
    def text_edit_Reset(self):
        self.text_edit.setText("")
        self.text_edit.setPlaceholderText("여기에 텍스트를 입력하세요...")
        self.label.setText("[입력 초기화....]")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
