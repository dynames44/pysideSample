import os
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QLabel, QPushButton, QWidget, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        
        super().__init__()

        # 창 타이틀, 초기 위치 및 크기
        self.setWindowTitle("QListWidget 예제")
        self.setGeometry(100, 100, 400, 300)
        self.setFixedSize(400, 300)
        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        
        icon_path = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "icon.png")
        self.setWindowIcon(QIcon(icon_path))

        container = QWidget()
        self.setCentralWidget(container)
        layout = QVBoxLayout()

        # QListWidget 생성
        self.list_widget = QListWidget()

        # 데이터 리스트
        listData = [
            dict(code="B001", codeName="리스트 옵션 1"),
            dict(code="B002", codeName="리스트 옵션 2"),
            dict(code="B003", codeName="리스트 옵션 3")
        ]

        # 동적 리스트 아이템 추가 
        for item in listData:
            list_item = QListWidgetItem(item["codeName"])
            list_item.setData(Qt.UserRole, item["code"])  # userData 설정
            self.list_widget.addItem(list_item)

        self.list_reSize(self.list_widget)  #리스트 사이즈 조정
        
        #리스트 중 특정 아이템만 Disable
        item = self.list_widget.item(2)  # 인덱스 1 = 두 번째 아이템
        item.setFlags(item.flags() & ~Qt.ItemIsEnabled)                    

        # 정적 리스트 아이템 추가 
        self.list_widget1 = QListWidget()
            
        list_item1 = QListWidgetItem("리스트 옵션 4")
        list_item1.setData(Qt.UserRole, "B004")
        self.list_widget1.addItem(list_item1)

        list_item2 = QListWidgetItem("리스트 옵션 5")
        list_item2.setData(Qt.UserRole, "B005")
        self.list_widget1.addItem(list_item2)

        list_item3 = QListWidgetItem("리스트 옵션 6")
        list_item3.setData(Qt.UserRole, "B006")
        self.list_widget1.addItem(list_item3)            
        
        list_item4 = QListWidgetItem("리스트 옵션 7")
        list_item4.setData(Qt.UserRole, "B007")
        self.list_widget1.addItem(list_item4)            
        
        self.list_widget1.setEnabled(False)  #리스트 객체 전체 Disable  
        self.list_reSize(self.list_widget1)  #리스트 사이즈 조정

        # 출력용 라벨
        self.label = QLabel("선택된 옵션이 여기에 표시됩니다.")

        # 선택된 항목 출력용 버튼
        button = QPushButton("선택된 옵션 확인")
        button.clicked.connect(self.show_selected_item)

        # 선택 변경 시 자동 표시
        self.list_widget.currentItemChanged.connect(self.list_item_changed)

        # 선택 모드: 단일 선택 (기본값)
        self.list_widget.setSelectionMode(QListWidget.SingleSelection)

        # 위젯들 레이아웃에 추가
        layout.addWidget(self.list_widget)
        layout.addWidget(self.list_widget1)
        layout.addWidget(button)
        layout.addWidget(self.label)

        container.setLayout(layout)

        # 초기 선택 (value 기준으로 선택)
        self.set_listwidget_value("B002")

    # 초기 선택 (value로 선택)
    def set_listwidget_value(self, target_value):
        for index in range(self.list_widget.count()):
            item = self.list_widget.item(index)
            if item.data(Qt.UserRole) == target_value:
                self.list_widget.setCurrentItem(item)
                break

    # 선택 변경 시 실행 함수
    def list_item_changed(self, current, previous):
        if current:
            text = current.text()
            value = current.data(Qt.UserRole)
            self.label.setText(f"[변경됨] {text} (Value: {value})")

    # 버튼 클릭 시 현재 선택된 항목 출력
    def show_selected_item(self):
        current_item = self.list_widget.currentItem()
        
        if current_item:
            text = current_item.text()
            value = current_item.data(Qt.UserRole)
            self.label.setText(f"선택된 옵션: {text} (Value: {value})")
            
        else:
            self.label.setText("선택된 항목 없음")
    
    #리스트 세로 길이 조정        
    def list_reSize(self, obj):
        row_count = obj.count(); #리스트 아이템 갯수
        row_height = obj.sizeHintForRow(0)  # 하나의 아이템 높이
        spacing = obj.spacing()  # 아이템 간 간격

        # 총 높이 계산
        total_height = row_count * row_height + (spacing * (row_count - 1)) + 2  # +2 는 패딩용
        obj.setFixedHeight(total_height)        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
