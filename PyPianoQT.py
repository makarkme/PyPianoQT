import sys
import design
from PyQt5.QtCore import Qt
from PyQt5.QtMultimedia import QSound  # Для работы со звуком
from multiprocessing import Process
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QAction, QPlainTextEdit
import time


class PyPianoQt(design.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(PyPianoQt, self).__init__()
        self.setupUi(self)  # Импорт дизайна.

        self.about_action = QAction(self)  # Для кнопки с инструкцией.
        self.about_action.setText("Инструкция")
        self.about_action.triggered.connect(self.about)  # Подключаем кнопку к функции about().
        self.menuBar().addAction(self.about_action)  # Подключаем кнопку к menuBar.

        self.about_action_1 = QAction(self)
        self.about_action_1.setText("Play")
        self.about_action_1.triggered.connect(self.play_thread)
        self.menuBar().addAction(self.about_action_1)

        self.about_program = AboutProgram()  # Чтобы каждый раз не создавать новое окно при нажатии.

        # Подключение регистров.
        self.lower_.triggered.connect(self.lower_case)
        self.lower_.setCheckable(True)
        self.middle_.triggered.connect(self.middle_case)
        self.middle_.setCheckable(True)
        self.high_.triggered.connect(self.high_case)
        self.high_.setCheckable(True)

        # Словарь, где ключ - клавиша на клавиатуре, значение - порядковый номер (нужен для перебора).
        self.keyword = {Qt.Key_Q: 0, Qt.Key_W: 1, Qt.Key_E: 2, Qt.Key_R: 3, Qt.Key_T: 4, Qt.Key_Y: 5, Qt.Key_U: 6,
                        Qt.Key_I: 7, Qt.Key_O: 8, Qt.Key_P: 9, Qt.Key_BracketLeft: 10, Qt.Key_BracketRight: 11,
                        Qt.Key_A: 12, Qt.Key_S: 13, Qt.Key_D: 14, Qt.Key_F: 15, Qt.Key_G: 16, Qt.Key_H: 17,
                        Qt.Key_J: 18, Qt.Key_K: 19, Qt.Key_L: 20, Qt.Key_Semicolon: 21, Qt.Key_Apostrophe: 22,
                        Qt.Key_Backslash: 23}

        # Словарь, где ключ - имя регистра, а значение - список названий звуков, которые относятся к этому регистру.
        # Чтоб не прописывать подключение 72 клавиш в ручную.

        # Почему такой кривой нейминг. Всё просто - ноты в английском алфавите записываются как буквы алфавита,
        # но начинаются они не с ноты До (как у нас), а с ноты Ля. То есть Ля мажор - это a-dur и так далее.
        # Цифры после буков обозначают регистр и значение октавы в регистре
        # (таким образом, нота Ля 1 регистра 1 октавы обозначается как a_1_1)
        # + a_b_1_1 - это нота (черная) между a_1_1 и b_1_1. Так по аналогии все остальные.
        self.keys = {"lower": ["a_1_1", "a_b_1_1", "b_1_1", "c_1_1", "c_d_1_1", "d_1_1",
                               "d_e_1_1", "e_1_1", "f_1_1", "f_g_1_1", "g_1_1", "g_a_1_1",
                               "a_2_1", "a_b_2_1", "b_2_1", "c_2_1", "c_d_2_1", "d_2_1",
                               "d_e_2_1", "e_2_1", "f_2_1", "f_g_2_1", "g_2_1", "g_a_2_1"],
                     "middle": ["a_1_2", "a_b_1_2", "b_1_2", "c_1_2", "c_d_1_2", "d_1_2",
                                "d_e_1_2", "e_1_2", "f_1_2", "f_g_1_2", "g_1_2", "g_a_1_2",
                                "a_2_2", "a_b_2_2", "b_2_2", "c_2_2", "c_d_2_2", "d_2_2",
                                "d_e_2_2", "e_2_2", "f_2_2", "f_g_2_2", "g_2_2", "g_a_2_2"],
                     "high": ["a_1_3", "a_b_1_3", "b_1_3", "c_1_3", "c_d_1_3", "d_1_3",
                              "d_e_1_3", "e_1_3", "f_1_3", "f_g_1_3", "g_1_3", "g_a_1_3",
                              "a_2_3", "a_b_2_3", "b_2_3", "c_2_3", "c_d_2_3", "d_2_3",
                              "d_e_2_3", "e_2_3", "f_2_3", "f_g_2_3", "g_2_3", "g_a_2_3"]}
        # (Звуки записывал сам, в интернете не нашёл всех 72 звуков).

    def lower_case(self):  # Функция нижнего регистра (остальные работают так же).
        self.actions(1)  # Для перебора словаря списков. Цифра 1 отвечает за нижний регистр.
        count = 0
        for i in self.buttonGroup_keys.buttons():  # Группа клавиш. Удобно подключить всё сразу, а не по одной.
            # Отключает кнопку от клавиши.
            # Нужно, чтобы потом при переключении регистра к клавише не была привязана старая нота с прошлого регистра.
            # Завернуто в try, т.к при первом включении выдаёт ошибку, а так - всё работает.
            try:
                i.clicked.disconnect()
            except TypeError:
                pass
            # Выбрал именно QSound, т.к легко взаимодействует с PyQt5
            # + звуки могут наслаиваться друг на друга практически без задержки.
            sound = QSound(f"Sounds/{self.keys['lower'][count]}.wav", self)  # Переменная, где лежит звук.
            # + Используем словарь self.keys
            i.clicked.connect(sound.play)  # Подключаем.
            count += 1  # Позволяет организовать перебор клавиш.

    def middle_case(self):  # Принцип работы как у lower_case.
        self.actions(2)
        count = 0
        for i in self.buttonGroup_keys.buttons():
            try:
                i.clicked.disconnect()
            except TypeError:
                pass
            sound = QSound(f"Sounds/{self.keys['middle'][count]}.wav", self)
            i.clicked.connect(sound.play)
            count += 1

    def high_case(self):  # Принцип работы как у lower_case.
        self.actions(3)
        count = 0
        for i in self.buttonGroup_keys.buttons():
            try:
                i.clicked.disconnect()
            except TypeError:
                pass
            sound = QSound(f"Sounds/{self.keys['high'][count]}.wav", self)
            i.clicked.connect(sound.play)
            count += 1

    # def play_input_data(self):
    #     with open("input_data.txt", "r", encoding="utf-8") as file:
    #         read_file = file.read().split(" ")
    #
    #         for index in range(len(read_file)):
    #             sound = QSound(f"Sounds/{read_file[index]}.wav", self)

    def actions(self, number):  # Костыльно, но с пивом потянет.
        # Нужно, чтобы какой-то регистр всегда был активен, а все остальные при этом не активны.
        if number == 1:
            if self.middle_.isChecked():  # Проверочка.
                self.middle_.setChecked(False)
            if self.high_.isChecked():
                self.high_.setChecked(False)
            if not self.lower_.isChecked():
                self.lower_.setChecked(True)
        elif number == 2:
            if self.lower_.isChecked():
                self.lower_.setChecked(False)
            if self.high_.isChecked():
                self.high_.setChecked(False)
            if not self.middle_.isChecked():
                self.middle_.setChecked(True)
        elif number == 3:
            if self.lower_.isChecked():
                self.lower_.setChecked(False)
            if self.middle_.isChecked():
                self.middle_.setChecked(False)
            if not self.high_.isChecked():
                self.high_.setChecked(True)

    def keyPressEvent(self, event):  # Подключаем клавиатуру.
        # Чтоб не вылетало при нажатии посторонних клавиш.
        try:
            self.keyword[event.key()]
        except KeyError:
            return None
        if self.lower_.isChecked():  # Проверочка.
            # Тут мы прописываем путь к звуку, используя наш словарь со значениями в виде списков
            # + звук записывается только при нажатой клавише. (значения словаря для клавиатуры)
            sound = QSound(f"Sounds/{self.keys['lower'][self.keyword[event.key()]]}.wav", self)
            sound.play()
        elif self.middle_.isChecked():  # С остальными так же.
            sound = QSound(f"Sounds/{self.keys['middle'][self.keyword[event.key()]]}.wav", self)
            sound.play()
        elif self.high_.isChecked():
            sound = QSound(f"Sounds/{self.keys['high'][self.keyword[event.key()]]}.wav", self)
            sound.play()

    def about(self):  # Выводим нашу инструкцию.
        self.about_program.show()

    def play_thread(self):
        t = Process(target=play, args=(self,))
        t.run()


class AboutProgram(QWidget):  # Окно с инструкцией.
    def __init__(self):
        super().__init__()

        self.info = QPlainTextEdit()  # Чтоб прочитать txt файл.
        text = open('manual.txt', 'r', encoding='utf-8').read()

        self.setWindowTitle("Инструкция")  # Немного дизайна.
        self.setLayout(QVBoxLayout())
        self.info = QLabel(self)
        self.info.setText(text)  # Вставляем текст.
        self.layout().addWidget(self.info)

        self.setStyleSheet(  # Ещё дизайн.
            "background-color: black; "
            "color: white;"
            "font: 12pt 'Times New Roman'"
        )


def play(self):
    file = open("input_data.txt", "r", encoding="utf-8")

    data = file.read().split()
    print(data)
    for i in range(len(data)):
        print(data[i])
        time.sleep(1)
        # sound = QSound(f"Sounds/{data[i]}.wav", self)
        # sound.play()
        QSound.play(f"Sounds/{data[i]}.wav")


if __name__ == "__main__":  # Пуск.
    app = QApplication(sys.argv)
    ex = PyPianoQt()
    ex.show()
    sys.exit(app.exec())

# Тут на 160 строк + файл дизайнера (около 700).
# Могло выйти меньше, но я не могу его редачить, т.к он не запустится с изменениями,
# а переписывать 700 строк в отдельный файл, а уж тем более в main проекта глупо,
# т.к. его нельзя редактировать в дизайнере.
# P.S Надеюсь, чистота кода в файле дизайнера не оценивается.
