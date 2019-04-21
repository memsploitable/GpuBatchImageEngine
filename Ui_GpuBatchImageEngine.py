# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\myApps\mygit\GpuBatchImageEngine\GpuBatchImageEngine.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(517, 260)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 517, 23))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuBatch = QtWidgets.QMenu(self.menuBar)
        self.menuBatch.setObjectName("menuBatch")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionImportImage = QtWidgets.QAction(MainWindow)
        self.actionImportImage.setObjectName("actionImportImage")
        self.actionPreference = QtWidgets.QAction(MainWindow)
        self.actionPreference.setObjectName("actionPreference")
        self.actionBatchWizard = QtWidgets.QAction(MainWindow)
        self.actionBatchWizard.setObjectName("actionBatchWizard")
        self.actionRA = QtWidgets.QAction(MainWindow)
        self.actionRA.setObjectName("actionRA")
        self.actionBA = QtWidgets.QAction(MainWindow)
        self.actionBA.setObjectName("actionBA")
        self.actionca = QtWidgets.QAction(MainWindow)
        self.actionca.setObjectName("actionca")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionImportImage)
        self.menuFile.addAction(self.actionPreference)
        self.menuBatch.addAction(self.actionBatchWizard)
        self.menuHelp.addAction(self.actionRA)
        self.menuHelp.addAction(self.actionBA)
        self.menuHelp.addAction(self.actionca)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuBatch.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GpuBatchImageEngine"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuBatch.setTitle(_translate("MainWindow", "Batch"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionImportImage.setText(_translate("MainWindow", "ImportImage"))
        self.actionPreference.setText(_translate("MainWindow", "Preference"))
        self.actionBatchWizard.setText(_translate("MainWindow", "BatchWizard"))
        self.actionRA.setText(_translate("MainWindow", "RA"))
        self.actionBA.setText(_translate("MainWindow", "BA"))
        self.actionca.setText(_translate("MainWindow", "ca"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

