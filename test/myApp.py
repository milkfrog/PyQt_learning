from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

class MainWindow(QMainWindow):

    my_awesome_signal = pyqtSignal(str)
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # self.windowTitleChanged.connect( lambda x: self.my_custom_fn(x, 10))

        self.setWindowTitle("My Awesome App")

        # label = QLabel("THIS IS AWESOME!!!")
        # label.setAlignment(Qt.AlignCenter)
        # self.setCentralWidget(label)

        # layout = QHBoxLayout()
        # for n in range(10):
        #     btn = QPushButton(str(n))
        #     btn.pressed.connect( lambda n=n: self.my_custom_fn(n) )
        #     layout.addWidget(btn)
        # widget = QWidget()
        # widget.setLayout(layout)

        button = QPushButton("HELLO!")
        button.pressed.connect( self.pushed_my_button )

        self.my_awesome_signal.connect( self.caught_my_own_signal )
        self.setCentralWidget(button)
        # self.setCentralWidget(label)

    def contextMenuEvent(self, e): # clicar com o botão direito do mouse
        print("Context menu requested!")

        super(MainWindow, self).contextMenuEvent(e)

    def pushed_my_button(self):
        print("Pressed it!")
        self.my_awesome_signal.emit("WOAH")

    def caught_my_own_signal(self, s):
        print(s)

    # def onWindowTitleChange(self, s):
    #     print(s)

    # def my_custom_fn(self, a):
    #     print(a)
    
app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT!!!

app.exec_()