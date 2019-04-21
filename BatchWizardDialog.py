# -*- coding: utf-8 -*-

#
#
# Created by: borlittle 2019/4/21
#
#


from PyQt5 import QtWidgets
from PyQt5 import QtGui

from Common import *
from Ui_BatchWizard import Ui_BatchWizardDialog


class BatchWizardDialog(QtWidgets.QDialog, Ui_BatchWizardDialog):
    def __init__(self, parent=None):
        super(BatchWizardDialog, self).__init__(parent)
        self.setupUi(self)
        logger.info('BatchWizard init over.')


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    BatchWizardDialog = QtWidgets.QDialog()
    ui = Ui_BatchWizardDialog()
    ui.setupUi(BatchWizardDialog)
    BatchWizardDialog.show()
    sys.exit(app.exec_())
