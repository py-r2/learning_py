# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookstore_gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from bkstore_bck import Database

database=Database('library.db')
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(659, 408)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_bkstorelabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_bkstorelabel.sizePolicy().hasHeightForWidth())
        self.label_bkstorelabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_bkstorelabel.setFont(font)
        self.label_bkstorelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.label_bkstorelabel.setObjectName("label_bkstorelabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_bkstorelabel)
        self.listView_records = QtWidgets.QListView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView_records.sizePolicy().hasHeightForWidth())
        self.listView_records.setSizePolicy(sizePolicy)
        self.listView_records.setBaseSize(QtCore.QSize(0, 0))
        self.listView_records.setObjectName("listView_records")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.listView_records)
        self.textBrowser_notes = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_notes.sizePolicy().hasHeightForWidth())
        self.textBrowser_notes.setSizePolicy(sizePolicy)
        self.textBrowser_notes.setObjectName("textBrowser_notes")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.textBrowser_notes)
        self.label_notes = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_notes.sizePolicy().hasHeightForWidth())
        self.label_notes.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_notes.setFont(font)
        self.label_notes.setAlignment(QtCore.Qt.AlignCenter)
        self.label_notes.setObjectName("label_notes")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_notes)
        self.gridLayout.addLayout(self.formLayout_3, 1, 3, 1, 3)
        self.pushButton_view = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_view.sizePolicy().hasHeightForWidth())
        self.pushButton_view.setSizePolicy(sizePolicy)
        self.pushButton_view.setObjectName("pushButton_view")
        self.gridLayout.addWidget(self.pushButton_view, 0, 0, 1, 1)
        self.pushButton_update = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_update.sizePolicy().hasHeightForWidth())
        self.pushButton_update.setSizePolicy(sizePolicy)
        self.pushButton_update.setObjectName("pushButton_update")
        self.gridLayout.addWidget(self.pushButton_update, 0, 4, 1, 1)
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout.addWidget(self.pushButton_add, 0, 1, 1, 1)
        self.pushButton_search = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_search.sizePolicy().hasHeightForWidth())
        self.pushButton_search.setSizePolicy(sizePolicy)
        self.pushButton_search.setObjectName("pushButton_search")
        self.gridLayout.addWidget(self.pushButton_search, 0, 3, 1, 1)
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_delete.sizePolicy().hasHeightForWidth())
        self.pushButton_delete.setSizePolicy(sizePolicy)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.gridLayout.addWidget(self.pushButton_delete, 0, 5, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_title.setIndent(0)
        self.label_title.setObjectName("label_title")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_title)
        self.lineEdit_title = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_title)
        self.label_author = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_author.setFont(font)
        self.label_author.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_author.setIndent(0)
        self.label_author.setObjectName("label_author")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_author)
        self.lineEdit_author = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_author.setObjectName("lineEdit_author")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_author)
        self.label_year = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_year.setFont(font)
        self.label_year.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_year.setIndent(0)
        self.label_year.setObjectName("label_year")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_year)
        self.lineEdit_year = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_year.setObjectName("lineEdit_year")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_year)
        self.label_isbn = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_isbn.setFont(font)
        self.label_isbn.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_isbn.setIndent(0)
        self.label_isbn.setObjectName("label_isbn")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_isbn)
        self.lineEdit_isbn = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_isbn.setObjectName("lineEdit_isbn")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_isbn)
        self.label_datein = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_datein.setFont(font)
        self.label_datein.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_datein.setIndent(0)
        self.label_datein.setObjectName("label_datein")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_datein)
        self.dateEdit_datein = QtWidgets.QDateEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_datein.sizePolicy().hasHeightForWidth())
        self.dateEdit_datein.setSizePolicy(sizePolicy)
        self.dateEdit_datein.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_datein.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_datein.setCalendarPopup(True)
        self.dateEdit_datein.setObjectName("dateEdit_datein")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dateEdit_datein)
        self.label_dateout = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_dateout.setFont(font)
        self.label_dateout.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_dateout.setIndent(0)
        self.label_dateout.setObjectName("label_dateout")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_dateout)
        self.dateEdit_dateout = QtWidgets.QDateEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_dateout.sizePolicy().hasHeightForWidth())
        self.dateEdit_dateout.setSizePolicy(sizePolicy)
        self.dateEdit_dateout.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_dateout.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_dateout.setCalendarPopup(True)
        self.dateEdit_dateout.setObjectName("dateEdit_dateout")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.dateEdit_dateout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.line)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.graphicsView)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 2)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 659, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuSchedule = QtWidgets.QMenu(self.menubar)
        self.menuSchedule.setObjectName("menuSchedule")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionView_All_Records = QtWidgets.QAction(MainWindow)
        self.actionView_All_Records.setObjectName("actionView_All_Records")
        self.actionAdd_New_Entry = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_Entry.setObjectName("actionAdd_New_Entry")
        self.actionSearch_item = QtWidgets.QAction(MainWindow)
        self.actionSearch_item.setObjectName("actionSearch_item")
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionDate_Out = QtWidgets.QAction(MainWindow)
        self.actionDate_Out.setObjectName("actionDate_Out")
        self.actionDate_In = QtWidgets.QAction(MainWindow)
        self.actionDate_In.setObjectName("actionDate_In")
        self.actionNotes = QtWidgets.QAction(MainWindow)
        self.actionNotes.setObjectName("actionNotes")
        self.actionAbout_us = QtWidgets.QAction(MainWindow)
        self.actionAbout_us.setObjectName("actionAbout_us")
        self.menuMenu.addAction(self.actionView_All_Records)
        self.menuMenu.addAction(self.actionAdd_New_Entry)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionSearch_item)
        self.menuMenu.addAction(self.actionUpdate)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionDelete)
        self.menuMenu.addAction(self.actionExit)
        self.menuSchedule.addAction(self.actionDate_Out)
        self.menuSchedule.addAction(self.actionDate_In)
        self.menuSchedule.addAction(self.actionNotes)
        self.menuAbout.addAction(self.actionAbout_us)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuSchedule.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_bkstorelabel.setText(_translate("MainWindow", "Bookstore records:"))
        self.label_notes.setText(_translate("MainWindow", "Notes:"))
        self.pushButton_view.setText(_translate("MainWindow", "View All"))
        self.pushButton_update.setText(_translate("MainWindow", "Update"))
        self.pushButton_add.setText(_translate("MainWindow", "Add item"))
        self.pushButton_search.setText(_translate("MainWindow", "Search"))
        self.pushButton_delete.setText(_translate("MainWindow", "Delete"))
        self.label_title.setText(_translate("MainWindow", "Title:"))
        self.label_author.setText(_translate("MainWindow", "Author:"))
        self.label_year.setText(_translate("MainWindow", "Year:"))
        self.label_isbn.setText(_translate("MainWindow", "ISBN:"))
        self.label_datein.setText(_translate("MainWindow", "Date_In:"))
        self.label_dateout.setText(_translate("MainWindow", "Date_Out:"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuSchedule.setTitle(_translate("MainWindow", "Schedule"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionView_All_Records.setText(_translate("MainWindow", "View All Records"))
        self.actionAdd_New_Entry.setText(_translate("MainWindow", "Add New Entry"))
        self.actionSearch_item.setText(_translate("MainWindow", "Search"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionDate_Out.setText(_translate("MainWindow", "Date_Out"))
        self.actionDate_In.setText(_translate("MainWindow", "Date_In"))
        self.actionNotes.setText(_translate("MainWindow", "Notes"))
        self.actionAbout_us.setText(_translate("MainWindow", "About us"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
