import xml.etree.ElementTree as ET
#import traceback
import linecache
import inspect
from xml.dom import minidom
from PyQt5 import QtWidgets, QtCore, uic, QtGui

CELL_SIZE = 45

class Score:
    def __init__(self, Name=""):
        self.Items = []
        self.Index = -1

        self.Name = Name
        self.Duration = 2100

class Part:
    def __init__(self, Name="", Numerator=4, Denominator=8):
        self.Items = []
        self.Index = -1

        self.Name = Name
        self.Numerator = Numerator
        self.Denominator = Denominator

class Stave:
    def __init__(self, Build="", Name="", Condition=""):
        self.Items = []
        self.Index = -1

        self.Name  = Name
        self.Build = Build
        self.Condition = Condition

class Note:
    def __init__(self, Column=0, Fxl="", Pos="", Pow=""):
        self.Column = Column
        self.Fxl = Fxl
        self.Pos = Pos
        self.Pow = Pow


class Map:
    def __init__(self, wnd, clss):
        self.Class = clss
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

                    #widget.editingFinished.connect(wnd.updateModel)
                    handler = lambda m=self.Mapper, a=attr_name, w=widget: wnd.updateModel(m, a, w)
                    widget.editingFinished.connect(handler)

    def FillModel(self, arr):
        self.Mapper.model().clear()
        for inst in arr:
            self.Mapper.model().appendRow([QtGui.QStandardItem(str(getattr(inst, value))) for value in self.Dict])

    def IsEmpty(self):
        return self.Mapper.model().rowCount() == 0

    def PosModel(self, index):
        max = self.Mapper.model().rowCount() - 1

        if index < 0 or index > max:
            return False
        
        self.Mapper.setCurrentIndex(index)

        return True

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



class Window(QtWidgets.QMainWindow, uic.loadUiType('Score.ui')[0]):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


        # interface

        self.centralwidget.layout().setAlignment(QtCore.Qt.AlignTop)

        self.bScoreLoad.clicked.connect(self.LoadScore)
        self.bScoreSave.clicked.connect(self.SaveScore)

        self.PartsList .itemSelectionChanged.connect(self.PartsSelectionChanged )
        self.StavesList.itemSelectionChanged.connect(self.StavesSelectionChanged)
        self.NotesList .itemSelectionChanged.connect(self.NotesSelectionChanged )
        
        self.StavesTable.cellClicked.connect(self.StavesTableCellClicked)

        self.StavesTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        self.StavesTable.horizontalHeader().setMinimumSectionSize(CELL_SIZE)
        self.StavesTable.horizontalHeader().setMaximumSectionSize(CELL_SIZE)

        self.StavesTable.verticalHeader()  .setMinimumSectionSize(CELL_SIZE)
        self.StavesTable.verticalHeader()  .setMaximumSectionSize(CELL_SIZE)



        self.printdivider.clicked.connect(self.PrintDivider)


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
        self.Maps[Part ] = Map(self, Part )
        self.Maps[Stave] = Map(self, Stave)
        self.Maps[Note ] = Map(self, Note )
#        self.Maps[Score].FillModel(self.Score)

    def Position(self, clss, fillList = False, curind = None):
        if   clss == Score :
            obj = None
            items = self.Score
            curind = 0
        elif clss != Note :
            obj = items[curind] if curind != -1 else None
            items  = obj.Items
#            curind = int(obj.Index)
            obj.Index = curind

        empty = len(items) == 0

        if   clss == Part:
            
            self.PartsList .itemSelectionChanged.disconnect()

            if fillList :
                self.PartsList.clear()

                for part in items:
                    self.PartsList.addItem(part.Name)

            self.PartsList .setCurrentRow(curind)

            self.PartsList .itemSelectionChanged.connect(self.PartsSelectionChanged)

        elif clss == Stave:

            if fillList :
                self.StavesList.clear()
                #self.StavesTable.setRowCount(0)
                for stave in items:
                    self.StavesList.addItem(stave.Name)

            self.StavesList.setCurrentRow(curind)
            
        elif clss == Note:

            if fillList :
                self.NotesList.clear()

                #list1 = [1, 2, 3]
                #list2 = ['a', 'b', 'c']

                #for item1, item2 in zip(list1, list2):
                #    print(item1, item2)

                for i, note in zip(range(0, len(items)), items):
                    self.NotesList.addItem(f"{note.Column}: {note.Fxl} {note.Pos} {note.Pow}")
                    #self.NotesList.insertItem(0, ")")

                #self.NotesList.addItem("(")
                #self.NotesList.insertItem(0, ")")

                self.NotesList .setCurrentRow(curind)



        #        if not fromthis:
        #            curmap.FillModel(items)
        # Position()
        # map.PosModel(curind)

    def Position____________withloop(self, clss, index):
        print("<", clss, index, PrintCallStack())
