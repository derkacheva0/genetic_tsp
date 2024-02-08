from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from Mediator import *


class MyPaintWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.figure = plt.gcf()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.canvas.mpl_connect("button_press_event", self._on_left_click)
        self.axes = self.figure.add_subplot(211)
        self.axes2 = self.figure.add_subplot(212)
        self.axes.set_xlim([1, 30])
        self.axes.set_ylim([1, 30])
        self.cities = []

        layout_canvas = QtWidgets.QVBoxLayout(self)
        layout_canvas.addWidget(self.canvas)

    def _on_left_click(self, event):
        x = event.xdata
        y = event.ydata

        if x and y and x > 1 and y > 1:
            self.axes.scatter(x, y, s=30)
            self.cities.append((x, y))
            self.figure.canvas.draw()

    def get_cities(self):
        return self.cities

    def set_cities(self, cities):
        self.cities.extend(cities)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(951, 859)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Georgian")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 0, 211, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 211, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 760, 181, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.mediator = None
        self.population_history = None
        self.current_index = 0
        self.step = 1
        self.pages = 0
        self.current_page = 0

        self.sc = MyPaintWidget(self.centralwidget)
        self.sc.setGeometry(QtCore.QRect(280, 0, 451, 781))
        self.sc.setObjectName("sc")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 211, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 230, 241, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")

        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(40, 40, 160, 22))
        self.horizontalSlider.setMaximum(10000)
        self.horizontalSlider.setPageStep(1000)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider.setTickInterval(1000)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(40, 120, 160, 22))
        self.horizontalSlider_2.setMaximum(100000)
        self.horizontalSlider_2.setPageStep(100)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")

        self.horizontalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(40, 200, 160, 22))
        self.horizontalSlider_3.setMaximum(100)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")

        self.horizontalSlider_4 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(40, 290, 160, 22))
        self.horizontalSlider_4.setMaximum(100)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 390, 181, 22))
        self.comboBox.setObjectName("comboBox")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 340, 241, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName("label_5")

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(40, 480, 181, 22))
        self.comboBox_2.setObjectName("comboBox_2")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 430, 241, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setScaledContents(False)
        self.label_6.setObjectName("label_6")

        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(40, 650, 181, 22))
        self.comboBox_3.setObjectName("comboBox_3")

        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(40, 560, 181, 22))
        self.comboBox_4.setObjectName("comboBox_4")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 520, 241, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setScaledContents(False)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 610, 241, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setScaledContents(False)
        self.label_8.setObjectName("label_8")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(735, 150, 180, 28))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(735, 180, 180, 28))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(735, 300, 180, 28)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(735, 330, 180, 28)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(735, 35, 180, 28)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(735, 65, 180, 28)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(735, 95, 180, 28)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(220, 40, 50, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(220, 120, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(220, 200, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(220, 290, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(750, 210, 121, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setScaledContents(False)
        self.label_13.setObjectName("label_13")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 848, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TSP"))
        self.label.setText(_translate("MainWindow", "Размер популяции"))
        self.label_2.setText(_translate("MainWindow", "Количество поколений"))
        self.pushButton.setText(_translate("MainWindow", "Запустить алгоритм"))
        self.label_3.setText(_translate("MainWindow", "Вероятность мутации"))
        self.label_4.setText(_translate("MainWindow", "Вероятность кроссинговера"))
        self.label_5.setText(_translate("MainWindow", "Вид кроссинговера"))
        self.label_6.setText(_translate("MainWindow", "Вид мутации"))
        self.label_7.setText(_translate("MainWindow", "Выбор родителей"))
        self.label_8.setText(_translate("MainWindow", "Вид селекции"))
        self.pushButton_2.setText(_translate("MainWindow", "Вперед"))
        self.pushButton_3.setText(_translate("MainWindow", "Назад"))
        self.pushButton_4.setText(_translate("MainWindow", "На первую стр."))
        self.pushButton_5.setText(_translate("MainWindow", "На последнюю стр."))
        self.pushButton_6.setText(_translate("MainWindow", "Сгенерировать города"))
        self.pushButton_7.setText(_translate("MainWindow", "Загрузить из файла"))
        self.pushButton_8.setText(_translate("MainWindow", "Очистить города"))
        self.label_13.setText(_translate("MainWindow", "Стр. 0 из 0"))
        self.label_9.setText(str(self.horizontalSlider.value()))
        self.label_10.setText(str(self.horizontalSlider_2.value()))
        self.label_11.setText(str(self.horizontalSlider_3.value()))
        self.label_12.setText(str(self.horizontalSlider_4.value()))
        self.setup_combobox_crossover()
        self.setup_combobox_mutation()
        self.setup_combobox_selection()
        self.setup_combobox_parent_selection()

    def set_mediator(self, mediator):
        self.mediator = mediator

    def add_functions(self):
        self.pushButton.clicked.connect(self.start)
        self.horizontalSlider.valueChanged.connect(self.change_crossover_label)
        self.horizontalSlider_2.valueChanged.connect(self.change_mutation_label)
        self.horizontalSlider_3.valueChanged.connect(self.change_selection_label)
        self.horizontalSlider_4.valueChanged.connect(self.change_parent_selection_label)
        self.pushButton_2.clicked.connect(self.forward)
        self.pushButton_3.clicked.connect(self.backward)
        self.pushButton_4.clicked.connect(self.go_to_first_page)
        self.pushButton_5.clicked.connect(self.go_to_last_page)
        self.pushButton_6.clicked.connect(self.generate_cities)
        self.pushButton_7.clicked.connect(self.read_cities)
        self.pushButton_8.clicked.connect(self.remove_cities)

    def start(self):
        self.mediator.run()
        self.sc.axes.clear()
        self.sc.axes2.clear()
        self.sc.axes.set_xlim([1, 30])
        self.sc.axes.set_ylim([1, 30])
        self.draw_cities()
        self.draw_cost_function()
        self.current_index = len(self.population_history) - 1
        self.step = int(0.05 * len(self.population_history))
        self.pages = len(self.population_history) // self.step + 1
        self.current_page = self.pages
        self.draw_history(self.current_index)
        self.change_page_label()
        print(self.population_history)

    def draw_history(self, index):
        way = None
        generation = self.population_history[index]
        min_element = min(generation.values())
        for i, item in enumerate(generation.items()):
            if item[1] == min_element:
                way = item[0]
                break
        for i in range(len(way) - 1):
            x = [self.sc.cities[way[i]][0], self.sc.cities[way[i + 1]][0]]
            y = [self.sc.cities[way[i]][1], self.sc.cities[way[i + 1]][1]]
            self.sc.axes.plot(x, y)
        self.sc.figure.canvas.draw()

    def draw_cost_function(self):
        x = list(range(len(self.population_history)))
        y = [min(self.population_history[i].values()) for i in range(len(self.population_history))]
        self.sc.axes2.plot(x, y)
        self.sc.figure.canvas.draw()

    def draw_cities(self):
        for item in self.sc.cities:
            x = item[0]
            y = item[1]
            self.sc.axes.scatter(x, y)
        self.sc.figure.canvas.draw()

    def forward(self):
        if self.population_history and self.current_index + self.step < len(self.population_history):
            self.sc.axes.clear()
            self.sc.axes.set_xlim([1, 30])
            self.sc.axes.set_ylim([1, 30])
            self.draw_cities()
            self.current_index += self.step
            self.current_page += 1
            self.draw_history(self.current_index)
            self.change_page_label()

    def backward(self):
        if self.population_history and self.current_index - self.step >= 0:
            self.sc.axes.clear()
            self.sc.axes.set_xlim([1, 30])
            self.sc.axes.set_ylim([1, 30])
            self.draw_cities()
            self.current_index -= self.step
            self.current_page -= 1
            self.draw_history(self.current_index)
            self.change_page_label()

    def go_to_first_page(self):
        if self.population_history:
            self.sc.axes.clear()
            self.sc.axes.set_xlim([1, 30])
            self.sc.axes.set_ylim([1, 30])
            self.draw_cities()
            self.current_index = len(self.population_history) - (self.pages - 1) * self.step
            self.current_page = 1
            self.draw_history(self.current_index)
            self.change_page_label()

    def go_to_last_page(self):
        if self.population_history:
            self.sc.axes.clear()
            self.sc.axes.set_xlim([1, 30])
            self.sc.axes.set_ylim([1, 30])
            self.draw_cities()
            self.current_index = len(self.population_history) - 1
            self.current_page = self.pages
            self.draw_history(self.current_index)
            self.change_page_label()

    def change_page_label(self):
        self.label_13.setText('Стр. ' + str(self.current_page) + ' из ' + str(self.pages))

    def change_crossover_label(self):
        self.label_9.setText(str(self.horizontalSlider.value()))

    def change_mutation_label(self):
        self.label_10.setText(str(self.horizontalSlider_2.value()))

    def change_selection_label(self):
        self.label_11.setText(str(self.horizontalSlider_3.value()))

    def change_parent_selection_label(self):
        self.label_12.setText(str(self.horizontalSlider_4.value()))

    def setup_combobox_crossover(self):
        self.comboBox.addItems(['SinglePointCrossover', 'TwoPointCrossover', 'UniformCrossover'])

    def setup_combobox_mutation(self):
        self.comboBox_2.addItems(['SwapMutation', 'UniformMutation', 'ScrambleMutation'])

    def setup_combobox_selection(self):
        self.comboBox_3.addItems(['RandomSelection', 'EliteSelection', 'ExclusionSelection'])

    def setup_combobox_parent_selection(self):
        self.comboBox_4.addItems(['Panmixia', 'TournamentParentSelection', 'RoulleteWheelParentSelection'])

    def read_cities(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, 'Open File', '.', 'TXT File (*.txt)')[0]
        if path:
            self.mediator.read_data(path)
            self.draw_cities()

    def generate_cities(self):
        self.mediator.generate_data()
        self.draw_cities()

    def remove_cities(self):
        self.sc.cities.clear()
        self.population_history = None
        self.sc.axes.clear()
        self.sc.axes2.clear()
        self.sc.axes.set_xlim([1, 30])
        self.sc.axes.set_ylim([1, 30])
        self.sc.figure.canvas.draw()