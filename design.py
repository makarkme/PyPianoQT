# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1075, 700)
        MainWindow.setMaximumSize(QtCore.QSize(1075, 700))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: black")
        self.centralwidget.setObjectName("centralwidget")
        self.a = QtWidgets.QPushButton(self.centralwidget)
        self.a.setGeometry(QtCore.QRect(-11, 170, 81, 500))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a.sizePolicy().hasHeightForWidth())
        self.a.setSizePolicy(sizePolicy)
        self.a.setMinimumSize(QtCore.QSize(0, 0))
        self.a.setSizeIncrement(QtCore.QSize(0, 0))
        self.a.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Cramaten")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.a.setFont(font)
        self.a.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.a.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    font: 26pt \"Cramaten\";\n"
"    font: 26pt \"Cramaten\";\n"
"    border: 1px solid white;\n"
"    border-radius: 5;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border: 1px solid grey;\n"
"    border-radius: 5\n"
"}\n"
"")
        self.a.setText("")
        self.a.setIconSize(QtCore.QSize(16, 16))
        self.a.setObjectName("a")
        self.buttonGroup_keys = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_keys.setObjectName("buttonGroup_keys")
        self.buttonGroup_keys.addButton(self.a)
        self.b = QtWidgets.QPushButton(self.centralwidget)
        self.b.setGeometry(QtCore.QRect(50, 167, 40, 340))
        font = QtGui.QFont()
        font.setFamily("Cramaten")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.b.setFont(font)
        self.b.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.b.setStyleSheet("QPushButton {\n"
"    background-color: black;\n"
"    font: 16pt \"Cramaten\";\n"
"    font: 20pt \"Cramaten\";\n"
"    font: 20pt \"Cramaten\";\n"
"    font: 26pt \"Cramaten\";\n"
"    border: 1px solid black;\n"
"    border-radius: 5;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border: 1px solid grey;\n"
"    border-radius: 5\n"
"}\n"
"\n"
"")
        self.b.setText("")
        self.b.setObjectName("b")
        self.buttonGroup_keys.addButton(self.b)
        self.c = QtWidgets.QPushButton(self.centralwidget)
        self.c.setGeometry(QtCore.QRect(75, 170, 70, 500))
        self.c.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.c.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    font: 26pt \"Cramaten\";\n"
"    font: 26pt \"Cramaten\";\n"
"    border: 1px solid white;\n"
"    border-radius: 5;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border: 1px solid grey;\n"
"    border-radius: 5\n"
"}\n"
"")
        self.c.setText("")
        self.c.setObjectName("c")
        self.buttonGroup_keys.addButton(self.c)
        self.d = QtWidgets.QPushButton(self.centralwidget)
        self.d.setGeometry(QtCore.QRect(150, 170, 70, 500))
        self.d.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.d.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    font: 26pt \"Cramaten\";\n"
"    font: 26pt \"Cramaten\";\n"
"    border: 1px solid white;\n"
"    border-radius: 5;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border: 1px solid grey;\n"
"    border-radius: 5\n"
"}\n"
"")
        self.d.setText("")
        self.d.setObjectName("d")
        self.buttonGroup_keys.addButton(self.d)
        self.e = QtWidgets.QPushButton(self.centralwidget)
        self.e.setGeometry(QtCore.QRect(200, 167, 40, 340))
        font = QtGui.QFont()
        font.setFamily("Cramaten")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.e.setFont(font)
        self.e.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.e.setStyleSheet("QPushButton {\n"
"    background-color: black;\n"
"    font: 16pt \"Cramaten\";\n"
"    font: 20pt \"Cramaten\";\n"
"    font: 20pt \"Cramaten\";\n"
"    font: 26pt \"Cramaten\";\n"
"    border: 1px solid black;\n"
"    border-radius: 5;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border: 1px solid grey;\n"
"    border-radius: 5\n"
"}\n"
"\n"
"")
        self.e.setText("")
        self.e.setObjectName("e")
        self.buttonGroup_keys.addButton(self.e)
        self.f = QtWidgets.QPushButton(self.centralwidget)
        self.f.setGeometry(QtCore.QRect(225, 170, 70, 500))
        self.f.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.f.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    font: 26pt \"Cramaten\";\n"
