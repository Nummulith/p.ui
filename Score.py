from PyQt5 import QtWidgets, QtCore, uic, QtGui

from xml.dom import minidom
import xml.etree.ElementTree as ET

import linecache
import inspect

from jinja2 import Template

def PrintCallStack():

#    current_frame = inspect.currentframe() # Получаем текущий фрейм (контекст выполнения кода)
#    current_code = inspect.getsource(current_frame.f_code) # Получаем код из текущего фрейма


    call_stack = inspect.stack() # Получаем текущий стек вызовов

    res = ""
    for frame_info in call_stack: # Выводим информацию о каждом уровне стека вызовов
        frame = frame_info[0]
        filename = frame_info[1]
        line_number = frame_info[2]
        function_name = frame_info[3]

        if function_name == "PrintCallStack": continue
        if function_name == "<module>": break

        # Получаем строку кода из файла
        code_line = linecache.getline(filename, line_number)

        res += f" {code_line.strip()} {line_number} {function_name}\n"

    return res

def PrintCallStack1():
    # Получаем список фреймов стека вызовов
    frames = inspect.getouterframes(inspect.currentframe())

    # Выводим строки кода из каждой функции
    for frame_info in frames[1:]:  # Пропускаем текущий фрейм (индекс 0)
        frame = frame_info.frame
        filename = frame_info.filename
        line_number = frame_info.lineno
        function_name = frame_info.function

        # Получаем строку кода из файла
        code_line = linecache.getline(filename, line_number)

        print(f"File: {filename}, Line: {line_number}, Function: {function_name}")
        print(f"Code Line: {code_line.strip()}")  # Выводим строку кода без символа новой строки

def find_column(Matrix, name):
    # Ищем индекс колонки по имени
    for column in range(Matrix.columnCount()):
        header_item = Matrix.horizontalHeaderItem(column)
        if header_item.text() == name:
            return column
    return -1  # Возвращаем -1, если колонка с таким именем не найдена

def prettify(elem):
    """Возвращает красиво отформатированный XML-элемент"""
    rough_string = ET.tostring(elem, "utf-8")
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

def print_widget_hierarchy(widget, indent=0):
    # не печатает лейауты ((
    print("  " * indent + "-" + widget.objectName() + " (" + widget.metaObject().className() + ")")

    for child_widget in widget.findChildren(QtWidgets.QWidget):
        if child_widget.parent() == widget:  # Check if the child's parent is the widget itself
            print_widget_hierarchy(child_widget, indent + 1)

def SomeDrafts_________________(self):
    currow = -1
    curcol = -1
    indexes = self.StavesTable.selectedIndexes()
    if len(indexes) > 0:
        currow = indexes[0].row()
        curcol = indexes[0].column()

    if False:
        item = QtWidgets.QTableWidgetItem(stave.Name)
        self.StavesTable.setVerticalHeaderItem(pos, item)

        #item = self.StavesTable.verticalHeaderItem(curstrcount)
        #item.setText(stave.Name)
        #self.StavesTable.setCurrentCell(currow, curind)

        #item = QtWidgets.QTableWidgetItem("O")
        #item.setTextAlignment(QtCore.Qt.AlignVCenter)
        #item.setBackground(QtGui.QColor(255, 0, 0))  # Красный фон
        #item.setTextAlignment(QtCore.Qt.AlignVCenter)
        #item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable)  # Разрешаем редактирование
        #self.StavesTable.setItem(pos, 0, item)

            #list1 = [1, 2, 3]
            #list2 = ['a', 'b', 'c']
            #for item1, item2 in zip(list1, list2):
            #    print(item1, item2)
            #self.NotesList.addItem("(")
            #self.NotesList.insertItem(0, ")")


CELL_SIZE = 45

class Score:
    def __init__(self, Name=""):
        self.Items = []
        self.Index = -1

        self.Name = Name
        self.Duration = 2100

    @staticmethod
    def next():
        return Part

class Part:
    def __init__(self, Name="", Numerator=4, Denominator=8):
        self.Items = []
        self.Index = -1

        self.Name = Name
        self.Numerator = Numerator
        self.Denominator = Denominator

    def View(self):
        return self.Name
    
    @staticmethod
    def prev():
        return Score

    @staticmethod
    def next():
        return Stave

