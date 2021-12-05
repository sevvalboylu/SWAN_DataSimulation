from pandas import *
from xlrd import open_workbook
from xlrd.timemachine import xrange


def read(file):
    book = open_workbook(file)
    sheet = book.sheet_by_index(0)

    # read header values into the list
    keys = [sheet.cell(0, col_index).value for col_index in xrange(sheet.ncols)]
    dict_list = []
    for row_index in xrange(1, sheet.nrows):
        d = {keys[col_index]: sheet.cell(row_index, col_index).value
             for col_index in xrange(sheet.ncols)}
        dict_list.append(d)
    return dict_list

def readLinks():
    read('links.xlsx')

def readFiles():
    i = read('interactive.xlsx')
    e = read('elastic.xlsx')
    b = read('background.xlsx')
    return i, e, b

# readFiles()