#        PrintCallStack1()
#        traceback.print_exc()

        # Model and lists

        obj = None
        items = self.Score
        curind = 0
        already = False
        empty = False
        for curclss, curmap in self.Maps.items():
            
            fromthis = curclss == clss

            if not already and fromthis:
                already = True
                curind = index

            if not empty:
                empty = len(items) == 0

            if already:
                if not fromthis:
                    curmap.FillModel(items)

                if   curclss == Part:
                    
                    self.PartsList .itemSelectionChanged.disconnect()
                    self.PartsList.clear()
                    self.PartsList .itemSelectionChanged.connect(self.PartsSelectionChanged)

                    for part in items:
                        self.PartsList.addItem(part.Name)

                elif curclss == Stave:

                    self.StavesList.clear()
                    
                    #self.StavesTable.setRowCount(0)
                    for stave in items:
                        self.StavesList.addItem(stave.Name)

                elif curclss == Note:

                    self.NotesList.clear()

                    #list1 = [1, 2, 3]
                    #list2 = ['a', 'b', 'c']

                    #for item1, item2 in zip(list1, list2):
                    #    print(item1, item2)

                    for i, note in zip(range(0, len(items)), items):
                        self.NotesList.addItem(f"{note.Column}: {note.Fxl} {note.Pos} {note.Pow}")
                        #self.NotesList.insertItem(0, ")")

                    #self.NotesList.addItem("(")
                    #self.NotesList.insertItem(0, ")")

                if not empty:
                    if curclss != Score:
                        obj.Index = curind

                    curmap.PosModel(curind)

                    if  (curclss == Part ):
                        self.PartsList .setCurrentRow(curind)

                    elif(curclss == Stave):
                        self.StavesList.setCurrentRow(curind)

                    elif(curclss == Note ):
                        self.NotesList .setCurrentRow(curind)

            if not empty:
                obj = items[curind] if curind != -1 else None
                if curclss != Note :
                    items  = obj.Items
                    curind = int(obj.Index)

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
            #print(f"{curstave.Name}")

            curstrcount = self.StavesTable.rowCount()
            self.StavesTable.insertRow(curstrcount)
            self.StavesTable.setRowHeight(curstrcount, CELL_SIZE)

            item = QtWidgets.QTableWidgetItem(curstave.Name)
            self.StavesTable.setVerticalHeaderItem(curstrcount, item)


            #item = self.StavesTable.verticalHeaderItem(curstrcount)
            #item.setText(stave.Name)
            #self.StavesTable.setCurrentCell(currow, curind)

            #item = QtWidgets.QTableWidgetItem("O")
            #item.setTextAlignment(QtCore.Qt.AlignVCenter)
            #item.setBackground(QtGui.QColor(255, 0, 0))  # Красный фон
            #item.setTextAlignment(QtCore.Qt.AlignVCenter)
            #item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable)  # Разрешаем редактирование
            #self.StavesTable.setItem(pos, 0, item)


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

                #print(f"  {curnote.Column}")

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
        self.Position(Stave, False, row)

        curscore = self.Score[0]
        curpart  = curscore.Items[curscore.Index]
        curstave = curpart .Items[curpart .Index]

        ind = -1
        curind = -1
        for curnote in curstave.Items:
            curind += 1
            curcol = int(curnote.Column)
            if col == curcol:
                ind = curind
                break
        
        self.Position(Note, False, ind)


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

    def PrintDivider(self):
        print("------------------------------------------")

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

            # Сохранение XML с отступами и переносами строк
            with open("Score.xml", "w") as xml_file:
                xml_file.write(prettify(xscore))            
            break


    def updateModel(self, m, a, w):
        items = self.Score
        for curmap in self.Maps.values():
            index = curmap.Mapper.currentIndex()
            obj = items[index]

            if curmap.Mapper != m:
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


    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        self.SaveScore()
        event.accept()


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


app = QtWidgets.QApplication([])
window = Window()
window.show()
app.exec_()
