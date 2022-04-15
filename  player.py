#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 02:09:34 2022

@author: entropy
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt, QUrl, QEvent
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineSettings, QWebEngineView

class YoutubePlayer(QWidget):
    def __init__(self, video_id, parent = None):
        super().__init__()
        self.parent = parent
        


class PlayerWindow(QWidget):
    def __int__(self):
        super().__init__()
        self.setWindowTitle('Reproductor')
        self.setWindowLogo('./fotos/images.png')
        self.setMiniumSize(1200, 800)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        
        
if __name__ == 'player':
    app = QApplication(sys.argv)
    
    window = PlayerWindow()
    window.show()
    
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print(' ')