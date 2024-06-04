import sys
from PySide6 import QtWidgets, QtCore, QtGui
from PIL import ImageGrab


class SnipWidget(QtWidgets.QWidget):
    def __init__(self, screen_geometry, scale_factor, main_app):
        super().__init__()
        self.screen_geometry = screen_geometry
        self.scale_factor = scale_factor
        self.main_app = main_app
        self.setGeometry(self.screen_geometry)
        self.setWindowTitle(' ')
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.setWindowOpacity(0.3)
        self.is_snipping = False
        QtWidgets.QApplication.setOverrideCursor(
            QtGui.QCursor(QtCore.Qt.CrossCursor)
        )
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.show()

    def paintEvent(self, event):
        if self.is_snipping:
            brush_color = (0, 0, 0, 0)
            lw = 0
            opacity = 0
        else:
            brush_color = (128, 128, 255, 128)
            lw = 3
            opacity = 0.3

        self.setWindowOpacity(opacity)
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor('black'), lw))
        qp.setBrush(QtGui.QColor(*brush_color))
        qp.drawRect(QtCore.QRectF(self.begin, self.end))

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Q:
            print('Quit')
            self.main_app.quit_all()
        event.accept()

    def mousePressEvent(self, event):
        self.begin = event.position().toPoint()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.position().toPoint()
        self.update()

    def mouseReleaseEvent(self, event):
        self.main_app.increment_num_snip()
        x1 = min(self.begin.x(), self.end.x()) * self.scale_factor + self.screen_geometry.x()
        y1 = min(self.begin.y(), self.end.y()) * self.scale_factor + self.screen_geometry.y()
        x2 = max(self.begin.x(), self.end.x()) * self.scale_factor + self.screen_geometry.x()
        y2 = max(self.begin.y(), self.end.y()) * self.scale_factor + self.screen_geometry.y()
        self.is_snipping = True
        self.repaint()
        QtWidgets.QApplication.processEvents()
        img = ImageGrab.grab(bbox=(x1, y1, x2, y2), all_screens=True)
        self.is_snipping = False
        self.begin, self.end = QtCore.QPoint(), QtCore.QPoint()
        self.repaint()
        QtWidgets.QApplication.processEvents()
        img_name = 'snip{}.png'.format(self.main_app.num_snip)
        img.save(img_name)
        print(img_name, 'saved')


class SnipApp(QtWidgets.QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.widgets = []
        self.num_snip = 0
        for screen in self.screens():
            screen_geometry = screen.geometry()
            scale_factor = screen.devicePixelRatio()
            widget = SnipWidget(screen_geometry, scale_factor, self)
            self.widgets.append(widget)
        print('Capture the screen...')
        print('Press q if you want to quit...')

    def quit_all(self):
        for widget in self.widgets:
            widget.close()
        self.quit()

    def increment_num_snip(self):
        self.num_snip += 1


if __name__ == '__main__':
    app = SnipApp(sys.argv)
    sys.exit(app.exec())
