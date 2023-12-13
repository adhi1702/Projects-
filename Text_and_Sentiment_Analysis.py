import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTextEdit
from PyQt5 import QtCore
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

def Sentiment_Analysis():
    url = entry_box.text()
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')
    text = ' '.join([p.get_text() for p in soup.find_all('p')])

    blob = TextBlob(text)
    global sentiment
    sentiment = blob.sentiment.polarity

    # Clear previous content and display sentiment analysis result
    content_display.clear()
    content_display.append(f"Sentiment Analysis Result: {sentiment}")

def content():
    url = entry_box.text()
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')
    global text_content
    text_content = ' '.join([p.get_text() for p in soup.find_all('p')])

    # Clear previous content and display fetched content
    content_display.clear()
    content_display.append(text_content)


def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('Sentiment Analysis')
    window.setGeometry(100, 100, 410, 600)

    layout = QVBoxLayout()

    label1 = QLabel('Paste URL:', window)
    layout.addWidget(label1)

    global entry_box
    entry_box = QLineEdit(window)
    entry_box.setFixedWidth(370)
    layout.addWidget(entry_box)

    button1 = QPushButton('Content', window)
    button1.clicked.connect(content)
    layout.addWidget(button1)

    label2 = QLabel('or', window)
    label2.setAlignment(QtCore.Qt.AlignHCenter)
    layout.addWidget(label2)

    button2 = QPushButton('Analyse', window)
    button2.clicked.connect(Sentiment_Analysis)
    layout.addWidget(button2)

    global content_display
    content_display = QTextEdit(window)
    layout.addWidget(content_display)

    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
