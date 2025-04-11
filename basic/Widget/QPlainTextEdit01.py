import os
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout


icon_path = os.path.join(os.path.dirname(__file__), "..", "assets", "icon.png")

class MainWindow(QMainWindow):
    
    '''
        QPlainTextEdit - 리치 텍스트 (HTML, 서식) 지원 안함!!!!!!
    '''
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QPlainTextEdit 예제")
        self.setGeometry(100, 100, 400, 300)
        self.setFixedSize(400, 300)
        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        
        icon_path = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "icon.png")
        self.setWindowIcon(QIcon(icon_path))

        container = QWidget()
        layout = QVBoxLayout()
        self.setCentralWidget(container)
        
        editlayout1 = QHBoxLayout() # TextEdit #1 Layout
        editlayout2 = QHBoxLayout() # TextEdit #2 Layout
        buttonLayout = QHBoxLayout() # Button Layout

        editLabel1 = QLabel("TextEdit #1")
        editLabel1.setFixedHeight(15)        
        editlayout1.addWidget(editLabel1) #TextEdit #1 Layout에 추가

        # QPlainTextEdit 생성 (순수 텍스트 편집기)
        self.plain_text_edit = QPlainTextEdit()

        # 플레이스홀더 텍스트
        self.plain_text_edit.setPlaceholderText("여기에 텍스트를 입력하세요...")
        
        #높이지정
        self.plain_text_edit.setFixedHeight(80)
        
        #스크롤바 
        self.plain_text_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)  # 수평 스크롤 항상
        self.plain_text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)  # 수직 스크롤 항상        

        # 초기 텍스트
        #self.plain_text_edit.setPlainText("기본 텍스트입니다.")
        editlayout1.addWidget(self.plain_text_edit)  #TextEdit #1 Layout에 추가     

        editLabel2 = QLabel("TextEdit #2")
        editLabel2.setFixedHeight(15)        
        
        textEdit2 = QPlainTextEdit()
        textEdit2.setPlainText("기본 텍스트입니다.")
        
        #높이지정
        textEdit2.setFixedHeight(80)

        # 읽기 전용으로 만들기 (뷰어 용도)
        textEdit2.setReadOnly(True)
        
        editlayout2.addWidget(editLabel2) #TextEdit #2 Layout에 추가
        editlayout2.addWidget(textEdit2) #TextEdit #2 Layout에 추가        

        # 텍스트 변경 시 함수 연결
        self.plain_text_edit.textChanged.connect(self.text_edit_changed)

        # 출력용 라벨
        self.label = QLabel("입력된 텍스트가 여기에 표시됩니다.")

        # 버튼: 텍스트 가져오기
        button = QPushButton("텍스트 가져오기")
        button.clicked.connect(self.show_text_edit_content)
        buttonLayout.addWidget(button)
        
        button2 = QPushButton("초기화")
        button2.clicked.connect(self.reset_text_edit)
        buttonLayout.addWidget(button2)
        
        #본판 레이아웃에 TextEdit #1 Layout add
        layout.addLayout(editlayout1)        
        layout.addLayout(editlayout2)      
        layout.addLayout(buttonLayout)      
        layout.addWidget(self.label)

        container.setLayout(layout)

    # 텍스트 변경 시 자동 실행 함수
    def text_edit_changed(self):
        text = self.plain_text_edit.toPlainText()
        self.label.setText(f"[변경됨] {text}")

    # 버튼 클릭 시 텍스트 가져오기
    def show_text_edit_content(self):
        text = self.plain_text_edit.toPlainText()
        self.label.setText(f"입력된 텍스트: {text}")
        
    # 초기화
    def reset_text_edit(self):
        self.plain_text_edit.setPlainText("")
        self.plain_text_edit.setPlaceholderText("여기에 텍스트를 입력하세요...")
        self.label.setText("[입력 초기화....]")        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
