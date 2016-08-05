# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 17:46:01 2016

@author: Everett Key
"""
import sys
import random
from PySide import QtCore, QtGui
from Game import Game
from Board import Board

class Communicate(QtCore.QObject):
    
    msgToSB = QtCore.Signal(str)

def main():
    app = QtGui.QApplication(sys.agv)
    game = Game()
    game.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
