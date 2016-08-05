# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 17:46:01 2016

@author: Everett Key
"""
import sys
import rando
from PySide import QtCore, QtGui
from Board import Board

class Game(QtGui.QMainWindow):
    def __init__(self):
        super(Game, self).__init__()
        
        self.setGeometry(300, 300, 180, 380)
        self.setWindowTitle("TETRIS")
        
        self.board = Baord(self)
        self.setCentralWidget(self.board)
        
        self.statusbar = self.statusBar()
        
        self.center_window()
        self.board.start()
        
    # Move the window to the center of the computer screen
    def center_window(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        window = self.geometry()
        self.move((screen.width() - window.width()) / 2,
                  (screen.height()- window.height()) /2)