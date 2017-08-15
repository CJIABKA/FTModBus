#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd

class XLSbase(object):
    Data = {}
    def __init__(self, filepath):
        rb = xlrd.open_workbook(filepath)
        for sheet in rb.sheets():
            self.GetDataFromXLS(sheet)

    def GetDataFromXLS(self, sheet):
        ColNames = []
        Device = sheet.name
        params = []
        for column in range(sheet.ncols):
            ColName = sheet.cell_value(0, column).encode('utf8').strip() if sheet.cell_value(0, column) else ''
            ColNames.append(ColName)

        for row in range(1, sheet.nrows):
            param = {}
            for column in range(sheet.ncols):
                value = sheet.cell_value(row,column)
                param[ColNames[column]] = value
            params.append(param)

        self.Data[Device] = params

    def SayWhatYouHave(self):
        for k,v in self.Data.items():
            print k
            for s in range(len(v)):
                print s
                for kk, vv in v[s].items():
                    print kk,vv

if __name__ == "__main__":
    testXLS = XLSbase('C:\\Temp\\Buf.xls')
    testXLS.SayWhatYouHave()