"    font: 26pt \"Cramaten\";\n"
"    border: 1px solid white;\n"
"    border-radius: 5;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border: 1px solid grey;\n"
"    border-radius: 5\n"
"}\n"
"")
        self.f.setText("")
        self.f.setObjectName("f")
        self.buttonGroup_keys.addButton(self.f)
        self.g = QtWidgets.QPushButton(self.centralwidget)
        self.g.setGeometry(QtCore.QRect(280, 167, 40, 340))
        font = QtGui.QFont()
        font.setFamily("Cramaten")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.g.setFont(font)
        self.g.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.g.setStyleSheet("QPushButton {\n"
"    background-color: black;\n"
"    font: 16pt \"Cramaten\";\n"
"    font: 20pt \"Cramaten\";\n"
"    font: 20pt \"Cramaten\";\n"
"    font: 26pt \"Cramaten\";\n"
"    border: 1px solid black;\n"
"    border-radius: 5;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border: 1px solid grey;\n"
"    border-radius: 5\n"
"}\n"
"\n"
"")
        self.g.setText("")
        self.g.setObjectName("g")
        self.buttonGroup_keys.addButton(self.g)
        self.h = QtWidgets.QPushButton(self.centralwidget)
        self.h.setGeometry(QtCore.QRect(300, 170, 70, 500))
        self.h.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.h.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    font: 26pt \"Cramaten\";\n"
"    font: 26pt \"Cramaten\";\n"
"    border: 1px solid white;\n"
"    border-radius: 5;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border: 1px solid grey;\n"
"    border-radius: 5\n"
"}\n"
"")
        self.h.setText("")
        self.h.setObjectName("h")
        self.buttonGroup_keys.addButton(self.h)
        self.i = QtWidgets.QPushButton(self.centralwidget)
        self.i.setGeometry(QtCore.QRect(375, 170, 70, 500))
        self.i.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.i.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    font: 26pt \"Cramaten\";\n"
"    font: 26pt \"Cramaten\";\n"
"    border: 1px solid white;\n"
"    border-radius: 5;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border: 1px solid grey;\n"
"    border-radius: 5\n"
"}\n"
"")
        self.i.setText("")
        self.i.setObjectName("i")
        self.buttonGroup_keys.addButton(self.i)
        self.j = QtWidgets.QPushButton(self.centralwidget)
        self.j.setGeometry(QtCore.QRect(430, 167, 40, 340))
        font = QtGui.QFont()
        font.setFamily("Cramaten")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.j.setFont(font)
        self.j.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.j.setStyleSheet("QPushButton {\n"
"    background-color: black;\n"
"    font: 16pt \"Cramaten\";\n"
"    font: 20pt \"Cramaten\";\n"
"    font: 20pt \"Cramaten\";\n"
"    font: 26pt \"Cramaten\";\n"
"    border: 1px solid black;\n"
"    border-radius: 5;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border: 1px solid grey;\n"
"    border-radius: 5\n"
"}\n"
"\n"
"")
        self.j.setText("")
        self.j.setObjectName("j")
        self.buttonGroup_keys.addButton(self.j)
        self.k = QtWidgets.QPushButton(self.centralwidget)
        self.k.setGeometry(QtCore.QRect(450, 170, 70, 500))
        self.k.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.k.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    font: 26pt \"Cramaten\";\n"
