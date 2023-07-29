from qt_material import apply_stylesheet
from PySide2.QtWidgets import QApplication
from ui.gui import TestWin

if __name__ == "__main__":
    app = QApplication([])
    apply_stylesheet(app, "light_blue.xml", invert_secondary=True)
    win = TestWin()
    win.ui.show()
    app.exec_()