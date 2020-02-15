from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

import os
import os.path
import urllib.request
from PyQt5.uic import loadUiType

ui,_ = loadUiType('main.ui')

class MainApp(QMainWindow , ui):
    def __init__(self , parent=None):
        super(MainApp , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.InitUI()
        self.Handle_Button()


    def InitUI(self):
        ## contains all the ui changes in the loading
        pass

    def Handle_Button(self):
        ## handle all buttons in the app
        self.pushButton.clicked.connect(self.Download)
        self.pushButton_2.clicked.connect(self.Handle_Browse)

    def Handle_progress(self, blocknum, blocksize, totalsize):
        ## calculate the progress
        read_data = blocknum * blocksize

        if totalsize > 0:
            download_percentage = read_data * 100 / totalsize
            self.progressBar.setValue(download_percentage)
            QApplication.processEvents()

    def Handle_Browse(self):
        ##  enable browsing to our os, pick save loaction
        save_location = QFileDialog.getSaveFileName(self, caption="Save As", directory=".", filter="All Files(*.*)")
        print(save_location)
        self.lineEdit_2.setText(str(save_location[0]))

    def Download(self):
        ## downloading any files
        print("Starting Download")

        download_url = self.lineEdit.text()
        save_location = self.lineEdit_2.text()

        if download_url == '' or save_location == '':
            QMessageBox.warning(self, "Data Error", "Prove a valid URL or save location")
        else:
            try:
                urllib.request.urlretrieve(download_url, save_location, self.Handle_progress)
            except Exception:
                QMessageBox.warning (self, "Download Error", "Prove a valid URL or save location")
                return

        QMessageBox.information(self, "Download Completed", "The Download Completed Successfully")

        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.progressBar.setValue(0)



    def Save_Browse(self):
        ## save location in line edit
        pass

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