"    font: 26pt \"Cramaten\";\n"
"    border: 1px solid white;\n"
"    border-radius: 5;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border: 1px solid grey;\n"
"    border-radius: 5\n"
"}\n"
"")
        self.k.setText("")
        self.k.setObjectName("k")
        self.buttonGroup_keys.addButton(self.k)
        self.l = QtWidgets.QPushButton(self.centralwidget)
        self.l.setGeometry(QtCore.QRect(500, 167, 40, 340))
        font = QtGui.QFont()
        font.setFamily("Cramaten")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.l.setFont(font)
        self.l.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.l.setStyleSheet("QPushButton {\n"
"    background-color: black;\n"
"    font: 16pt \"Cramaten\";\n"
"    font: 20pt \"Cramaten\";\n"
"    font: 20pt \"Cramaten\";\n"
"    font: 26pt \"Cramaten\";\n"
"    border: 1px solid black;\n"
"    border-radius: 5;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border: 1px solid grey;\n"
"    border-radius: 5\n"
"}\n"
"\n"
"")
        self.l.setText("")
        self.l.setObjectName("l")
        self.buttonGroup_keys.addButton(self.l)
        self.m = QtWidgets.QPushButton(self.centralwidget)
        self.m.setGeometry(QtCore.QRect(525, 170, 70, 500))
        self.m.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.m.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    font: 26pt \"Cramaten\";\n"
"    font: 26pt \"Cramaten\";\n"
"    border: 1px solid white;\n"
"    border-radius: 5;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border: 1px solid grey;\n"
"    border-radius: 5\n"
"}\n"
"")
        self.m.setText("")
        self.m.setObjectName("m")
        self.buttonGroup_keys.addButton(self.m)
        self.n = QtWidgets.QPushButton(self.centralwidget)
        self.n.setGeometry(QtCore.QRect(580, 167, 40, 340))
        font = QtGui.QFont()
        font.setFamily("Cramaten")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.n.setFont(font)
        self.n.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.n.setStyleSheet("QPushButton {\n"
"    background-color: black;\n"
"    font: 16pt \"Cramaten\";\n"
"    font: 20pt \"Cramaten\";\n"
"    font: 20pt \"Cramaten\";\n"
"    font: 26pt \"Cramaten\";\n"
"    border: 1px solid black;\n"
"    border-radius: 5;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border: 1px solid grey;\n"
"    border-radius: 5\n"
"}\n"
"\n"
"")
        self.n.setText("")
        self.n.setObjectName("n")
        self.buttonGroup_keys.addButton(self.n)
        self.o = QtWidgets.QPushButton(self.centralwidget)
        self.o.setGeometry(QtCore.QRect(600, 170, 70, 500))
        self.o.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.o.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    font: 26pt \"Cramaten\";\n"
"    font: 26pt \"Cramaten\";\n"
"    border: 1px solid white;\n"
"    border-radius: 5;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border: 1px solid grey;\n"
"    border-radius: 5\n"
"}\n"
"")
        self.o.setText("")
        self.o.setObjectName("o")
        self.buttonGroup_keys.addButton(self.o)
        self.p = QtWidgets.QPushButton(self.centralwidget)
        self.p.setGeometry(QtCore.QRect(675, 170, 70, 500))
        self.p.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.p.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    font: 26pt \"Cramaten\";\n"
"    font: 26pt \"Cramaten\";\n"
"    border: 1px solid white;\n"
"    border-radius: 5;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border: 1px solid grey;\n"
"    border-radius: 5\n"
"}\n"
"")
        self.p.setText("")
        self.p.setObjectName("p")
        self.buttonGroup_keys.addButton(self.p)
        self.q = QtWidgets.QPushButton(self.centralwidget)
        self.q.setGeometry(QtCore.QRect(730, 167, 40, 340))
        font = QtGui.QFont()
        font.setFamily("Cramaten")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.q.setFont(font)
        self.q.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.q.setStyleSheet("QPushButton {\n"
"    background-color: black;\n"
"    font: 16pt \"Cramaten\";\n"
"    font: 20pt \"Cramaten\";\n"
"    font: 20pt \"Cramaten\";\n"
"    font: 26pt \"Cramaten\";\n"
"    border: 1px solid black;\n"
"    border-radius: 5;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border: 1px solid grey;\n"
"    border-radius: 5\n"
"}\n"
"\n"
"")
        self.q.setText("")
        self.q.setObjectName("q")
        self.buttonGroup_keys.addButton(self.q)
        self.r = QtWidgets.QPushButton(self.centralwidget)
        self.r.setGeometry(QtCore.QRect(750, 170, 70, 500))
        self.r.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.r.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    font: 26pt \"Cramaten\";\n"
