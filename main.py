import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QLabel, QFrame, QStackedWidget
)
from PyQt5.QtGui import QFont, QPixmap, QColor, QPalette
from PyQt5.QtCore import Qt

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

CHARACTERS = [
    {
        "id": 1,
        "poem": (
            "Кепка набок, взгляд орлиный,\n"
"Спорт и стать — мужчина видный.\n"
"Каждый день он на зарядке —\n"
"Угадай без всякой загадки!"
        ),
        "photo": resource_path("assets/person1.jpg"),
        "name": "Персонаж 1"
    },
    {
        "id": 2,
        "poem": (
            "Она урок ведёт с улыбкой,\n"
"Характер добрый, не ошибка.\n"
"Джони — пёс её родной —\n"
"Угадай, кто перед тобой!"
        ),
        "photo": resource_path("assets/person2.jpg"),
        "name": "Персонаж 2"
    },
]

STYLE = """
QWidget {
    background-color: #0f0f1a;
    color: #ffffff;
    font-family: Arial;
}
QPushButton {
    background-color: #5865f2;
    color: #ffffff;
    border: none;
    border-radius: 20px;
    padding: 10px 24px;
    font-size: 15px;
    font-weight: bold;
}
QPushButton:hover {
    background-color: #4752c4;
}
QPushButton#back_btn {
    background-color: transparent;
    color: #9090aa;
    border: 1px solid #444466;
    font-weight: normal;
}
QPushButton#back_btn:hover {
    background-color: #1e1e2e;
}
QLabel#title {
    font-size: 40px;
    font-weight: bold;
    color: #ffffff;
}
QLabel#subtitle {
    font-size: 14px;
    color: #9090aa;
}
QLabel#accent {
    font-size: 16px;
    font-weight: bold;
    color: #5865f2;
}
QLabel#poem {
    font-size: 16px;
    color: #e0e0f0;
    background-color: #1e1e2e;
    border-radius: 12px;
    padding: 24px;
}
QLabel#name_label {
    font-size: 20px;
    font-weight: bold;
    color: #5865f2;
}
"""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Угадай кто")
self.showMaximized()
self.setStyleSheet(STYLE)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.main_screen = MainScreen(self)
        self.choice_screen = ChoiceScreen(self)

        self.stack.addWidget(self.main_screen)
        self.stack.addWidget(self.choice_screen)

        self.poem_screens = []
        self.photo_screens = []
        for i in range(len(CHARACTERS)):
            ps = PoemScreen(self, i)
            ph = PhotoScreen(self, i)
            self.poem_screens.append(ps)
            self.photo_screens.append(ph)
            self.stack.addWidget(ps)
            self.stack.addWidget(ph)

        self.show_main()

    def show_main(self):
        self.stack.setCurrentWidget(self.main_screen)

    def show_choice(self):
        self.stack.setCurrentWidget(self.choice_screen)

    def show_poem(self, idx):
        self.stack.setCurrentWidget(self.poem_screens[idx])

    def show_photo(self, idx):
        self.stack.setCurrentWidget(self.photo_screens[idx])


class MainScreen(QWidget):
    def __init__(self, master):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        top_bar = QFrame()
        top_bar.setFixedHeight(4)
        top_bar.setStyleSheet("background-color: #5865f2;")
        layout.addWidget(top_bar)

        center = QWidget()
        center_layout = QVBoxLayout(center)
        center_layout.setAlignment(Qt.AlignCenter)
        center_layout.setSpacing(16)

        lbl_game = QLabel("ИГРА")
        lbl_game.setObjectName("accent")
        lbl_game.setAlignment(Qt.AlignCenter)

        lbl_title = QLabel("Угадай кто?")
        lbl_title.setObjectName("title")
        lbl_title.setAlignment(Qt.AlignCenter)

        lbl_sub = QLabel("Прочитай подсказку и угадай персонажа!")
        lbl_sub.setObjectName("subtitle")
        lbl_sub.setAlignment(Qt.AlignCenter)

        btn_start = QPushButton("Начать игру")
        btn_start.setFixedSize(220, 54)
        btn_start.clicked.connect(master.show_choice)

        center_layout.addWidget(lbl_game)
        center_layout.addWidget(lbl_title)
        center_layout.addSpacing(8)
        center_layout.addWidget(lbl_sub)
        center_layout.addSpacing(32)
        center_layout.addWidget(btn_start, alignment=Qt.AlignCenter)

        layout.addWidget(center, stretch=1)

        lbl_ver = QLabel("v1.0")
        lbl_ver.setAlignment(Qt.AlignCenter)
        lbl_ver.setStyleSheet("color: #444466; font-size: 11px;")
        layout.addWidget(lbl_ver)
        layout.addSpacing(16)


