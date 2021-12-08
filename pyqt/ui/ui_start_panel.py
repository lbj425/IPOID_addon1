# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_panel.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_start_panel(object):
    def setupUi(self, start_panel):
        if not start_panel.objectName():
            start_panel.setObjectName(u"start_panel")
        start_panel.resize(846, 606)
        start_panel.setMinimumSize(QSize(0, 0))
        start_panel.setMaximumSize(QSize(16777215, 16777215))
        self.action_frequency = QAction(start_panel)
        self.action_frequency.setObjectName(u"action_frequency")
        self.action_filter = QAction(start_panel)
        self.action_filter.setObjectName(u"action_filter")
        self.centralwidget = QWidget(start_panel)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamilies([u"Arial"])
        self.centralwidget.setFont(font)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget_prepare = QTabWidget(self.centralwidget)
        self.tabWidget_prepare.setObjectName(u"tabWidget_prepare")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(13)
        font1.setBold(False)
        self.tabWidget_prepare.setFont(font1)
        self.tab_eyetracker = QWidget()
        self.tab_eyetracker.setObjectName(u"tab_eyetracker")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_eyetracker)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_info = QFrame(self.tab_eyetracker)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setMinimumSize(QSize(400, 400))
        self.frame_info.setMaximumSize(QSize(400, 450))
        self.frame_info.setFrameShape(QFrame.Box)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_info)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.eyetracker_info = QPlainTextEdit(self.frame_info)
        self.eyetracker_info.setObjectName(u"eyetracker_info")
        self.eyetracker_info.setEnabled(False)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.eyetracker_info.setFont(font2)
        self.eyetracker_info.setFrameShape(QFrame.Panel)
        self.eyetracker_info.setFrameShadow(QFrame.Plain)

        self.verticalLayout_3.addWidget(self.eyetracker_info)

        self.vSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_3.addItem(self.vSpacer)

        self.btn_start_eyetracker = QPushButton(self.frame_info)
        self.btn_start_eyetracker.setObjectName(u"btn_start_eyetracker")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(16)
        font3.setBold(False)
        self.btn_start_eyetracker.setFont(font3)

        self.verticalLayout_3.addWidget(self.btn_start_eyetracker)


        self.horizontalLayout_3.addWidget(self.frame_info)

        self.frame_state = QFrame(self.tab_eyetracker)
        self.frame_state.setObjectName(u"frame_state")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_state.sizePolicy().hasHeightForWidth())
        self.frame_state.setSizePolicy(sizePolicy)
        self.frame_state.setMinimumSize(QSize(400, 450))
        self.frame_state.setMaximumSize(QSize(400, 450))
        self.frame_state.setFrameShape(QFrame.Box)
        self.frame_state.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_state)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gLayout_eyepos = QGridLayout()
        self.gLayout_eyepos.setObjectName(u"gLayout_eyepos")
        self.pgb_h = QProgressBar(self.frame_state)
        self.pgb_h.setObjectName(u"pgb_h")
        self.pgb_h.setValue(50)
        self.pgb_h.setAlignment(Qt.AlignCenter)
        self.pgb_h.setInvertedAppearance(False)
        self.pgb_h.setTextDirection(QProgressBar.TopToBottom)

        self.gLayout_eyepos.addWidget(self.pgb_h, 1, 0, 1, 1)

        self.hSpacer = QSpacerItem(25, 25, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gLayout_eyepos.addItem(self.hSpacer, 1, 1, 1, 1)

        self.widget_eyepos = QWidget(self.frame_state)
        self.widget_eyepos.setObjectName(u"widget_eyepos")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(6)
        sizePolicy1.setVerticalStretch(6)
        sizePolicy1.setHeightForWidth(self.widget_eyepos.sizePolicy().hasHeightForWidth())
        self.widget_eyepos.setSizePolicy(sizePolicy1)

        self.gLayout_eyepos.addWidget(self.widget_eyepos, 0, 0, 1, 1)

        self.pgb_v = QProgressBar(self.frame_state)
        self.pgb_v.setObjectName(u"pgb_v")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pgb_v.sizePolicy().hasHeightForWidth())
        self.pgb_v.setSizePolicy(sizePolicy2)
        self.pgb_v.setMinimum(45)
        self.pgb_v.setMaximum(75)
        self.pgb_v.setValue(60)
        self.pgb_v.setOrientation(Qt.Vertical)

        self.gLayout_eyepos.addWidget(self.pgb_v, 0, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gLayout_eyepos)

        self.verticalSpacer_2 = QSpacerItem(17, 37, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.btn_calibration = QPushButton(self.frame_state)
        self.btn_calibration.setObjectName(u"btn_calibration")
        self.btn_calibration.setFont(font3)

        self.verticalLayout_4.addWidget(self.btn_calibration)


        self.horizontalLayout_3.addWidget(self.frame_state)

        self.tabWidget_prepare.addTab(self.tab_eyetracker, "")
        self.tab_db = QWidget()
        self.tab_db.setObjectName(u"tab_db")
        self.verticalLayout_5 = QVBoxLayout(self.tab_db)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_imgdb = QGroupBox(self.tab_db)
        self.groupBox_imgdb.setObjectName(u"groupBox_imgdb")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.groupBox_imgdb.sizePolicy().hasHeightForWidth())
        self.groupBox_imgdb.setSizePolicy(sizePolicy3)
        self.groupBox_imgdb.setMinimumSize(QSize(300, 100))
        self.groupBox_imgdb.setMaximumSize(QSize(4000, 150))
        font4 = QFont()
        font4.setFamilies([u"\u9ed1\u4f53"])
        font4.setBold(False)
        font4.setItalic(False)
        self.groupBox_imgdb.setFont(font4)
        self.groupBox_imgdb.setToolTipDuration(-1)
        self.groupBox_imgdb.setStyleSheet(u"QGroupBox {\n"
"    font: 20px \"\u9ed1\u4f53\";\n"
"	background-color: rgb(240, 240, 240);\n"
"    border-radius:6px;\n"
"    margin-top:12px;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(255, 0, 0);\n"
"}\n"
"QGroupBox:title {\n"
"    color:rgb(28, 120, 167);\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_imgdb)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.hLayout_dir_select = QHBoxLayout()
        self.hLayout_dir_select.setObjectName(u"hLayout_dir_select")
        self.label = QLabel(self.groupBox_imgdb)
        self.label.setObjectName(u"label")
        font5 = QFont()
        font5.setPointSize(14)
        self.label.setFont(font5)

        self.hLayout_dir_select.addWidget(self.label)

        self.lineEdit = QLineEdit(self.groupBox_imgdb)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(7)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy4)

        self.hLayout_dir_select.addWidget(self.lineEdit)

        self.btnDirget = QPushButton(self.groupBox_imgdb)
        self.btnDirget.setObjectName(u"btnDirget")
        self.btnDirget.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btnDirget.sizePolicy().hasHeightForWidth())
        self.btnDirget.setSizePolicy(sizePolicy5)
        self.btnDirget.setMinimumSize(QSize(40, 25))
        self.btnDirget.setMaximumSize(QSize(1000, 30))
        font6 = QFont()
        font6.setPointSize(10)
        self.btnDirget.setFont(font6)

        self.hLayout_dir_select.addWidget(self.btnDirget)

        self.hLayout_dir_select.setStretch(0, 2)
        self.hLayout_dir_select.setStretch(1, 8)
        self.hLayout_dir_select.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.hLayout_dir_select)

        self.hLayout_dir_apply = QHBoxLayout()
        self.hLayout_dir_apply.setObjectName(u"hLayout_dir_apply")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hLayout_dir_apply.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnApply = QPushButton(self.groupBox_imgdb)
        self.btnApply.setObjectName(u"btnApply")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.btnApply.sizePolicy().hasHeightForWidth())
        self.btnApply.setSizePolicy(sizePolicy6)
        font7 = QFont()
        font7.setPointSize(12)
        self.btnApply.setFont(font7)

        self.horizontalLayout_2.addWidget(self.btnApply)


        self.hLayout_dir_apply.addLayout(self.horizontalLayout_2)

        self.hLayout_dir_apply.setStretch(0, 10)
        self.hLayout_dir_apply.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.hLayout_dir_apply)


        self.verticalLayout_5.addWidget(self.groupBox_imgdb)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.tabWidget_prepare.addTab(self.tab_db, "")

        self.verticalLayout.addWidget(self.tabWidget_prepare)

        self.hLayout_start = QHBoxLayout()
        self.hLayout_start.setObjectName(u"hLayout_start")
        self.hSpacer_left = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hLayout_start.addItem(self.hSpacer_left)

        self.btn_start = QPushButton(self.centralwidget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy6)
        self.btn_start.setMinimumSize(QSize(150, 35))
        self.btn_start.setMaximumSize(QSize(301, 40))
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        font8.setPointSize(16)
        font8.setBold(True)
        font8.setUnderline(False)
        font8.setStyleStrategy(QFont.PreferAntialias)
        self.btn_start.setFont(font8)
        self.btn_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start.setAutoFillBackground(False)

        self.hLayout_start.addWidget(self.btn_start)

        self.hSpacer_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hLayout_start.addItem(self.hSpacer_right)


        self.verticalLayout.addLayout(self.hLayout_start)

        start_panel.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(start_panel)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 846, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        start_panel.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(start_panel)
        self.statusbar.setObjectName(u"statusbar")
        start_panel.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_frequency)

        self.retranslateUi(start_panel)

        self.tabWidget_prepare.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(start_panel)
    # setupUi

    def retranslateUi(self, start_panel):
        start_panel.setWindowTitle(QCoreApplication.translate("start_panel", u"MainWindow", None))
        self.action_frequency.setText(QCoreApplication.translate("start_panel", u"\u8bbe\u7f6e\u91c7\u6837\u9891\u7387", None))
        self.action_filter.setText(QCoreApplication.translate("start_panel", u"\u8bbe\u7f6e\u6ee4\u6ce2\u5668", None))
        self.btn_start_eyetracker.setText(QCoreApplication.translate("start_panel", u"\u542f\u52a8\u773c\u52a8\u4eea", None))
        self.pgb_h.setFormat(QCoreApplication.translate("start_panel", u"%p", None))
        self.btn_calibration.setText(QCoreApplication.translate("start_panel", u"\u5f00\u59cb\u77eb\u6b63", None))
        self.tabWidget_prepare.setTabText(self.tabWidget_prepare.indexOf(self.tab_eyetracker), QCoreApplication.translate("start_panel", u"\u773c\u52a8\u4eea", None))
        self.groupBox_imgdb.setTitle(QCoreApplication.translate("start_panel", u"\u6570\u636e\u5e93", None))
        self.label.setText(QCoreApplication.translate("start_panel", u"\u6570\u636e\u5e93\u5730\u5740\uff1a", None))
        self.btnDirget.setText(QCoreApplication.translate("start_panel", u"...", None))
        self.btnApply.setText(QCoreApplication.translate("start_panel", u"\u5e94\u7528", None))
        self.tabWidget_prepare.setTabText(self.tabWidget_prepare.indexOf(self.tab_db), QCoreApplication.translate("start_panel", u"\u4e3b\u89c2\u5b9e\u9a8c", None))
        self.btn_start.setText(QCoreApplication.translate("start_panel", u"\u5f00\u59cb\u5b9e\u9a8c", None))
        self.menu.setTitle(QCoreApplication.translate("start_panel", u"\u8bbe\u7f6e", None))
    # retranslateUi