"    font: 26pt \"Cramaten\";\n"
"    border: 1px solid white;\n"
"    border-radius: 5;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border: 1px solid grey;\n"
"    border-radius: 5\n"
"}\n"
"")
        self.r.setText("")
        self.r.setObjectName("r")
        self.buttonGroup_keys.addButton(self.r)
        self.s = QtWidgets.QPushButton(self.centralwidget)
        self.s.setGeometry(QtCore.QRect(810, 167, 40, 340))
        font = QtGui.QFont()
        font.setFamily("Cramaten")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.s.setFont(font)
        self.s.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.s.setStyleSheet("QPushButton {\n"
"    background-color: black;\n"
"    font: 16pt \"Cramaten\";\n"
"    font: 20pt \"Cramaten\";\n"
"    font: 20pt \"Cramaten\";\n"
"    font: 26pt \"Cramaten\";\n"
"    border: 1px solid black;\n"
"    border-radius: 5;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border: 1px solid grey;\n"
"    border-radius: 5\n"
"}\n"
"\n"
"")
        self.s.setText("")
        self.s.setObjectName("s")
        self.buttonGroup_keys.addButton(self.s)
        self.t = QtWidgets.QPushButton(self.centralwidget)
        self.t.setGeometry(QtCore.QRect(825, 170, 70, 500))
        self.t.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.t.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    font: 26pt \"Cramaten\";\n"
"    font: 26pt \"Cramaten\";\n"
"    border: 1px solid white;\n"
"    border-radius: 5;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border: 1px solid grey;\n"
"    border-radius: 5\n"
"}\n"
"")
        self.t.setText("")
        self.t.setObjectName("t")
        self.buttonGroup_keys.addButton(self.t)
        self.u = QtWidgets.QPushButton(self.centralwidget)
        self.u.setGeometry(QtCore.QRect(900, 170, 70, 500))
        self.u.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.u.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    font: 26pt \"Cramaten\";\n"
"    font: 26pt \"Cramaten\";\n"
"    border: 1px solid white;\n"
"    border-radius: 5;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border: 1px solid grey;\n"
"    border-radius: 5\n"
"}\n"
"")
        self.u.setText("")
        self.u.setObjectName("u")
        self.buttonGroup_keys.addButton(self.u)
        self.v = QtWidgets.QPushButton(self.centralwidget)
        self.v.setGeometry(QtCore.QRect(950, 167, 40, 340))
        font = QtGui.QFont()
        font.setFamily("Cramaten")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.v.setFont(font)
        self.v.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.v.setStyleSheet("QPushButton {\n"
"    background-color: black;\n"
"    font: 16pt \"Cramaten\";\n"
"    font: 20pt \"Cramaten\";\n"
"    font: 20pt \"Cramaten\";\n"
"    font: 26pt \"Cramaten\";\n"
"    border: 1px solid black;\n"
"    border-radius: 5;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border: 1px solid grey;\n"
"    border-radius: 5\n"
"}\n"
"\n"
"")
        self.v.setText("")
        self.v.setObjectName("v")
        self.buttonGroup_keys.addButton(self.v)
        self.w = QtWidgets.QPushButton(self.centralwidget)
        self.w.setGeometry(QtCore.QRect(975, 170, 70, 500))
        self.w.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.w.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    font: 26pt \"Cramaten\";\n"
