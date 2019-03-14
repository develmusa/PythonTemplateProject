import sys
from PyQt5.QtWidgets import QApplication, QWidget

def app():
    my_app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("Example")
    w.show()
    #Let the application Infinit Loop 
    sys.exit(my_app.exec_())  

app()