class Stave:
    def __init__(self, Name=""):
        self.Items = []
        self.Index = -1

        self.Name  = Name
        self.Build = ""
        self.Condition = ""
        self.Type = "Module"
        self.ZeroLength = False
        self.Sequence = ""
        self.Parameter = ""
        self.Sample = ""
        self.Expression = ""

    def View(self):
        return self.Name
    
    @staticmethod
    def prev():
        return Part

    @staticmethod
    def next():
        return Note

class Note:
    def __init__(self, Column=0, Fxl="", Pos="", Pow=""):
        self.Column = Column
        self.Fxl = Fxl
        self.Pos = Pos
        self.Pow = Pow

    @staticmethod
    def prev():
        return Stave
    
    def View(self):
        return f"{self.Column}: {self.CellView()}"
    
    def CellView(self):
        return f"{self.Fxl} {self.Pos} {self.Pow}"


class Map:
    def __init__(self, wnd, clss, vallist = None):
        self.Class = clss
        self.List = vallist
        self.Dict = []
        el = clss()
        for key in list(el.__dict__.keys()):
            if key.startswith('__') \
                or key == "Items"\
                or key == "Index"\
                or isinstance(getattr(el, key), list)\
            :
                continue
            self.Dict.append(key)

        self.Mapper = QtWidgets.QDataWidgetMapper(wnd)
        self.Mapper.setModel(QtGui.QStandardItemModel())

        for attr_index, attr_name in enumerate(self.Dict):
            cl_attr_name = el.__class__.__name__ + "_" + attr_name
            if hasattr(wnd, cl_attr_name):
                widget = getattr(wnd, cl_attr_name)
                if isinstance(widget, QtWidgets.QWidget):
                    self.Mapper.addMapping(widget, attr_index)

#                    handler = lambda reserved=None, c=self.Class, a=attr_name, w=widget: wnd.updateObject(reserved, c, a, w)
                    handler = wnd.updateObjectHandler(clss, attr_name, widget)

                    if isinstance(widget, QtWidgets.QTabWidget):
                        event = widget.currentChanged
                    elif isinstance(widget, QtWidgets.QCheckBox):
                        event = widget.stateChanged
                    else:
                        event = widget.editingFinished

                    event.connect(handler)

    def FillModel(self, items):
        self.Mapper.model().clear()
        for inst in items:
            self.Mapper.model().appendRow([QtGui.QStandardItem(str(getattr(inst, value))) for value in self.Dict])

    def IsEmpty(self):
        return self.Mapper.model().rowCount() == 0

    def PosModel(self, wnd, index):
#        max = self.Mapper.model().rowCount() - 1
#        if index < 0 or index > max:
#            return False

        self.Mapper.setCurrentIndex(index)


class Window(QtWidgets.QMainWindow, uic.loadUiType('Score.ui')[0]):

    def updateObjectHandler(self, clss, attr_name, widget):
        return lambda reserved=None, c=clss, a=attr_name, w=widget: self.updateObject(reserved, c, a, w)
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        # interface

        self.centralwidget.layout().setAlignment(QtCore.Qt.AlignTop)

        self.bScoreLoad.clicked.connect(self.LoadScore)
        self.bScoreSave.clicked.connect(self.SaveScore)

        self.bRun.clicked.connect(self.Run)

        self.PartsList .itemSelectionChanged.connect(self.PartsSelectionChanged )
        self.StavesList.itemSelectionChanged.connect(self.StavesSelectionChanged)
        self.NotesList .itemSelectionChanged.connect(self.NotesSelectionChanged )
        
        self.StavesTable.cellClicked.connect(self.StavesTableCellClicked)

        self.StavesTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        self.StavesTable.horizontalHeader().setMinimumSectionSize(CELL_SIZE)
        self.StavesTable.horizontalHeader().setMaximumSectionSize(CELL_SIZE)

        self.StavesTable.verticalHeader()  .setMinimumSectionSize(CELL_SIZE)
        self.StavesTable.verticalHeader()  .setMaximumSectionSize(CELL_SIZE)



        # visibility buttons 

        panels = []
        for i in range(self.PanelsLayout.count()):
            layout = self.PanelsLayout.itemAt(i)
            widget = layout.widget()
            if not isinstance(layout, QtWidgets.QWidgetItem) or not isinstance(widget, QtWidgets.QWidget):
                continue

            sublayout = widget.layout()
            if sublayout is None or sublayout.count() == 0:
                continue

            panels.append(widget)


        splitter = QtWidgets.QSplitter(self)
        splitter.setObjectName("PanelsLayoutSplitter")  # Устанавливаем имя для стиля
        self.PanelsLayout.addWidget(splitter)


        splitter.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)


        self.ButtonsLayout.setAlignment(QtCore.Qt.AlignLeft)
        for widget in panels:

            splitter.addWidget(widget)

            label = widget.layout().itemAt(0)
            if not label.widget() or not isinstance(label.widget(), QtWidgets.QLabel):
                continue

            name = widget.objectName()
            text = label.widget().text()
            #print(f"N: {i}, Panel: {name}, Label: {text}")

            button = QtWidgets.QPushButton(text)
            button.setCheckable(True)
            button.setChecked  (True)

            handler = lambda state, n = name: getattr(self, n).setVisible(state)
            button.clicked.connect(handler)

            button.setMaximumWidth(200)

            self.ButtonsLayout.addWidget(button)

