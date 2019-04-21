# -*- coding: utf-8 -*-

#
#
# Created by: borlittle 2019/4/21
#
#


from PyQt5 import QtWidgets

from Common import *
from Ui_GpuBatchImageEngine import Ui_MainWindow
from BatchWizardDialog import BatchWizardDialog


class GpuBatchImageEngine(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(GpuBatchImageEngine, self).__init__(parent)
        # Important variables

        self.setupUi(self)
        self.initEvents()

        logger.info('Program init over.')

    def initEvents(self):
        self.actionBatchWizard.triggered.connect(self.loadBatchWizard)

    def setGui(self):
        pass

    ##########UI event actions
    def loadBatchWizard(self):
        self.batchWizard = BatchWizardDialog()
        self.batchWizard.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myshow = GpuBatchImageEngine()
    myshow.show()

    sys.exit(app.exec_())
