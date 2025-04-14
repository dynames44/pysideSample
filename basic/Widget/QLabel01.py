import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from common.SampleBaseWindow import SampleBaseWindow as BaseWindow
from PySide6.QtWidgets import QApplication ,QLabel

class MainWindow(BaseWindow): # 메인 윈도우를 정의

    def __init__(self):
        super().__init__("첫 번째 PySide6 앱")        
        
        label = QLabel("Hello PySide6!") #레이블 텍스트 지정  
        self.setCentralWidget(label) # 메인 윈도우의 중앙에 위젯 배치 : 하나의 위젯만 가능

if __name__ == "__main__":
    
    # sys.argv: 프로그램 실행 시 전달되는 인자들 (없어도 되지만 관습적으로 넣음)
    app = QApplication(sys.argv) # QApplication: 프로그램 전체 객체
    window = MainWindow() # 메인 윈도우(MainWindow 클래스) 인스턴스 생성
    window.show() # 창을 화면에 띄움 (안 하면 안 보임!)
    sys.exit(app.exec()) # 이벤트 루프 실행: 프로그램이 종료될 때까지 GUI 가 사용자 이벤트(클릭, 키보드 입력 등)를 기다림