class ChoiceScreen(QWidget):
    def __init__(self, master):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        top_bar = QFrame()
        top_bar.setFixedHeight(4)
        top_bar.setStyleSheet("background-color: #5865f2;")
        layout.addWidget(top_bar)

        center = QWidget()
        center_layout = QVBoxLayout(center)
        center_layout.setAlignment(Qt.AlignCenter)
        center_layout.setSpacing(16)

        lbl_title = QLabel("Выбери персонажа")
        lbl_title.setStyleSheet("font-size: 28px; font-weight: bold;")
        lbl_title.setAlignment(Qt.AlignCenter)

        lbl_sub = QLabel("Нажми на кнопку — получи подсказку")
        lbl_sub.setObjectName("subtitle")
        lbl_sub.setAlignment(Qt.AlignCenter)

        btn_row = QWidget()
        btn_row_layout = QHBoxLayout(btn_row)
        btn_row_layout.setAlignment(Qt.AlignCenter)
        btn_row_layout.setSpacing(40)

        for char in CHARACTERS:
            idx = char["id"] - 1
            btn = QPushButton(str(char["id"]))
            btn.setFixedSize(110, 110)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #1e1e2e;
                    color: #ffffff;
                    border: 2px solid #5865f2;
                    border-radius: 55px;
                    font-size: 36px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #5865f2;
                }
            """)
            btn.clicked.connect(lambda checked, i=idx: master.show_poem(i))
            btn_row_layout.addWidget(btn)

        center_layout.addWidget(lbl_title)
        center_layout.addWidget(lbl_sub)
        center_layout.addSpacing(24)
        center_layout.addWidget(btn_row)

        layout.addWidget(center, stretch=1)

        btn_back = QPushButton("Назад")
        btn_back.setObjectName("back_btn")
        btn_back.setFixedSize(140, 40)
        btn_back.clicked.connect(master.show_main)
        layout.addWidget(btn_back, alignment=Qt.AlignCenter)
        layout.addSpacing(24)


class PoemScreen(QWidget):
    def __init__(self, master, char_index):
        super().__init__()
        char = CHARACTERS[char_index]
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        top_bar = QFrame()
        top_bar.setFixedHeight(4)
        top_bar.setStyleSheet("background-color: #5865f2;")
        layout.addWidget(top_bar)

        center = QWidget()
        center_layout = QVBoxLayout(center)
        center_layout.setContentsMargins(40, 0, 40, 0)
        center_layout.setAlignment(Qt.AlignCenter)
        center_layout.setSpacing(16)

        lbl_hint = QLabel("Угадай кто это?")
        lbl_hint.setObjectName("accent")
        lbl_hint.setAlignment(Qt.AlignCenter)

        lbl_poem = QLabel(char["poem"])
        lbl_poem.setObjectName("poem")
        lbl_poem.setAlignment(Qt.AlignCenter)
        lbl_poem.setWordWrap(True)

        btn_row = QWidget()
        btn_row_layout = QHBoxLayout(btn_row)
        btn_row_layout.setAlignment(Qt.AlignCenter)
        btn_row_layout.setSpacing(20)

        btn_back = QPushButton("Назад")
        btn_back.setObjectName("back_btn")
        btn_back.setFixedSize(140, 44)
        btn_back.clicked.connect(master.show_choice)

        btn_next = QPushButton("Далее")
        btn_next.setFixedSize(140, 44)
        btn_next.clicked.connect(lambda: master.show_photo(char_index))

        btn_row_layout.addWidget(btn_back)
        btn_row_layout.addWidget(btn_next)

        center_layout.addWidget(lbl_hint)
        center_layout.addWidget(lbl_poem)
        center_layout.addSpacing(16)
        center_layout.addWidget(btn_row)

        layout.addWidget(center, stretch=1)


class PhotoScreen(QWidget):
    def __init__(self, master, char_index):
        super().__init__()
        char = CHARACTERS[char_index]
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        top_bar = QFrame()
        top_bar.setFixedHeight(4)
        top_bar.setStyleSheet("background-color: #5865f2;")
        layout.addWidget(top_bar)

        center = QWidget()
        center_layout = QVBoxLayout(center)
        center_layout.setContentsMargins(40, 0, 40, 0)
        center_layout.setAlignment(Qt.AlignCenter)
        center_layout.setSpacing(16)

        lbl_title = QLabel("Вот кто это!")
        lbl_title.setStyleSheet("font-size: 22px; font-weight: bold;")
        lbl_title.setAlignment(Qt.AlignCenter)

        lbl_photo = QLabel()
        lbl_photo.setAlignment(Qt.AlignCenter)
        lbl_photo.setFixedSize(300, 300)
        photo_path = char["photo"]
        if os.path.exists(photo_path):
            pixmap = QPixmap(photo_path).scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            lbl_photo.setPixmap(pixmap)
        else:
            lbl_photo.setText("Фото не найдено\nassets/person{}.jpg".format(char_index + 1))
            lbl_photo.setStyleSheet("background-color: #1e1e2e; border-radius: 12px; color: #555577; font-size: 14px;")
            lbl_photo.setAlignment(Qt.AlignCenter)

        lbl_name = QLabel(char["name"])
        lbl_name.setObjectName("name_label")
        lbl_name.setAlignment(Qt.AlignCenter)

        btn_back = QPushButton("Назад к подсказке")
        btn_back.setObjectName("back_btn")
        btn_back.setFixedSize(200, 44)
        btn_back.clicked.connect(lambda: master.show_poem(char_index))

        center_layout.addWidget(lbl_title)
        center_layout.addWidget(lbl_photo, alignment=Qt.AlignCenter)
        center_layout.addWidget(lbl_name)
        center_layout.addSpacing(8)
        center_layout.addWidget(btn_back, alignment=Qt.AlignCenter)

        layout.addWidget(center, stretch=1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
