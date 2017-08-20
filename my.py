#!/usr/bin/env python
# encoding: utf-8

class Read() :
    def __init__(self,num) :
        self.num = int(num)
        self.sumup = 0

    def sum_up(self) :
    	pass

    def print_it(self) :
    	pass

    def change(self) :
    	pass

if __name__ == '__main__' :
    number = Read(input("输入一个尽可能长的数字\n"))
    number.sum_up()
    number.print_it()
    number.change()