import sys
import socket
import whois
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel, QTextEdit

class InfoGatheringTool(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        
        # Input field for domain or IP
        self.inputField = QLineEdit(self)
        self.inputField.setPlaceholderText('Enter domain or IP')
        
        # Buttons for different actions
        self.whoisButton = QPushButton('WHOIS Lookup', self)
        self.whoisButton.clicked.connect(self.performWhoisLookup)
        
        self.pingButton = QPushButton('Ping', self)
        self.pingButton.clicked.connect(self.performPing)
        
        self.publicIpButton = QPushButton('Get Public IP', self)
        self.publicIpButton.clicked.connect(self.getPublicIp)
        
        # Text area to display results
        self.resultArea = QTextEdit(self)
        self.resultArea.setReadOnly(True)

        layout.addWidget(QLabel('Input:'))
        layout.addWidget(self.inputField)
        layout.addWidget(self.whoisButton)
        layout.addWidget(self.pingButton)
        layout.addWidget(self.publicIpButton)
        layout.addWidget(self.resultArea)
        
        self.setLayout(layout)
        self.setWindowTitle('Information Gathering Tool')
        self.show()

    def performWhoisLookup(self):
        domain = self.inputField.text()
        try:
            result = whois.whois(domain)
            self.resultArea.setPlainText(str(result))
        except Exception as e:
            self.resultArea.setPlainText(f"Error: {str(e)}")

    def performPing(self):
        target = self.inputField.text()
        try:
            response = os.system(f"ping -c 4 {target}")
            self.resultArea.setPlainText(f"Ping result:\n{response}")
        except Exception as e:
            self.resultArea.setPlainText(f"Error: {str(e)}")

    def getPublicIp(self):
        try:
            response = requests.get('https://api.ipify.org?format=json')
            data = response.json()
            self.resultArea.setPlainText(f"Your public IP is: {data['ip']}")
        except Exception as e:
            self.resultArea.setPlainText(f"Error: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InfoGatheringTool()
    sys.exit(app.exec_())