#       print_widget_hierarchy(self)


#       Load and draw

        self.LoadScore()
        self.InitMaps()
        self.Position(Score, True, 0)
        self.DrawStavesTable()


    def InitMaps(self):
        self.Maps = {}
        self.Maps[Score] = Map(self, Score)
        self.Maps[Part ] = Map(self, Part , self.PartsList )
        self.Maps[Stave] = Map(self, Stave, self.StavesList)
        self.Maps[Note ] = Map(self, Note , self.NotesList )
#        self.Maps[Score].FillModel(self.Score)

        self.Objs = {}

    def Position(self, clss, fillList = False, index = None):
        curmap = self.Maps[clss]

        if   clss == Score :
            par = None
            items = self.Score
            curind = 0
        else: #if clss != Note 
            par = self.Objs[clss.prev()]
            items  = par.Items
            if index == None:
                curind = int(par.Index)
            else:
                curind = index[0] if isinstance(index, list) else index
                par.Index = curind

        self.Objs[clss] = items[curind] if curind != -1 else None

        empty = len(items) == 0


        if fillList:
            curmap.FillModel(items)

        curmap.PosModel(self, curind)


        if   clss == Part:
            
            self.PartsList .itemSelectionChanged.disconnect()

            if fillList:
                self.PartsList.clear()

                for part in items:
                    self.PartsList.addItem(part.Name)

            self.PartsList .setCurrentRow(curind)

            self.PartsList .itemSelectionChanged.connect(self.PartsSelectionChanged)

        elif clss == Stave:

            self.StavesList.itemSelectionChanged.disconnect()

            if fillList :
                self.StavesList.clear()
                #self.StavesTable.setRowCount(0)
                for stave in items:
                    self.StavesList.addItem(stave.Name)

            self.StavesList.setCurrentRow(curind)
            
            self.StavesList.itemSelectionChanged.connect(self.StavesSelectionChanged)

        elif clss == Note:

            self.NotesList.itemSelectionChanged.disconnect()

            if fillList :
                self.NotesList.clear()

                for i, note in zip(range(0, len(items)), items):
                    self.NotesList.addItem("")
                    self.SetView(self.NotesList, i, note)

            self.NotesList.setCurrentRow(curind)

            self.NotesList.itemSelectionChanged.connect(self.NotesSelectionChanged)


        for attr_name in curmap.Dict:
            cl_attr_name = clss.__name__ + "_" + attr_name
            wgt = getattr(self, cl_attr_name)
            if index != -1:
                if isinstance(wgt, QtWidgets.QTabWidget):

                    wgt.currentChanged.disconnect()

                    wgt.setCurrentWidget(
                        wgt.findChild(QtWidgets.QWidget, wgt.objectName() + "_" + getattr(self.Objs[clss], attr_name))
                    )

                    wgt.currentChanged.connect(
                        self.updateObjectHandler(clss, attr_name, wgt)
                    )


            else: # empty cell
                if isinstance(wgt, QtWidgets.QSpinBox):
                    wgt.setValue(0)
                elif isinstance(wgt, QtWidgets.QLineEdit):
                    wgt.setText("")


        if clss != Note:
            nxtind = index[1] if isinstance(index, list) else None
            self.Position(clss.next(), True, nxtind)

    def SetView(self, vallist, index, Obj):
        item = vallist.item(index)
        item.setText(Obj.View())

    def updateObject(self, reserved, clss, attr, wdg):
        if isinstance(wdg, QtWidgets.QLineEdit):
            value = wdg.text()
        elif isinstance(wdg, QtWidgets.QSpinBox):
            value = wdg.value()
        elif isinstance(wdg, QtWidgets.QTabWidget):
            value = wdg.currentWidget().objectName()
            value = value.replace(wdg.objectName() + "_", "")
        elif isinstance(wdg, QtWidgets.QCheckBox):
            value = wdg.isChecked()
        else: 
            value = "" # ?

        obj = self.Objs[clss]

        if obj == None:
            obj = clss()
            par = self.Objs[clss.prev()]
            par.Items.append(obj)
            self.Position(clss, True, len(par.Items) - 1)

        setattr(obj, attr, value)

        vallist = self.Maps[clss].List
        if vallist != None:
            par = self.Objs[clss.prev()]
            self.SetView(vallist, int(par.Index), obj)

    def updateObject__obs(self, map, a, w):
        items = self.Score
        for curmap in self.Maps.values():
            index = curmap.Mapper.currentIndex()
            obj = items[index]

            if curmap.Mapper != map.Mapper:
                items = obj.Items
            else:
                if isinstance(w, QtWidgets.QLineEdit):
                    value = w.text()
                elif isinstance(w, QtWidgets.QSpinBox):
                    value = w.value()
                else: 
                    value = "" # ?

                setattr(obj, a, value)

                break

    def DrawStavesTable(self):
        curscore = self.Score[0]
        curpart  = curscore.Items[int(curscore.Index)]
        
