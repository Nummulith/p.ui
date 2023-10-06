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
        pApp.resize(1568, 808)
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
        sizePolicy.setHeightForWidth(self.frame0.sizePolicy().hasHeightForWidth())
        self.frame0.setSizePolicy(sizePolicy)
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

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_10)


        self.PanelsLayout.addWidget(self.frame0)

        self.frame1 = QFrame(self.PanelsLayout_2)
        self.frame1.setObjectName(u"frame1")
        sizePolicy.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy)
        self.frame1.setMinimumSize(QSize(280, 0))
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.verticalLayout_3 = QVBoxLayout(self.frame1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.PartsList = QListWidget(self.frame1)
        self.PartsList.setObjectName(u"PartsList")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.PartsList.sizePolicy().hasHeightForWidth())
        self.PartsList.setSizePolicy(sizePolicy2)
        self.PartsList.setMinimumSize(QSize(0, 200))

        self.horizontalLayout_10.addWidget(self.PartsList)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.PartsListAdd = QPushButton(self.frame1)
        self.PartsListAdd.setObjectName(u"PartsListAdd")
        self.PartsListAdd.setMaximumSize(QSize(26, 32))

        self.verticalLayout_15.addWidget(self.PartsListAdd)

        self.PartsListDel = QPushButton(self.frame1)
        self.PartsListDel.setObjectName(u"PartsListDel")
        self.PartsListDel.setMaximumSize(QSize(26, 32))

        self.verticalLayout_15.addWidget(self.PartsListDel)


        self.horizontalLayout_10.addLayout(self.verticalLayout_15)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.Part_Name = QLineEdit(self.frame1)
        self.Part_Name.setObjectName(u"Part_Name")

        self.verticalLayout_3.addWidget(self.Part_Name)

        self.Part_ZeroLength = QCheckBox(self.frame1)
        self.Part_ZeroLength.setObjectName(u"Part_ZeroLength")

        self.verticalLayout_3.addWidget(self.Part_ZeroLength)

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

        self.label_9 = QLabel(self.frame1)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_3.addWidget(self.label_9)

        self.Part_ColumnWidth = QTabWidget(self.frame1)
        self.Part_ColumnWidth.setObjectName(u"Part_ColumnWidth")
        self.Part_ColumnWidth_Fixed = QWidget()
        self.Part_ColumnWidth_Fixed.setObjectName(u"Part_ColumnWidth_Fixed")
        self.horizontalLayout_9 = QHBoxLayout(self.Part_ColumnWidth_Fixed)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.Part_Numerator = QSpinBox(self.Part_ColumnWidth_Fixed)
        self.Part_Numerator.setObjectName(u"Part_Numerator")

        self.horizontalLayout_9.addWidget(self.Part_Numerator)

        self.label_3 = QLabel(self.Part_ColumnWidth_Fixed)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setMinimumSize(QSize(10, 0))

        self.horizontalLayout_9.addWidget(self.label_3)

        self.Part_Denominator = QSpinBox(self.Part_ColumnWidth_Fixed)
        self.Part_Denominator.setObjectName(u"Part_Denominator")

        self.horizontalLayout_9.addWidget(self.Part_Denominator)

        self.Part_ColumnWidth.addTab(self.Part_ColumnWidth_Fixed, "")
        self.Part_ColumnWidth_Calculated = QWidget()
        self.Part_ColumnWidth_Calculated.setObjectName(u"Part_ColumnWidth_Calculated")
        self.Part_ColumnWidth.addTab(self.Part_ColumnWidth_Calculated, "")

        self.verticalLayout_3.addWidget(self.Part_ColumnWidth)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_11)


        self.PanelsLayout.addWidget(self.frame1)

        self.frame = QFrame(self.PanelsLayout_2)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_20 = QVBoxLayout(self.frame)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_20.addWidget(self.label)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_26 = QLabel(self.frame)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_7.addWidget(self.label_26)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)


        self.verticalLayout_20.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Part_BuildFxl = QCheckBox(self.frame)
        self.Part_BuildFxl.setObjectName(u"Part_BuildFxl")

        self.horizontalLayout_6.addWidget(self.Part_BuildFxl)

        self.Part_BuildPos = QCheckBox(self.frame)
        self.Part_BuildPos.setObjectName(u"Part_BuildPos")

        self.horizontalLayout_6.addWidget(self.Part_BuildPos)

        self.Part_BuildPow = QCheckBox(self.frame)
        self.Part_BuildPow.setObjectName(u"Part_BuildPow")

        self.horizontalLayout_6.addWidget(self.Part_BuildPow)


        self.verticalLayout_20.addLayout(self.horizontalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Part_Fxl = QLineEdit(self.frame)
        self.Part_Fxl.setObjectName(u"Part_Fxl")

        self.horizontalLayout.addWidget(self.Part_Fxl)

        self.Part_Pos = QLineEdit(self.frame)
        self.Part_Pos.setObjectName(u"Part_Pos")

        self.horizontalLayout.addWidget(self.Part_Pos)

        self.Part_Pow = QLineEdit(self.frame)
        self.Part_Pow.setObjectName(u"Part_Pow")

        self.horizontalLayout.addWidget(self.Part_Pow)


        self.verticalLayout_20.addLayout(self.horizontalLayout)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_13)


        self.PanelsLayout.addWidget(self.frame)

        self.frame2 = QFrame(self.PanelsLayout_2)
        self.frame2.setObjectName(u"frame2")
        sizePolicy.setHeightForWidth(self.frame2.sizePolicy().hasHeightForWidth())
        self.frame2.setSizePolicy(sizePolicy)
        self.frame2.setMinimumSize(QSize(450, 0))
        self.frame2.setFrameShape(QFrame.StyledPanel)
        self.frame2.setFrameShadow(QFrame.Plain)
        self.verticalLayout_13 = QVBoxLayout(self.frame2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_13 = QLabel(self.frame2)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_13.addWidget(self.label_13)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.InstrsList = QListWidget(self.frame2)
        self.InstrsList.setObjectName(u"InstrsList")
        sizePolicy2.setHeightForWidth(self.InstrsList.sizePolicy().hasHeightForWidth())
        self.InstrsList.setSizePolicy(sizePolicy2)
        self.InstrsList.setMinimumSize(QSize(0, 200))

        self.horizontalLayout_11.addWidget(self.InstrsList)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.InstrsListAdd = QPushButton(self.frame2)
        self.InstrsListAdd.setObjectName(u"InstrsListAdd")
        self.InstrsListAdd.setMaximumSize(QSize(26, 32))

        self.verticalLayout_16.addWidget(self.InstrsListAdd)

        self.InstrsListDel = QPushButton(self.frame2)
        self.InstrsListDel.setObjectName(u"InstrsListDel")
        self.InstrsListDel.setMaximumSize(QSize(26, 32))

        self.verticalLayout_16.addWidget(self.InstrsListDel)


        self.horizontalLayout_11.addLayout(self.verticalLayout_16)


        self.verticalLayout_13.addLayout(self.horizontalLayout_11)

        self.Instr_Name = QLineEdit(self.frame2)
        self.Instr_Name.setObjectName(u"Instr_Name")

        self.verticalLayout_13.addWidget(self.Instr_Name)

        self.Instr_Type = QTabWidget(self.frame2)
        self.Instr_Type.setObjectName(u"Instr_Type")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Instr_Type.sizePolicy().hasHeightForWidth())
        self.Instr_Type.setSizePolicy(sizePolicy4)
        self.Instr_Type.setMinimumSize(QSize(290, 0))
        self.Instr_Type.setMaximumSize(QSize(6000, 200))
        self.Instr_Type.setBaseSize(QSize(0, 0))
        self.Instr_Type_Module = QWidget()
        self.Instr_Type_Module.setObjectName(u"Instr_Type_Module")
        self.verticalLayout_7 = QVBoxLayout(self.Instr_Type_Module)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_19 = QLabel(self.Instr_Type_Module)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_7.addWidget(self.label_19)

        self.Instr_Module = QLineEdit(self.Instr_Type_Module)
        self.Instr_Module.setObjectName(u"Instr_Module")

        self.verticalLayout_7.addWidget(self.Instr_Module)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.Instr_Type.addTab(self.Instr_Type_Module, "")
        self.Instr_Type_Sequence = QWidget()
        self.Instr_Type_Sequence.setObjectName(u"Instr_Type_Sequence")
        self.verticalLayout_8 = QVBoxLayout(self.Instr_Type_Sequence)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_20 = QLabel(self.Instr_Type_Sequence)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_8.addWidget(self.label_20)

        self.Instr_Sequence = QLineEdit(self.Instr_Type_Sequence)
        self.Instr_Sequence.setObjectName(u"Instr_Sequence")

        self.verticalLayout_8.addWidget(self.Instr_Sequence)

        self.label_21 = QLabel(self.Instr_Type_Sequence)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_8.addWidget(self.label_21)

        self.Instr_Parameter = QLineEdit(self.Instr_Type_Sequence)
        self.Instr_Parameter.setObjectName(u"Instr_Parameter")

        self.verticalLayout_8.addWidget(self.Instr_Parameter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.Instr_Type.addTab(self.Instr_Type_Sequence, "")
        self.Instr_Type_Sample = QWidget()
        self.Instr_Type_Sample.setObjectName(u"Instr_Type_Sample")
        self.verticalLayout_9 = QVBoxLayout(self.Instr_Type_Sample)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_22 = QLabel(self.Instr_Type_Sample)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_9.addWidget(self.label_22)

        self.Instr_Sample = QLineEdit(self.Instr_Type_Sample)
        self.Instr_Sample.setObjectName(u"Instr_Sample")

        self.verticalLayout_9.addWidget(self.Instr_Sample)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_4)

        self.Instr_Type.addTab(self.Instr_Type_Sample, "")
        self.Instr_Type_Expression = QWidget()
        self.Instr_Type_Expression.setObjectName(u"Instr_Type_Expression")
        self.verticalLayout_10 = QVBoxLayout(self.Instr_Type_Expression)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_23 = QLabel(self.Instr_Type_Expression)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_10.addWidget(self.label_23)

        self.Instr_Expression = QLineEdit(self.Instr_Type_Expression)
        self.Instr_Expression.setObjectName(u"Instr_Expression")

        self.verticalLayout_10.addWidget(self.Instr_Expression)

        self.verticalSpacer_5 = QSpacerItem(20, 101, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_5)

        self.Instr_Type.addTab(self.Instr_Type_Expression, "")

        self.verticalLayout_13.addWidget(self.Instr_Type)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_8)


        self.PanelsLayout.addWidget(self.frame2)

        self.frame3 = QFrame(self.PanelsLayout_2)
        self.frame3.setObjectName(u"frame3")
        sizePolicy.setHeightForWidth(self.frame3.sizePolicy().hasHeightForWidth())
        self.frame3.setSizePolicy(sizePolicy)
        self.frame3.setFrameShape(QFrame.StyledPanel)
        self.frame3.setFrameShadow(QFrame.Plain)
        self.verticalLayout_14 = QVBoxLayout(self.frame3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_15 = QLabel(self.frame3)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_14.addWidget(self.label_15)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.BuildsList = QListWidget(self.frame3)
        self.BuildsList.setObjectName(u"BuildsList")
        sizePolicy2.setHeightForWidth(self.BuildsList.sizePolicy().hasHeightForWidth())
        self.BuildsList.setSizePolicy(sizePolicy2)
        self.BuildsList.setMinimumSize(QSize(0, 200))

        self.horizontalLayout_8.addWidget(self.BuildsList)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.BuildsListAdd = QPushButton(self.frame3)
        self.BuildsListAdd.setObjectName(u"BuildsListAdd")
        self.BuildsListAdd.setMaximumSize(QSize(26, 32))

        self.verticalLayout_17.addWidget(self.BuildsListAdd)

        self.BuildsListDel = QPushButton(self.frame3)
        self.BuildsListDel.setObjectName(u"BuildsListDel")
        self.BuildsListDel.setMaximumSize(QSize(26, 32))

        self.verticalLayout_17.addWidget(self.BuildsListDel)


        self.horizontalLayout_8.addLayout(self.verticalLayout_17)


        self.verticalLayout_14.addLayout(self.horizontalLayout_8)

        self.Build_Name = QLineEdit(self.frame3)
        self.Build_Name.setObjectName(u"Build_Name")

        self.verticalLayout_14.addWidget(self.Build_Name)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_9)


        self.PanelsLayout.addWidget(self.frame3)

        self.frame4 = QFrame(self.PanelsLayout_2)
        self.frame4.setObjectName(u"frame4")
        sizePolicy.setHeightForWidth(self.frame4.sizePolicy().hasHeightForWidth())
        self.frame4.setSizePolicy(sizePolicy)
        self.frame4.setFrameShape(QFrame.StyledPanel)
        self.verticalLayout_6 = QVBoxLayout(self.frame4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.frame4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.StavesList = QListWidget(self.frame4)
        self.StavesList.setObjectName(u"StavesList")
        sizePolicy2.setHeightForWidth(self.StavesList.sizePolicy().hasHeightForWidth())
        self.StavesList.setSizePolicy(sizePolicy2)
        self.StavesList.setMinimumSize(QSize(0, 200))

        self.horizontalLayout_4.addWidget(self.StavesList)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.StavesListAdd = QPushButton(self.frame4)
        self.StavesListAdd.setObjectName(u"StavesListAdd")
        self.StavesListAdd.setMaximumSize(QSize(26, 32))

        self.verticalLayout_18.addWidget(self.StavesListAdd)

        self.StavesListDel = QPushButton(self.frame4)
        self.StavesListDel.setObjectName(u"StavesListDel")
        self.StavesListDel.setMaximumSize(QSize(26, 32))

        self.verticalLayout_18.addWidget(self.StavesListDel)


        self.horizontalLayout_4.addLayout(self.verticalLayout_18)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.Stave_Name = QLineEdit(self.frame4)
        self.Stave_Name.setObjectName(u"Stave_Name")

        self.verticalLayout_6.addWidget(self.Stave_Name)

        self.label_16 = QLabel(self.frame4)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_6.addWidget(self.label_16)

        self.Stave_Build = QLineEdit(self.frame4)
        self.Stave_Build.setObjectName(u"Stave_Build")

        self.verticalLayout_6.addWidget(self.Stave_Build)

        self.label_27 = QLabel(self.frame4)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_6.addWidget(self.label_27)

        self.Stave_Instr = QLineEdit(self.frame4)
        self.Stave_Instr.setObjectName(u"Stave_Instr")

        self.verticalLayout_6.addWidget(self.Stave_Instr)

        self.label_17 = QLabel(self.frame4)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_6.addWidget(self.label_17)

        self.Stave_Condition = QLineEdit(self.frame4)
        self.Stave_Condition.setObjectName(u"Stave_Condition")

        self.verticalLayout_6.addWidget(self.Stave_Condition)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_12)


        self.PanelsLayout.addWidget(self.frame4)

        self.frame5 = QFrame(self.PanelsLayout_2)
        self.frame5.setObjectName(u"frame5")
        sizePolicy.setHeightForWidth(self.frame5.sizePolicy().hasHeightForWidth())
        self.frame5.setSizePolicy(sizePolicy)
        self.frame5.setFrameShape(QFrame.StyledPanel)
        self.verticalLayout_2 = QVBoxLayout(self.frame5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.frame5)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.NotesList = QListWidget(self.frame5)
        self.NotesList.setObjectName(u"NotesList")
        sizePolicy2.setHeightForWidth(self.NotesList.sizePolicy().hasHeightForWidth())
        self.NotesList.setSizePolicy(sizePolicy2)
        self.NotesList.setMinimumSize(QSize(0, 200))
        self.NotesList.setMaximumSize(QSize(16777215, 200))

        self.horizontalLayout_5.addWidget(self.NotesList)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.NotesListAdd = QPushButton(self.frame5)
        self.NotesListAdd.setObjectName(u"NotesListAdd")
        self.NotesListAdd.setMaximumSize(QSize(26, 32))

        self.verticalLayout_19.addWidget(self.NotesListAdd)

        self.NotesListDel = QPushButton(self.frame5)
        self.NotesListDel.setObjectName(u"NotesListDel")
        self.NotesListDel.setMaximumSize(QSize(26, 32))

        self.verticalLayout_19.addWidget(self.NotesListDel)


        self.horizontalLayout_5.addLayout(self.verticalLayout_19)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.Note_Column = QSpinBox(self.frame5)
        self.Note_Column.setObjectName(u"Note_Column")

        self.verticalLayout_2.addWidget(self.Note_Column)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_14 = QLabel(self.frame5)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_12.addWidget(self.label_14)

        self.label_11 = QLabel(self.frame5)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_12.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame5)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_12.addWidget(self.label_12)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Note_Fxl = QLineEdit(self.frame5)
        self.Note_Fxl.setObjectName(u"Note_Fxl")
        self.Note_Fxl.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_3.addWidget(self.Note_Fxl)

        self.Note_Pos = QLineEdit(self.frame5)
        self.Note_Pos.setObjectName(u"Note_Pos")
        self.Note_Pos.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_3.addWidget(self.Note_Pos)

        self.Note_Pow = QLineEdit(self.frame5)
        self.Note_Pow.setObjectName(u"Note_Pow")
        self.Note_Pow.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_3.addWidget(self.Note_Pow)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.PanelsLayout.addWidget(self.frame5)


        self.verticalLayout.addWidget(self.PanelsLayout_2)

        self.frameMatrix = QFrame(self.centralwidget)
        self.frameMatrix.setObjectName(u"frameMatrix")
        sizePolicy.setHeightForWidth(self.frameMatrix.sizePolicy().hasHeightForWidth())
        self.frameMatrix.setSizePolicy(sizePolicy)
        self.frameMatrix.setFrameShape(QFrame.StyledPanel)
        self.frameMatrix.setFrameShadow(QFrame.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.frameMatrix)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_18 = QLabel(self.frameMatrix)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_5.addWidget(self.label_18)

        self.StavesTable = QTableWidget(self.frameMatrix)
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


        self.verticalLayout.addWidget(self.frameMatrix)

        pApp.setCentralWidget(self.centralwidget)

        self.retranslateUi(pApp)

        self.Part_Role.setCurrentIndex(0)
        self.Part_ColumnWidth.setCurrentIndex(0)
        self.Instr_Type.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(pApp)
    # setupUi

    def retranslateUi(self, pApp):
        pApp.setWindowTitle(QCoreApplication.translate("pApp", u"p", None))
        self.label_7.setText(QCoreApplication.translate("pApp", u"Score", None))
        self.label_10.setText(QCoreApplication.translate("pApp", u"Duration", None))
        self.bScoreLoad.setText(QCoreApplication.translate("pApp", u"Load", None))
        self.bScoreSave.setText(QCoreApplication.translate("pApp", u"Save", None))
        self.bRun.setText(QCoreApplication.translate("pApp", u"Run", None))
        self.label_2.setText(QCoreApplication.translate("pApp", u"Partitures", None))
        self.PartsListAdd.setText(QCoreApplication.translate("pApp", u"+", None))
        self.PartsListDel.setText(QCoreApplication.translate("pApp", u"-", None))
        self.Part_ZeroLength.setText(QCoreApplication.translate("pApp", u"Zero Length", None))
        self.label_24.setText(QCoreApplication.translate("pApp", u"Pitch", None))
        self.Part_Role.setTabText(self.Part_Role.indexOf(self.Part_Role_Main), QCoreApplication.translate("pApp", u"Main", None))
        self.label_25.setText(QCoreApplication.translate("pApp", u"Transpose", None))
        self.Part_Role.setTabText(self.Part_Role.indexOf(self.Part_Role_Function), QCoreApplication.translate("pApp", u"Function", None))
        self.Part_Role.setTabText(self.Part_Role.indexOf(self.Part_Role_None), QCoreApplication.translate("pApp", u"None", None))
        self.label_9.setText(QCoreApplication.translate("pApp", u"Column width", None))
        self.label_3.setText(QCoreApplication.translate("pApp", u"/", None))
        self.Part_ColumnWidth.setTabText(self.Part_ColumnWidth.indexOf(self.Part_ColumnWidth_Fixed), QCoreApplication.translate("pApp", u"Fixed", None))
        self.Part_ColumnWidth.setTabText(self.Part_ColumnWidth.indexOf(self.Part_ColumnWidth_Calculated), QCoreApplication.translate("pApp", u"Calculated", None))
        self.label.setText(QCoreApplication.translate("pApp", u"Build", None))
        self.label_26.setText(QCoreApplication.translate("pApp", u"Fxl", None))
        self.label_6.setText(QCoreApplication.translate("pApp", u"Pos", None))
        self.label_8.setText(QCoreApplication.translate("pApp", u"Pow", None))
        self.Part_BuildFxl.setText("")
        self.Part_BuildPos.setText("")
        self.Part_BuildPow.setText("")
        self.label_13.setText(QCoreApplication.translate("pApp", u"Instruments", None))
        self.InstrsListAdd.setText(QCoreApplication.translate("pApp", u"+", None))
        self.InstrsListDel.setText(QCoreApplication.translate("pApp", u"-", None))
        self.label_19.setText(QCoreApplication.translate("pApp", u"File", None))
        self.Instr_Type.setTabText(self.Instr_Type.indexOf(self.Instr_Type_Module), QCoreApplication.translate("pApp", u"Module", None))
        self.label_20.setText(QCoreApplication.translate("pApp", u"Sequence", None))
        self.label_21.setText(QCoreApplication.translate("pApp", u"Parameter", None))
        self.Instr_Type.setTabText(self.Instr_Type.indexOf(self.Instr_Type_Sequence), QCoreApplication.translate("pApp", u"Sequence", None))
        self.label_22.setText(QCoreApplication.translate("pApp", u"Sample", None))
        self.Instr_Type.setTabText(self.Instr_Type.indexOf(self.Instr_Type_Sample), QCoreApplication.translate("pApp", u"Sample", None))
        self.label_23.setText(QCoreApplication.translate("pApp", u"Expression", None))
        self.Instr_Type.setTabText(self.Instr_Type.indexOf(self.Instr_Type_Expression), QCoreApplication.translate("pApp", u"Expression", None))
        self.label_15.setText(QCoreApplication.translate("pApp", u"Builds", None))
        self.BuildsListAdd.setText(QCoreApplication.translate("pApp", u"+", None))
        self.BuildsListDel.setText(QCoreApplication.translate("pApp", u"-", None))
        self.label_4.setText(QCoreApplication.translate("pApp", u"Staves", None))
        self.StavesListAdd.setText(QCoreApplication.translate("pApp", u"+", None))
        self.StavesListDel.setText(QCoreApplication.translate("pApp", u"-", None))
        self.label_16.setText(QCoreApplication.translate("pApp", u"Build", None))
        self.label_27.setText(QCoreApplication.translate("pApp", u"Instrument", None))
        self.label_17.setText(QCoreApplication.translate("pApp", u"Condition", None))
        self.label_5.setText(QCoreApplication.translate("pApp", u"Notes", None))
        self.NotesListAdd.setText(QCoreApplication.translate("pApp", u"+", None))
        self.NotesListDel.setText(QCoreApplication.translate("pApp", u"-", None))
        self.label_14.setText(QCoreApplication.translate("pApp", u"Fxl", None))
        self.label_11.setText(QCoreApplication.translate("pApp", u"Pos", None))
        self.label_12.setText(QCoreApplication.translate("pApp", u"Pow", None))
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

    # retranslateUi

