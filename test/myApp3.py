from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        # widget = QLabel("Hello")
        # font = widget.font()
        # font.setPointSize(30)
        # widget.setFont(font)
        # widget.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        # widget = QLabel()
        # widget.setPixmap( QPixmap("hqdefault.jpg") )
        # widget.setScaledContents(True)

        # widget = QCheckBox()
        # # widget.setChecked(True)
        # # widget.setCheckState(Qt.PartiallyChecked)
        # widget.setTristate(True)
        # widget.stateChanged.connect(self.show_state)

        # widget = QComboBox()
        # widget.addItems(["teste1", "teste2", "teste3"])
        # widget.currentIndexChanged.connect( self.index_changed )
        # widget.currentIndexChanged[str].connect( self.text_changed )
        # widget.currentTextChanged.connect( self.text_changed )

        # widget = QListWidget()
        # widget.addItems(["bla1", "bla2", "bla3"])
        # widget.currentItemChanged.connect( self.item_changed )
        # widget.currentTextChanged.connect( self.text_changed )

        # widget = QLineEdit()
        # widget.setMaxLength(10)
        # widget.setPlaceholderText("Escreve ai")
        # # widget.setReadOnly(True)
        # widget.returnPressed.connect( self.return_pressed )
        # widget.selectionChanged.connect( self.selection_changed )
        # widget.textChanged.connect( self.text_changed)
        # widget.textEdited.connect( self.text_edited )

        # widget = QSpinBox()
        # widget.setMinimum(-10)
        # widget.setMaximum(50)
        # # widget.setPrefix("%")
        # widget.setSuffix("%")
        # widget.setSingleStep(10)
        # widget.valueChanged.connect( self.value_changed )
        # widget.valueChanged[str].connect( self.value_changed_str )

        # widget = QDoubleSpinBox()
        # # widget.setMinimum(-10)
        # # widget.setMaximum(50)
        # widget.setRange(-5, 10)
        # # widget.setPrefix("%")
        # widget.setSuffix("%")
        # widget.setSingleStep(0.2)
        # widget.valueChanged.connect( self.value_changed )
        # widget.valueChanged[str].connect( self.value_changed_str )

        # widget = QSlider()
        # widget.setRange(-10, 100)
        # widget.setSingleStep(0.5)
        # widget.valueChanged.connect( self.value_changed )
        # widget.sliderMoved.connect( self.slider_position )
        # widget.sliderPressed.connect( self.slider_pressed )
        # widget.sliderReleased.connect( self.slider_released )

        widget = QDial()
        widget.setRange(-10, 100)
        widget.setSingleStep(0.5)
        widget.valueChanged.connect( self.value_changed )
        widget.sliderMoved.connect( self.slider_position )
        widget.sliderPressed.connect( self.slider_pressed )
        widget.sliderReleased.connect( self.slider_released )
        

        self.setCentralWidget(widget)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released!")

    def slider_position( self, p):
        print("position", p)

    def value_changed(self, i):
        print(i)
        
    def value_changed_str(self, s):
        print(s)

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("surpriseee")

    def item_changed(self, i):
        print(i.text())

    def index_changed(self, i):
        print(i)

    def text_edited(self, i):
        print("Text edited..")
        print(i)

    def text_changed(self, i):
        print("Text changed...")
        print(i)

    def show_state(self, s):
        print( s == Qt.Checked)
        print(s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()