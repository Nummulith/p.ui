# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Score.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_pApp(object):
    def setupUi(self, pApp):
        if not pApp.objectName():
            pApp.setObjectName(u"pApp")
        pApp.resize(1250, 943)
        self.centralwidget = QWidget(pApp)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ButtonsLayout_2 = QFrame(self.centralwidget)
        self.ButtonsLayout_2.setObjectName(u"ButtonsLayout_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ButtonsLayout_2.sizePolicy().hasHeightForWidth())
        self.ButtonsLayout_2.setSizePolicy(sizePolicy1)
        self.ButtonsLayout = QHBoxLayout(self.ButtonsLayout_2)
        self.ButtonsLayout.setObjectName(u"ButtonsLayout")

        self.verticalLayout.addWidget(self.ButtonsLayout_2)

        self.PanelsLayout_2 = QFrame(self.centralwidget)
        self.PanelsLayout_2.setObjectName(u"PanelsLayout_2")
        sizePolicy.setHeightForWidth(self.PanelsLayout_2.sizePolicy().hasHeightForWidth())
        self.PanelsLayout_2.setSizePolicy(sizePolicy)
        self.PanelsLayout = QHBoxLayout(self.PanelsLayout_2)
        self.PanelsLayout.setObjectName(u"PanelsLayout")
        self.frame0 = QFrame(self.PanelsLayout_2)
        self.frame0.setObjectName(u"frame0")
        sizePolicy1.setHeightForWidth(self.frame0.sizePolicy().hasHeightForWidth())
        self.frame0.setSizePolicy(sizePolicy1)
        self.frame0.setFrameShape(QFrame.StyledPanel)
        self.verticalLayout_4 = QVBoxLayout(self.frame0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_7 = QLabel(self.frame0)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.label_6 = QLabel(self.frame0)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_4.addWidget(self.label_6)

        self.Score_Name = QLineEdit(self.frame0)
        self.Score_Name.setObjectName(u"Score_Name")

        self.verticalLayout_4.addWidget(self.Score_Name)

        self.label_10 = QLabel(self.frame0)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_4.addWidget(self.label_10)

        self.Score_Duration = QSpinBox(self.frame0)
        self.Score_Duration.setObjectName(u"Score_Duration")
        self.Score_Duration.setMaximum(999999)

        self.verticalLayout_4.addWidget(self.Score_Duration)

        self.label = QLabel(self.frame0)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.PartsList = QListWidget(self.frame0)
        self.PartsList.setObjectName(u"PartsList")

        self.verticalLayout_4.addWidget(self.PartsList)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.bScoreLoad = QPushButton(self.frame0)
        self.bScoreLoad.setObjectName(u"bScoreLoad")

        self.horizontalLayout_2.addWidget(self.bScoreLoad)

        self.bScoreSave = QPushButton(self.frame0)
        self.bScoreSave.setObjectName(u"bScoreSave")

        self.horizontalLayout_2.addWidget(self.bScoreSave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.PanelsLayout.addWidget(self.frame0)

        self.frame1 = QFrame(self.PanelsLayout_2)
        self.frame1.setObjectName(u"frame1")
        sizePolicy.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy)
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.verticalLayout_3 = QVBoxLayout(self.frame1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_8 = QLabel(self.frame1)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_3.addWidget(self.label_8)

        self.Part_Name = QLineEdit(self.frame1)
        self.Part_Name.setObjectName(u"Part_Name")

        self.verticalLayout_3.addWidget(self.Part_Name)

        self.label_3 = QLabel(self.frame1)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.Part_Numerator = QSpinBox(self.frame1)
        self.Part_Numerator.setObjectName(u"Part_Numerator")

        self.verticalLayout_3.addWidget(self.Part_Numerator)

        self.label_9 = QLabel(self.frame1)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_3.addWidget(self.label_9)

        self.Part_Denominator = QSpinBox(self.frame1)
        self.Part_Denominator.setObjectName(u"Part_Denominator")

        self.verticalLayout_3.addWidget(self.Part_Denominator)

        self.label_11 = QLabel(self.frame1)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_3.addWidget(self.label_11)

        self.StavesList = QListWidget(self.frame1)
        self.StavesList.setObjectName(u"StavesList")

        self.verticalLayout_3.addWidget(self.StavesList)


        self.PanelsLayout.addWidget(self.frame1)

        self.frame2 = QFrame(self.PanelsLayout_2)
        self.frame2.setObjectName(u"frame2")
        sizePolicy.setHeightForWidth(self.frame2.sizePolicy().hasHeightForWidth())
        self.frame2.setSizePolicy(sizePolicy)
        self.frame2.setFrameShape(QFrame.StyledPanel)
        self.verticalLayout_6 = QVBoxLayout(self.frame2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.frame2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)

        self.label_15 = QLabel(self.frame2)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_6.addWidget(self.label_15)

        self.Stave_Name = QLineEdit(self.frame2)
        self.Stave_Name.setObjectName(u"Stave_Name")

        self.verticalLayout_6.addWidget(self.Stave_Name)

        self.label_16 = QLabel(self.frame2)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_6.addWidget(self.label_16)

        self.Stave_Build = QLineEdit(self.frame2)
        self.Stave_Build.setObjectName(u"Stave_Build")

        self.verticalLayout_6.addWidget(self.Stave_Build)

        self.label_17 = QLabel(self.frame2)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_6.addWidget(self.label_17)

        self.Stave_Condition = QLineEdit(self.frame2)
        self.Stave_Condition.setObjectName(u"Stave_Condition")

        self.verticalLayout_6.addWidget(self.Stave_Condition)

        self.label_12 = QLabel(self.frame2)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_6.addWidget(self.label_12)

        self.NotesList = QListWidget(self.frame2)
        self.NotesList.setObjectName(u"NotesList")

        self.verticalLayout_6.addWidget(self.NotesList)


        self.PanelsLayout.addWidget(self.frame2)

        self.frame4 = QFrame(self.PanelsLayout_2)
        self.frame4.setObjectName(u"frame4")
        sizePolicy.setHeightForWidth(self.frame4.sizePolicy().hasHeightForWidth())
        self.frame4.setSizePolicy(sizePolicy)
        self.frame4.setFrameShape(QFrame.StyledPanel)
        self.verticalLayout_5 = QVBoxLayout(self.frame4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_18 = QLabel(self.frame4)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_5.addWidget(self.label_18)

        self.StavesTable = QTableWidget(self.frame4)
        if (self.StavesTable.columnCount() < 2):
            self.StavesTable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.StavesTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.StavesTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.StavesTable.rowCount() < 1):
            self.StavesTable.setRowCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.StavesTable.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.StavesTable.setItem(0, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.StavesTable.setItem(0, 1, __qtablewidgetitem4)
        self.StavesTable.setObjectName(u"StavesTable")
        self.StavesTable.setStyleSheet(u"QHeaderView::section {\n"
"	/* \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0438 */\n"
"	background-color: rgb(230, 255, 255);\n"
"	text-align: center;\n"
"	padding: 0px;\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"QTableWidget::item {\n"
"	/* \u042f\u0447\u0435\u0439\u043a\u0438 */\n"
"	padding: 0px;\n"
"	color: rgb(0, 0, 255);\n"
"	text-align: center;\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.StavesTable)


        self.PanelsLayout.addWidget(self.frame4)

        self.frame3 = QFrame(self.PanelsLayout_2)
        self.frame3.setObjectName(u"frame3")
        sizePolicy.setHeightForWidth(self.frame3.sizePolicy().hasHeightForWidth())
        self.frame3.setSizePolicy(sizePolicy)
        self.frame3.setFrameShape(QFrame.StyledPanel)
        self.verticalLayout_2 = QVBoxLayout(self.frame3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.frame3)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_13 = QLabel(self.frame3)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_2.addWidget(self.label_13)

        self.Note_Column = QSpinBox(self.frame3)
        self.Note_Column.setObjectName(u"Note_Column")

        self.verticalLayout_2.addWidget(self.Note_Column)

        self.label_14 = QLabel(self.frame3)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_2.addWidget(self.label_14)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Note_Fxl = QLineEdit(self.frame3)
        self.Note_Fxl.setObjectName(u"Note_Fxl")
        self.Note_Fxl.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_3.addWidget(self.Note_Fxl)

        self.Note_Pos = QLineEdit(self.frame3)
        self.Note_Pos.setObjectName(u"Note_Pos")
        self.Note_Pos.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_3.addWidget(self.Note_Pos)

        self.Note_Pow = QLineEdit(self.frame3)
        self.Note_Pow.setObjectName(u"Note_Pow")
        self.Note_Pow.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_3.addWidget(self.Note_Pow)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.PanelsLayout.addWidget(self.frame3)


        self.verticalLayout.addWidget(self.PanelsLayout_2)

        pApp.setCentralWidget(self.centralwidget)

        self.retranslateUi(pApp)

        QMetaObject.connectSlotsByName(pApp)
    # setupUi

    def retranslateUi(self, pApp):
        pApp.setWindowTitle(QCoreApplication.translate("pApp", u"p", None))
        self.label_7.setText(QCoreApplication.translate("pApp", u"Score", None))
        self.label_6.setText(QCoreApplication.translate("pApp", u"Name", None))
        self.label_10.setText(QCoreApplication.translate("pApp", u"Duration", None))
        self.label.setText(QCoreApplication.translate("pApp", u"Parts", None))
        self.bScoreLoad.setText(QCoreApplication.translate("pApp", u"Load", None))
        self.bScoreSave.setText(QCoreApplication.translate("pApp", u"Save", None))
        self.label_2.setText(QCoreApplication.translate("pApp", u"Partiture", None))
        self.label_8.setText(QCoreApplication.translate("pApp", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("pApp", u"Numerator", None))
        self.label_9.setText(QCoreApplication.translate("pApp", u"Denominator", None))
        self.label_11.setText(QCoreApplication.translate("pApp", u"Staves", None))
        self.label_4.setText(QCoreApplication.translate("pApp", u"Stave", None))
        self.label_15.setText(QCoreApplication.translate("pApp", u"Name", None))
        self.label_16.setText(QCoreApplication.translate("pApp", u"Build", None))
        self.label_17.setText(QCoreApplication.translate("pApp", u"Condition", None))
        self.label_12.setText(QCoreApplication.translate("pApp", u"Notes", None))
        self.label_18.setText(QCoreApplication.translate("pApp", u"Matrix", None))
        ___qtablewidgetitem = self.StavesTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("pApp", u"0", None));
        ___qtablewidgetitem1 = self.StavesTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("pApp", u"1", None));
        ___qtablewidgetitem2 = self.StavesTable.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("pApp", u"Str01", None));

        __sortingEnabled = self.StavesTable.isSortingEnabled()
        self.StavesTable.setSortingEnabled(False)
        ___qtablewidgetitem3 = self.StavesTable.item(0, 0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("pApp", u"1212", None));
        ___qtablewidgetitem4 = self.StavesTable.item(0, 1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("pApp", u"matrix", None));
        self.StavesTable.setSortingEnabled(__sortingEnabled)

        self.label_5.setText(QCoreApplication.translate("pApp", u"Note", None))
        self.label_13.setText(QCoreApplication.translate("pApp", u"Column", None))
        self.label_14.setText(QCoreApplication.translate("pApp", u"Fxl, Pos, Pow", None))
    # retranslateUi

