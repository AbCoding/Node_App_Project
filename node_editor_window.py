from PyQt5.QtWidgets import *
from node_graphics_scene import QDMGraphicsScene

# Creates the window which will run the program
class node_editor_window(QWidget):
    def __init__(self, parent=None):
        # extends Qwidget
        super().__init__(parent)
        self.initUI()
    # initalizes the User Interface of the program
    def initUI(self):
        # sets initial location and dimensions of the UI
        self.setGeometry(200, 200, 800, 600)
        self.layout=QVBoxLayout()
        self.setLayout(self.layout)

        # creates Graphic scene
        self.grScene= QDMGraphicsScene()



        # creates Graphic View

        self.view = QGraphicsView(self)
        self.view.setScene(self.grScene)
        self.layout.addWidget(self.view)
        self.setWindowTitle("Node Editor")

        self.show()
