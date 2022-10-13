from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import math

# This class sets up the graphics of the main scene in the app

class QDMGraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)

        # settings

        # Colors of elements
        self._color_background = QColor("#fbf6f5")
        self.color_grid_light = QColor("#cccccc")
        self.color_grid_dark = QColor("#aaaaaa")

        self._pen_grid_light = QPen(self.color_grid_light)
        self._pen_grid_dark = QPen(self.color_grid_dark)

        # Width of GridPens
        self._pen_grid_light.setWidth(1)
        self._pen_grid_dark.setWidth(2)

        self.grid_size = 20
        self.grid_square=4



        # Sets up the rect which contains the scene

        self.scene_width, self.scene_height = 64000, 64000
        self.setSceneRect(-self.scene_width // 2, -self.scene_height // 2, self.scene_width // 2,
                          self.scene_height // 2)

        # sets the background color
        self.setBackgroundBrush(self._color_background)

    # function that dras the background and grid
    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)

        # grid creation
        left = int(math.floor(rect.left()))
        right = int(math.ceil(rect.right()))
        top = int(math.floor(rect.top()))
        bottom = int(math.ceil(rect.bottom()))

        first_left = left - (left % self.grid_size)
        first_top = top - (top % self.grid_size)

        # compute lines to be drawn
        lines_grid_light= []
        lines_grid_dark=[]
        for x in range(first_left, right, self.grid_size):
            if x%(self.grid_size*self.grid_square) !=0:
                lines_grid_light.append(QLine(x, top, x, bottom))
            else:
                lines_grid_dark.append(QLine(x,top,x,bottom))

        for y in range(first_top, bottom, self.grid_size):
            if y%(self.grid_size*self.grid_square) !=0:
                lines_grid_light.append(QLine(left, y, right, y))
            else:
                lines_grid_dark.append(QLine(left,y,right,y))

        # draw lines
        painter.setPen(self._pen_grid_light)
        painter.drawLines(*lines_grid_light)  # this star means that it takes each indivisual element of an array as a parameter
        painter.setPen(self._pen_grid_dark)
        painter.drawLines(*lines_grid_dark)
