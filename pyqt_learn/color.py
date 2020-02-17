#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QFrame, QApplication)
from PyQt5.QtGui import QColor


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        # 色の初期設定（黒にする）
        self.col = QColor(0, 0, 0)       

        # 赤用トグルボタンの作成
        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10, 10)

        # クリックされたらsetColor関数の呼び出し
        redb.clicked.connect(self.setColor)

        # 緑用トグルボタンの作成
        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)

        greenb.clicked[bool].connect(self.setColor)

        # 青用トグルボタンの作成
        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)

        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %  
            self.col.name())

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle button')
        self.show()


    def setColor(self, pressed):

        # 押されたボタンをsource変数に代入
        source = self.sender()      

        # ボタンがクリックされたら、色を設定
        if pressed:
            val = 255
        else: val = 0

        # Redボタンが押されたら、色に赤を混ぜる
        if source.text() == "Red":
            self.col.setRed(val)    
        # Greenボタンが押されたら、色に緑を混ぜる            
        elif source.text() == "Green":
            self.col.setGreen(val)   
        # Blueボタンが押されたら、色に青を混ぜる
        else:
            self.col.setBlue(val) 

        # 色を変える
        self.square.setStyleSheet("QFrame { background-color: %s }" %
            self.col.name())  


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
