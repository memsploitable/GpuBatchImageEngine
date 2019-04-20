# -*- coding: utf-8 -*-

#
#
# Created by: borlittle 2019/4/21
#
#

import sys
from PyQt5 import QtWidgets
from Ui_GpuBatchImageEngine import Ui_MainWindow


class GpuBatchImageEngine(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(GpuBatchImageEngine, self).__init__(parent)
        self.setupUi(self)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myshow = GpuBatchImageEngine()
    myshow.show()

    sys.exit(app.exec_())