#        if clss == Score or clss == Part :
#?          self.StavesTable.clear()
        for i in range(0, self.StavesTable.rowCount()):
            self.StavesTable.removeRow(0)
        for i in range(0, self.StavesTable.columnCount()):
            self.StavesTable.removeColumn(0)

        curstr = -1
        for curstave in curpart.Items:
            curstr += 1

            curstrcount = self.StavesTable.rowCount()
            self.StavesTable.insertRow(curstrcount)
            self.StavesTable.setRowHeight(curstrcount, CELL_SIZE)

            item = QtWidgets.QTableWidgetItem(curstave.Name)
            self.StavesTable.setVerticalHeaderItem(curstrcount, item)

            for curnote in curstave.Items:
                
                curcol = int(curnote.Column)
                curcolcount = self.StavesTable.columnCount()

                if curcol > curcolcount - 1:
                    self.StavesTable.setColumnCount(curcol + 1)

                    for i in range(curcolcount, curcol + 1):
                        item = QtWidgets.QTableWidgetItem(str(i))
                        item.setFlags(QtCore.Qt.ItemIsUserCheckable)
                        self.StavesTable.setHorizontalHeaderItem(i, item)

                        self.StavesTable.setColumnWidth(i, CELL_SIZE)


                item = QtWidgets.QTableWidgetItem(curnote.Fxl + curnote.Pos + curnote.Pow)
                self.StavesTable.setItem(curstr, curcol, item)

        self.PosStavesTable()

    def PosStavesTable(self):
        curscore = self.Score[0]
        curpart  = curscore.Items[int(curscore.Index)]
        curstave = curpart .Items[int(curpart .Index)]

        if curstave.Index != -1:
            curnote  = curstave.Items[int(curstave.Index)]
            curcol = int(curnote.Column)

            self.StavesTable.setCurrentCell(int(curpart.Index), curcol)


    def PartsSelectionChanged(self):
        self.Position(Part , False, self.PartsList .currentRow())
        self.DrawStavesTable()

    def StavesSelectionChanged(self):
        self.Position(Stave, False, self.StavesList.currentRow())
        self.PosStavesTable()

    def NotesSelectionChanged(self):
        self.Position(Note , False, self.NotesList .currentRow())
        self.PosStavesTable()

    def StavesTableCellClicked(self, row, col):