"    font: 26pt \"Cramaten\";\n"
"    border: 1px solid white;\n"
"    border-radius: 5;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border: 1px solid grey;\n"
"    border-radius: 5\n"
"}\n"
"")
        self.w.setText("")
        self.w.setObjectName("w")
        self.buttonGroup_keys.addButton(self.w)
        self.x = QtWidgets.QPushButton(self.centralwidget)
        self.x.setGeometry(QtCore.QRect(1030, 167, 40, 340))
        font = QtGui.QFont()
        font.setFamily("Cramaten")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.x.setFont(font)
        self.x.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.x.setStyleSheet("QPushButton {\n"
"    background-color: black;\n"
"    font: 16pt \"Cramaten\";\n"
"    font: 20pt \"Cramaten\";\n"
"    font: 20pt \"Cramaten\";\n"
"    font: 26pt \"Cramaten\";\n"
"    border: 1px solid black;\n"
"    border-radius: 5;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: grey;\n"
"    border: 1px solid grey;\n"
"    border-radius: 5\n"
"}\n"
"\n"
"")
        self.x.setText("")
        self.x.setObjectName("x")
        self.buttonGroup_keys.addButton(self.x)
        self.zzz = QtWidgets.QPushButton(self.centralwidget)
        self.zzz.setGeometry(QtCore.QRect(1050, 170, 70, 500))
        self.zzz.setStyleSheet("background-color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5;\n"
"color: black")
        self.zzz.setText("")
        self.zzz.setObjectName("zzz")
        self.zzz_2 = QtWidgets.QLabel(self.centralwidget)
        self.zzz_2.setGeometry(QtCore.QRect(6, -8, 1071, 171))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.zzz_2.setFont(font)
        self.zzz_2.setStyleSheet("background-color: black;\n"
"font: italic 28pt \"Rockwell\";\n"
"color: white")
        self.zzz_2.setAlignment(QtCore.Qt.AlignCenter)
        self.zzz_2.setObjectName("zzz_2")
        self.zzz.raise_()
        self.a.raise_()
        self.c.raise_()
        self.d.raise_()
        self.f.raise_()
        self.h.raise_()
        self.i.raise_()
        self.k.raise_()
        self.m.raise_()
        self.o.raise_()
        self.p.raise_()
        self.r.raise_()
        self.t.raise_()
        self.u.raise_()
        self.w.raise_()
        self.j.raise_()
        self.b.raise_()
        self.e.raise_()
        self.g.raise_()
        self.l.raise_()
        self.n.raise_()
        self.q.raise_()
        self.s.raise_()
        self.v.raise_()
        self.x.raise_()
        self.zzz_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1075, 21))
        self.menubar.setStyleSheet("background-color: black;\n"
"color: white;")
        self.menubar.setObjectName("menubar")
        self.case_ = QtWidgets.QMenu(self.menubar)
        self.case_.setStyleSheet("background-color: black;\n"
"color: white;\n"
"\n"
"")
        self.case_.setObjectName("case_")
        MainWindow.setMenuBar(self.menubar)
        self.lower_ = QtWidgets.QAction(MainWindow)
        self.lower_.setObjectName("lower_")
        self.middle_ = QtWidgets.QAction(MainWindow)
        self.middle_.setObjectName("middle_")
        self.high_ = QtWidgets.QAction(MainWindow)
        self.high_.setObjectName("high_")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.case_.addAction(self.lower_)
        self.case_.addAction(self.middle_)
        self.case_.addAction(self.high_)
        self.menubar.addAction(self.case_.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyPianoQT"))
        self.zzz_2.setText(_translate("MainWindow", "PyPianoQT - электронное фортепиано нового поколения"))
        self.case_.setTitle(_translate("MainWindow", "Регистр"))
        self.lower_.setText(_translate("MainWindow", "Нижний"))
        self.middle_.setText(_translate("MainWindow", "Средний"))
        self.high_.setText(_translate("MainWindow", "Высокий"))
        self.action_4.setText(_translate("MainWindow", "Русский"))
        self.action_5.setText(_translate("MainWindow", "Английский"))
