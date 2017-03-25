#!/usr/bin/python

'''
Program ot read the xls file.


'''

import xlrd

workbook=xlrd.open_workbook('/home/hrushi/sample.xls')


for sheet in workbook.sheets():
    print "The name of the sheet is :{}" .format(sheet.name)
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            print "Row:{} Coloumn :{} has value :{}" .format(row,col,sheet.cell_value(row,col))
