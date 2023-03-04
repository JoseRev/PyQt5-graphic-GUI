import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QPlainTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Inscritos por Pais'
        self.left = 50
        self.top = 100
        self.width = 550
        self.height = 160
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create Label Instrucciones
        labelI = QLabel(self)
        labelI.setText("Este programa convierte el .csv descargado de Forms y elimina al personal duplicado (por correo y nombre), asimismo muestra en pantalla la relacion por pais de gente inscrita en el seminario.")
        labelI.resize(500, 80)
        labelI.setWordWrap(True)
        labelI.move(20, 0)
        
        # Create Label Nombre Archivo
        labelN = QLabel(self)
        labelN.setText("Nombre de CSV")
        labelN.resize(100, 40)
        labelN.move(20, 80)


        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(140, 80)
        self.textbox.resize(380,40)
        
        
        # Multiline Label
        #labelM = QLabel(self)
        #labelM.setWordWrap(True)
        #labelM.setText("PANDAS")
        #labelM.resize(500, 500)
        #labelM.move(20, 160)

        # Multiline String
        s1="""
        uno
        dos tres
        cuatro cinco
        sies
        """
        
        # Multiline Text
        self.mLine = QPlainTextEdit(self)
        self.mLine.move(20, 160)
        self.mLine.resize(500, 500)
        self.mLine.setPlainText(s1)

        #
        
        # Create a button in the window
        self.button = QPushButton('Enter', self)
        self.button.move(200,120)
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
  
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())