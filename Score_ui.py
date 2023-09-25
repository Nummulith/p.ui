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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

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

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame0)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.PartsListAdd = QPushButton(self.frame0)
        self.PartsListAdd.setObjectName(u"PartsListAdd")
        self.PartsListAdd.setMaximumSize(QSize(26, 32))

        self.horizontalLayout.addWidget(self.PartsListAdd)

        self.PartsListDel = QPushButton(self.frame0)
        self.PartsListDel.setObjectName(u"PartsListDel")
        self.PartsListDel.setMaximumSize(QSize(26, 32))

        self.horizontalLayout.addWidget(self.PartsListDel)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

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

        self.bRun = QPushButton(self.frame0)
        self.bRun.setObjectName(u"bRun")

        self.verticalLayout_4.addWidget(self.bRun)


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

        self.Part_Name = QLineEdit(self.frame1)
        self.Part_Name.setObjectName(u"Part_Name")

        self.verticalLayout_3.addWidget(self.Part_Name)

        self.Part_Role = QTabWidget(self.frame1)
        self.Part_Role.setObjectName(u"Part_Role")
        self.Part_Role.setMaximumSize(QSize(1000, 150))
        self.Part_Role_Main = QWidget()
        self.Part_Role_Main.setObjectName(u"Part_Role_Main")
        self.verticalLayout_11 = QVBoxLayout(self.Part_Role_Main)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_24 = QLabel(self.Part_Role_Main)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_11.addWidget(self.label_24)

        self.Part_Pitch = QSpinBox(self.Part_Role_Main)
        self.Part_Pitch.setObjectName(u"Part_Pitch")

        self.verticalLayout_11.addWidget(self.Part_Pitch)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_6)

        self.Part_Role.addTab(self.Part_Role_Main, "")
        self.Part_Role_Function = QWidget()
        self.Part_Role_Function.setObjectName(u"Part_Role_Function")
        self.verticalLayout_12 = QVBoxLayout(self.Part_Role_Function)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_25 = QLabel(self.Part_Role_Function)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_12.addWidget(self.label_25)

        self.Part_Transpose = QSpinBox(self.Part_Role_Function)
        self.Part_Transpose.setObjectName(u"Part_Transpose")

        self.verticalLayout_12.addWidget(self.Part_Transpose)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_7)

        self.Part_Role.addTab(self.Part_Role_Function, "")
        self.Part_Role_None = QWidget()
        self.Part_Role_None.setObjectName(u"Part_Role_None")
        self.Part_Role.addTab(self.Part_Role_None, "")

        self.verticalLayout_3.addWidget(self.Part_Role)

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

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_26 = QLabel(self.frame1)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_6.addWidget(self.label_26)

        self.Part_BuildFxl = QCheckBox(self.frame1)
        self.Part_BuildFxl.setObjectName(u"Part_BuildFxl")

        self.horizontalLayout_6.addWidget(self.Part_BuildFxl)

        self.Part_BuildPos = QCheckBox(self.frame1)
        self.Part_BuildPos.setObjectName(u"Part_BuildPos")

        self.horizontalLayout_6.addWidget(self.Part_BuildPos)

        self.Part_BuildPow = QCheckBox(self.frame1)
        self.Part_BuildPow.setObjectName(u"Part_BuildPow")

        self.horizontalLayout_6.addWidget(self.Part_BuildPow)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_11 = QLabel(self.frame1)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_4.addWidget(self.label_11)

        self.StavesListAdd = QPushButton(self.frame1)
        self.StavesListAdd.setObjectName(u"StavesListAdd")
        self.StavesListAdd.setMaximumSize(QSize(26, 32))

        self.horizontalLayout_4.addWidget(self.StavesListAdd)

        self.StavesListDel = QPushButton(self.frame1)
        self.StavesListDel.setObjectName(u"StavesListDel")
        self.StavesListDel.setMaximumSize(QSize(26, 32))

        self.horizontalLayout_4.addWidget(self.StavesListDel)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.StavesList = QListWidget(self.frame1)
        self.StavesList.setObjectName(u"StavesList")

        self.verticalLayout_3.addWidget(self.StavesList)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.frame1)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.InstrsListAdd = QPushButton(self.frame1)
        self.InstrsListAdd.setObjectName(u"InstrsListAdd")
        self.InstrsListAdd.setMaximumSize(QSize(26, 32))

        self.horizontalLayout_7.addWidget(self.InstrsListAdd)

        self.InstrsListDel = QPushButton(self.frame1)
        self.InstrsListDel.setObjectName(u"InstrsListDel")
        self.InstrsListDel.setMaximumSize(QSize(26, 32))

        self.horizontalLayout_7.addWidget(self.InstrsListDel)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.InstrsList = QListWidget(self.frame1)
        self.InstrsList.setObjectName(u"InstrsList")

        self.verticalLayout_3.addWidget(self.InstrsList)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.frame1)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.BuildsListAdd = QPushButton(self.frame1)
        self.BuildsListAdd.setObjectName(u"BuildsListAdd")
        self.BuildsListAdd.setMaximumSize(QSize(26, 32))

        self.horizontalLayout_8.addWidget(self.BuildsListAdd)

        self.BuildsListDel = QPushButton(self.frame1)
        self.BuildsListDel.setObjectName(u"BuildsListDel")
        self.BuildsListDel.setMaximumSize(QSize(26, 32))

        self.horizontalLayout_8.addWidget(self.BuildsListDel)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.BuildsList = QListWidget(self.frame1)
        self.BuildsList.setObjectName(u"BuildsList")

        self.verticalLayout_3.addWidget(self.BuildsList)


        self.PanelsLayout.addWidget(self.frame1)

        self.frame5 = QFrame(self.PanelsLayout_2)
        self.frame5.setObjectName(u"frame5")
        sizePolicy.setHeightForWidth(self.frame5.sizePolicy().hasHeightForWidth())
        self.frame5.setSizePolicy(sizePolicy)
        self.frame5.setFrameShape(QFrame.StyledPanel)
        self.frame5.setFrameShadow(QFrame.Plain)
        self.verticalLayout_13 = QVBoxLayout(self.frame5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_13 = QLabel(self.frame5)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_13.addWidget(self.label_13)

        self.Instr_Name = QLineEdit(self.frame5)
        self.Instr_Name.setObjectName(u"Instr_Name")

        self.verticalLayout_13.addWidget(self.Instr_Name)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_8)


        self.PanelsLayout.addWidget(self.frame5)

        self.frame6 = QFrame(self.PanelsLayout_2)
        self.frame6.setObjectName(u"frame6")
        sizePolicy.setHeightForWidth(self.frame6.sizePolicy().hasHeightForWidth())
        self.frame6.setSizePolicy(sizePolicy)
        self.frame6.setFrameShape(QFrame.StyledPanel)
        self.frame6.setFrameShadow(QFrame.Plain)
        self.verticalLayout_14 = QVBoxLayout(self.frame6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_15 = QLabel(self.frame6)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_14.addWidget(self.label_15)

        self.Build_Name = QLineEdit(self.frame6)
        self.Build_Name.setObjectName(u"Build_Name")

        self.verticalLayout_14.addWidget(self.Build_Name)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_9)


        self.PanelsLayout.addWidget(self.frame6)

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

        self.Stave_Type = QTabWidget(self.frame2)
        self.Stave_Type.setObjectName(u"Stave_Type")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Stave_Type.sizePolicy().hasHeightForWidth())
        self.Stave_Type.setSizePolicy(sizePolicy2)
        self.Stave_Type.setMaximumSize(QSize(6000, 200))
        self.Stave_Type.setBaseSize(QSize(0, 0))
        self.Stave_Type_Module = QWidget()
        self.Stave_Type_Module.setObjectName(u"Stave_Type_Module")
        self.verticalLayout_7 = QVBoxLayout(self.Stave_Type_Module)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_19 = QLabel(self.Stave_Type_Module)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_7.addWidget(self.label_19)

        self.Stave_Module = QLineEdit(self.Stave_Type_Module)
        self.Stave_Module.setObjectName(u"Stave_Module")

        self.verticalLayout_7.addWidget(self.Stave_Module)

        self.Stave_ZeroLength = QCheckBox(self.Stave_Type_Module)
        self.Stave_ZeroLength.setObjectName(u"Stave_ZeroLength")

        self.verticalLayout_7.addWidget(self.Stave_ZeroLength)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.Stave_Type.addTab(self.Stave_Type_Module, "")
        self.Stave_Type_Sequence = QWidget()
        self.Stave_Type_Sequence.setObjectName(u"Stave_Type_Sequence")
        self.verticalLayout_8 = QVBoxLayout(self.Stave_Type_Sequence)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_20 = QLabel(self.Stave_Type_Sequence)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_8.addWidget(self.label_20)

        self.Stave_Sequence = QLineEdit(self.Stave_Type_Sequence)
        self.Stave_Sequence.setObjectName(u"Stave_Sequence")

        self.verticalLayout_8.addWidget(self.Stave_Sequence)

        self.label_21 = QLabel(self.Stave_Type_Sequence)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_8.addWidget(self.label_21)

        self.Stave_Parameter = QLineEdit(self.Stave_Type_Sequence)
        self.Stave_Parameter.setObjectName(u"Stave_Parameter")

        self.verticalLayout_8.addWidget(self.Stave_Parameter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.Stave_Type.addTab(self.Stave_Type_Sequence, "")
        self.Stave_Type_Sample = QWidget()
        self.Stave_Type_Sample.setObjectName(u"Stave_Type_Sample")
        self.verticalLayout_9 = QVBoxLayout(self.Stave_Type_Sample)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_22 = QLabel(self.Stave_Type_Sample)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_9.addWidget(self.label_22)

        self.Stave_Sample = QLineEdit(self.Stave_Type_Sample)
        self.Stave_Sample.setObjectName(u"Stave_Sample")

        self.verticalLayout_9.addWidget(self.Stave_Sample)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_4)

        self.Stave_Type.addTab(self.Stave_Type_Sample, "")
        self.Stave_Type_Expression = QWidget()
        self.Stave_Type_Expression.setObjectName(u"Stave_Type_Expression")
        self.verticalLayout_10 = QVBoxLayout(self.Stave_Type_Expression)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_23 = QLabel(self.Stave_Type_Expression)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_10.addWidget(self.label_23)

        self.Stave_Expression = QLineEdit(self.Stave_Type_Expression)
        self.Stave_Expression.setObjectName(u"Stave_Expression")

        self.verticalLayout_10.addWidget(self.Stave_Expression)

        self.verticalSpacer_5 = QSpacerItem(20, 101, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_5)

        self.Stave_Type.addTab(self.Stave_Type_Expression, "")

        self.verticalLayout_6.addWidget(self.Stave_Type)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_12 = QLabel(self.frame2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_5.addWidget(self.label_12)

        self.NotesListAdd = QPushButton(self.frame2)
        self.NotesListAdd.setObjectName(u"NotesListAdd")
        self.NotesListAdd.setMaximumSize(QSize(26, 32))

        self.horizontalLayout_5.addWidget(self.NotesListAdd)

        self.NotesListDel = QPushButton(self.frame2)
        self.NotesListDel.setObjectName(u"NotesListDel")
        self.NotesListDel.setMaximumSize(QSize(26, 32))

        self.horizontalLayout_5.addWidget(self.NotesListDel)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.NotesList = QListWidget(self.frame2)
        self.NotesList.setObjectName(u"NotesList")

        self.verticalLayout_6.addWidget(self.NotesList)


        self.PanelsLayout.addWidget(self.frame2)

        self.frame4 = QFrame(self.PanelsLayout_2)
        self.frame4.setObjectName(u"frame4")
        sizePolicy.setHeightForWidth(self.frame4.sizePolicy().hasHeightForWidth())
        self.frame4.setSizePolicy(sizePolicy)
        self.frame4.setFrameShape(QFrame.StyledPanel)
        self.frame4.setFrameShadow(QFrame.Plain)
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

        self.Part_Role.setCurrentIndex(1)
        self.Stave_Type.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(pApp)
    # setupUi

    def retranslateUi(self, pApp):
        pApp.setWindowTitle(QCoreApplication.translate("pApp", u"p", None))
        self.label_7.setText(QCoreApplication.translate("pApp", u"Score", None))
        self.label_10.setText(QCoreApplication.translate("pApp", u"Duration", None))
        self.label.setText(QCoreApplication.translate("pApp", u"Partitures", None))
        self.PartsListAdd.setText(QCoreApplication.translate("pApp", u"+", None))
        self.PartsListDel.setText(QCoreApplication.translate("pApp", u"-", None))
        self.bScoreLoad.setText(QCoreApplication.translate("pApp", u"Load", None))
        self.bScoreSave.setText(QCoreApplication.translate("pApp", u"Save", None))
        self.bRun.setText(QCoreApplication.translate("pApp", u"Run", None))
        self.label_2.setText(QCoreApplication.translate("pApp", u"Partiture", None))
        self.label_24.setText(QCoreApplication.translate("pApp", u"Pitch", None))
        self.Part_Role.setTabText(self.Part_Role.indexOf(self.Part_Role_Main), QCoreApplication.translate("pApp", u"Main", None))
        self.label_25.setText(QCoreApplication.translate("pApp", u"Transpose", None))
        self.Part_Role.setTabText(self.Part_Role.indexOf(self.Part_Role_Function), QCoreApplication.translate("pApp", u"Function", None))
        self.Part_Role.setTabText(self.Part_Role.indexOf(self.Part_Role_None), QCoreApplication.translate("pApp", u"None", None))
        self.label_3.setText(QCoreApplication.translate("pApp", u"Numerator", None))
        self.label_9.setText(QCoreApplication.translate("pApp", u"Denominator", None))
        self.label_26.setText(QCoreApplication.translate("pApp", u"Build fpp", None))
        self.Part_BuildFxl.setText("")
        self.Part_BuildPos.setText("")
        self.Part_BuildPow.setText("")
        self.label_11.setText(QCoreApplication.translate("pApp", u"Staves", None))
        self.StavesListAdd.setText(QCoreApplication.translate("pApp", u"+", None))
        self.StavesListDel.setText(QCoreApplication.translate("pApp", u"-", None))
        self.label_6.setText(QCoreApplication.translate("pApp", u"Instruments", None))
        self.InstrsListAdd.setText(QCoreApplication.translate("pApp", u"+", None))
        self.InstrsListDel.setText(QCoreApplication.translate("pApp", u"-", None))
        self.label_8.setText(QCoreApplication.translate("pApp", u"Builds", None))
        self.BuildsListAdd.setText(QCoreApplication.translate("pApp", u"+", None))
        self.BuildsListDel.setText(QCoreApplication.translate("pApp", u"-", None))
        self.label_13.setText(QCoreApplication.translate("pApp", u"Instrument", None))
        self.label_15.setText(QCoreApplication.translate("pApp", u"Build", None))
        self.label_4.setText(QCoreApplication.translate("pApp", u"Stave", None))
        self.label_16.setText(QCoreApplication.translate("pApp", u"Build", None))
        self.label_17.setText(QCoreApplication.translate("pApp", u"Condition", None))
        self.label_19.setText(QCoreApplication.translate("pApp", u"File", None))
        self.Stave_ZeroLength.setText(QCoreApplication.translate("pApp", u"Zero Length", None))
        self.Stave_Type.setTabText(self.Stave_Type.indexOf(self.Stave_Type_Module), QCoreApplication.translate("pApp", u"Module", None))
        self.label_20.setText(QCoreApplication.translate("pApp", u"Sequence", None))
        self.label_21.setText(QCoreApplication.translate("pApp", u"Parameter", None))
        self.Stave_Type.setTabText(self.Stave_Type.indexOf(self.Stave_Type_Sequence), QCoreApplication.translate("pApp", u"Sequence", None))
        self.label_22.setText(QCoreApplication.translate("pApp", u"Sample", None))
        self.Stave_Type.setTabText(self.Stave_Type.indexOf(self.Stave_Type_Sample), QCoreApplication.translate("pApp", u"Sample", None))
        self.label_23.setText(QCoreApplication.translate("pApp", u"Expression", None))
        self.Stave_Type.setTabText(self.Stave_Type.indexOf(self.Stave_Type_Expression), QCoreApplication.translate("pApp", u"Expression", None))
        self.label_12.setText(QCoreApplication.translate("pApp", u"Notes", None))
        self.NotesListAdd.setText(QCoreApplication.translate("pApp", u"+", None))
        self.NotesListDel.setText(QCoreApplication.translate("pApp", u"-", None))
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
        self.label_14.setText(QCoreApplication.translate("pApp", u"Fxl, Pos, Pow", None))
    # retranslateUi

