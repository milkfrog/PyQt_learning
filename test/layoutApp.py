from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

class Color(QWidget):

    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        # layout1 = QVBoxLayout()
        # layout2 = QHBoxLayout()
        # # layout1.setContentsMargins(0,0,0,0)
        # layout1.setSpacing(20)
        # layout1.addWidget( Color('red') )
        # layout1.addWidget( Color('green') )
        # layout1.addLayout(layout2)
        # layout1.addWidget( Color('blue') )
        # layout2.addWidget( Color('yellow'))
        # layout2.addWidget( Color('grey'))
        # layout2.addWidget( Color('black'))

        # layout = QGridLayout(
        # layout.addWidget( Color('red'), 0, 0)
        # layout.addWidget( Color('green'), 10, 10)

        # pageLayout = QVBoxLayout()
        # button_layout = QHBoxLayout()
        # layout = QStackedLayout()

        # pageLayout.addLayout(button_layout)
        # pageLayout.addLayout(layout)

        # for n, color in enumerate(['red', 'green', 'blue', 'yellow']):      
        #     btn = QPushButton( str(color) )
        #     btn.pressed.connect( lambda n=n: layout.setCurrentIndex(n) )
        #     button_layout.addWidget( btn )
        #     layout.addWidget( Color(str(color)) )
    

        tabs = QTabWidget()
        tabs.setDocumentMode(True)
        tabs.setTabPosition(QTabWidget.East)
        tabs.setMovable(True)

        for n, color in enumerate(['red', 'green', 'blue', 'yellow']):      
            tabs.addTab( Color(color), color)


        # widget = QWidget()
        # widget.setLayout(pageLayout)
        # widget.setLayout(layout1)


        self.setCentralWidget(tabs)




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()