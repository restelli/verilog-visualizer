import PyQt4.QtCore
from PyQt4.QtGui import *

from graphics_view import GraphicsView as GV
from graphics_scene import GraphicsScene as GS
from box import Box

class GraphicsWidget (QWidget):


    def __init__(self, view = None, scene = None):
        QWidget.__init__(self, None)
        if view is None:
            self.view = GV(self)
        else:
            self.view = view

        if scene is None:
            self.scene = GS(self.view, self)
        else:
            self.scene = scene
        self.view.setScene(self.scene)
        self.prevPoint = PyQt4.QtCore.QPoint()
        layout = QHBoxLayout()
        layout.addWidget(self.view)
        self.setLayout(layout)
        self.controller = None

    def fit_view(self):
        self.view._scale_fit()

    def add_box(self, name, color = "black", position = PyQt4.QtCore.QPointF(0, 0)):
        b = Box(position = position,
            scene = self.scene,
            name = name,
            color = color)
        return b

    #Controller Functions
    def set_controller(self, controller):
        self.controller = controller

    def get_controller(self):
        return self.controller

    def drop_event(self, event):
        #Send an event to a controller
        print "Demo Graphics View: Drop Event"



