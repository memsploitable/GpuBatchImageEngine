# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\myApps\mygit\GpuBatchImageEngine\BatchWizard.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BatchWizardDialog(object):
    def setupUi(self, BatchWizardDialog):
        BatchWizardDialog.setObjectName("BatchWizardDialog")
        BatchWizardDialog.resize(803, 494)
        BatchWizardDialog.setSizeGripEnabled(True)
        self.tabWidget = QtWidgets.QTabWidget(BatchWizardDialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 781, 461))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushAddImageButton = QtWidgets.QPushButton(self.tab)
        self.pushAddImageButton.setGeometry(QtCore.QRect(20, 370, 75, 23))
        self.pushAddImageButton.setObjectName("pushAddImageButton")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab)
        self.graphicsView.setGeometry(QtCore.QRect(510, 30, 256, 192))
        self.graphicsView.setObjectName("graphicsView")
        self.pushNextButton_1 = QtWidgets.QPushButton(self.tab)
        self.pushNextButton_1.setGeometry(QtCore.QRect(510, 410, 75, 23))
        self.pushNextButton_1.setObjectName("pushNextButton_1")
        self.pushCanceButton_1 = QtWidgets.QPushButton(self.tab)
        self.pushCanceButton_1.setGeometry(QtCore.QRect(600, 410, 75, 23))
        self.pushCanceButton_1.setObjectName("pushCanceButton_1")
        self.pushAddDirectoryButton = QtWidgets.QPushButton(self.tab)
        self.pushAddDirectoryButton.setGeometry(QtCore.QRect(120, 370, 80, 23))
        self.pushAddDirectoryButton.setObjectName("pushAddDirectoryButton")
        self.pushDeleteImageButton = QtWidgets.QPushButton(self.tab)
        self.pushDeleteImageButton.setGeometry(QtCore.QRect(220, 370, 75, 23))
        self.pushDeleteImageButton.setObjectName("pushDeleteImageButton")
        self.pushDeleteAllButton = QtWidgets.QPushButton(self.tab)
        self.pushDeleteAllButton.setGeometry(QtCore.QRect(320, 370, 75, 23))
        self.pushDeleteAllButton.setObjectName("pushDeleteAllButton")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(510, 10, 54, 12))
        self.label.setObjectName("label")
        self.pushExporeButton = QtWidgets.QPushButton(self.tab)
        self.pushExporeButton.setGeometry(QtCore.QRect(410, 370, 75, 23))
        self.pushExporeButton.setObjectName("pushExporeButton")
        self.pushHelpButton_1 = QtWidgets.QPushButton(self.tab)
        self.pushHelpButton_1.setGeometry(QtCore.QRect(690, 410, 75, 23))
        self.pushHelpButton_1.setObjectName("pushHelpButton_1")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(510, 230, 78, 12))
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(510, 250, 251, 91))
        self.textEdit.setObjectName("textEdit")
        self.tableImagesWidget = QtWidgets.QTableWidget(self.tab)
        self.tableImagesWidget.setGeometry(QtCore.QRect(10, 10, 481, 351))
        self.tableImagesWidget.setObjectName("tableImagesWidget")
        self.tableImagesWidget.setColumnCount(0)
        self.tableImagesWidget.setRowCount(0)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(BatchWizardDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(BatchWizardDialog)

    def retranslateUi(self, BatchWizardDialog):
        _translate = QtCore.QCoreApplication.translate
        BatchWizardDialog.setWindowTitle(_translate("BatchWizardDialog", "BatchWizard"))
        self.pushAddImageButton.setText(_translate("BatchWizardDialog", "AddImage"))
        self.pushNextButton_1.setText(_translate("BatchWizardDialog", "Next"))
        self.pushCanceButton_1.setText(_translate("BatchWizardDialog", "Cancel"))
        self.pushAddDirectoryButton.setText(_translate("BatchWizardDialog", "AddDirectory"))
        self.pushDeleteImageButton.setText(_translate("BatchWizardDialog", "Delete"))
        self.pushDeleteAllButton.setText(_translate("BatchWizardDialog", "DeleteAll"))
        self.label.setText(_translate("BatchWizardDialog", "ViewImage"))
        self.pushExporeButton.setText(_translate("BatchWizardDialog", "Explore"))
        self.pushHelpButton_1.setText(_translate("BatchWizardDialog", "Help"))
        self.label_2.setText(_translate("BatchWizardDialog", "ImageDetails:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("BatchWizardDialog", "1.Select Images>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  _translate("BatchWizardDialog", "2.Select Options>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3),
                                  _translate("BatchWizardDialog", "3.Output Configurations>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BatchWizardDialog = QtWidgets.QDialog()
    ui = Ui_BatchWizardDialog()
    ui.setupUi(BatchWizardDialog)
    BatchWizardDialog.show()
    sys.exit(app.exec_())

