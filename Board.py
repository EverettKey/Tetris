# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 17:46:01 2016

@author: Everett Key
"""
import sys
import random
from PySide import QtCore, QtGui

class Communicate(QtCore.QObject):
    
    msgToSB = QtCore.Signal(str)

class Board(QtGui.QFrame):
    board_width = 10
    board_height = 22
    speed = 300
    
    def __init__(self, parent):
        super(Board, self).__init__()
        
        self.timer = QtCore.QBasicTimer()
        self.isWaitingAfterLine = False
        self.cur_piece = Shape()
        self.next_piece = Shape()
        self.curX = 0
        self.curY = 0
        self.num_lines_removed = 0
        self.board = []
        
        self.setFocusPolicy(QtCore.Qt.StronFocus)
        self.is_started = False
        self.is_paused = False
        self.clear_board()
        
        self.c = Communicate()
        
        self.next_piece.set_random_shape()
        
    def shape_at(self, x, y):
    def set_shape_at(self, x, y, shape):
    def square_width(self):
    def start(self):
    def pause(self):
    def paint_event(self, event):
    def key_press_event(self, event):
    def timer_event(self, event):
    def clear_board(self):
    def drop_down(self):
    def one_line_down(self):
    def piece_dropped(self):
    def remove_full_lines(self):
    def new_piece(self):
    def tryMove(self, piece, newX, newY):
    def drawSquare(self, painter, x, y, shape):
    