#        self.Position(Stave, False, row)

        curscore = self.Score[0]
        curpart  = curscore.Items[int(curscore.Index)]
        curstave = curpart .Items[row] # int(curpart .Index)

        ind = -1
        curind = -1
        for curnote in curstave.Items:
            curind += 1
            curcol = int(curnote.Column)
            if col == curcol:
                ind = curind
                break
        
        self.Position(Stave, False, [row, ind])

        if ind == -1:
            self.Note_Column.setValue(col)


    def Run(self):
        with open('template.j2', 'r') as file: template_str = file.read()

        template_str = "".join([line.strip() for line in template_str.splitlines()])

        template = Template(template_str)

        output = template.render(scores=self.Score)

        with open('score.p', 'w') as file: file.write(output)


    def LoadScorePreset(self):
        self.Score = []

        self.Score.append(Score("amen brother"))
        song = self.Score[0]
        
        song.Items.append(Part("Bass" , 5, 8))
        song.Items[0].Items.append(Stave("Fast", "slap", "!0"))
        song.Items[0].Items.append(Stave("Fast", "smooth", "!0"))

        song.Items[0].Items[0].Items.append(Note(2, "1", "q", "7"))
        song.Items[0].Items[0].Items.append(Note(3, "2", "w", "8"))
        song.Items[0].Items[0].Items.append(Note(5, "3", "e", "9"))

        song.Items[0].Items[1].Items.append(Note(1, "4", "r", "0"))
        song.Items[0].Items[1].Items.append(Note(2, "5", "t", "-"))
        song.Items[0].Items[1].Items.append(Note(4, "6", "y", "="))

        song.Items.append(Part("Drums", 4, 2))
        song.Items[1].Items.append(Stave("Fast", "Snare", "!0"))
        song.Items[1].Items.append(Stave("Fast", "kick!", "!0"))

        song.Items[1].Items[0].Items.append(Note(2, "1", "a", "f"))
        song.Items[1].Items[0].Items.append(Note(3, "2", "s", "g"))
        song.Items[1].Items[0].Items.append(Note(4, "3", "d", "h"))

        song.Items[1].Items[1].Items.append(Note(3, "4", "f", "j"))
        song.Items[1].Items[1].Items.append(Note(4, "5", "g", "k"))
        song.Items[1].Items[1].Items.append(Note(5, "6", "h", "l"))

    def LoadScore(self):
        xml_file_path = "Score.xml" # Путь к XML файлу
        xscore = ET.parse(xml_file_path).getroot() # Чтение XML файла

        self.Score = []
        score = Score()
        self.Score.append(score)

        for name, value in xscore.attrib.items():
            setattr(score, name, value)

        for xpart in xscore:
            part = Part()
            score.Items.append(part)

            for name, value in xpart.attrib.items():
                setattr(part, name, value)

            for xstave in xpart:
                stave = Stave()
                part.Items.append(stave)

                for name, value in xstave.attrib.items():
                    setattr(stave, name, value)

                for xnote in xstave:
                    note = Note()
                    stave.Items.append(note)

                    for name, value in xnote.attrib.items():
                        setattr(note, name, value)

        self.setGeometry(
            int(xscore.attrib['window_left'  ]),
            int(xscore.attrib['window_top'   ]),
            int(xscore.attrib['window_width' ]),
            int(xscore.attrib['window_height']),
        )


    def SaveScore(self):
        for score in self.Score:
            xscore = ET.Element("Score") # Создание корневого элемента XML

            for attr in self.Maps[Score].Dict + ["Index"]:
                xscore.set(attr, str(getattr(score, attr)))

            for part in score.Items:
                xpart = ET.SubElement(xscore, "Part")

                for attr in self.Maps[Part].Dict + ["Index"]:
                    xpart.set(attr, str(getattr(part, attr)))

                for stave in part.Items:
                    xstave = ET.SubElement(xpart, "Stave")

                    for attr in self.Maps[Stave].Dict + ["Index"]:
                        xstave.set(attr, str(getattr(stave, attr)))

                    for note in stave.Items:
                        xnote = ET.SubElement(xstave, "Note")

                        for attr in self.Maps[Note].Dict:
                            xnote.set(attr, str(getattr(note, attr)))
            
            #xml_tree = ET.ElementTree(xscore) # Создание XML-документа
            #xml_tree.write("ScoreSaved.xml") # Сохранение XML-документа в файл

            xscore.set("window_left"  , str(self.geometry().x()))
            xscore.set("window_top"   , str(self.geometry().y()))
            xscore.set("window_width" , str(self.geometry().width ()))
            xscore.set("window_height", str(self.geometry().height()))

            # Сохранение XML с отступами и переносами строк
            with open("Score.xml", "w") as xml_file:
                xml_file.write(prettify(xscore))            
            break


    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        self.SaveScore()
        event.accept()

app = QtWidgets.QApplication([])
window = Window()
window.show()
app.exec_()
