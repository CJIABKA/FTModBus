#!/usr/bin/env python
# -*- coding: utf-8 -*-
from MyXLS import XLSbase
from MyDevices_lib import Device
from MyFastTools_lib import FastTools
import os
import xlwt

class Project(object):
    u'''Проект!! Здесь всё тело программы'''
    def __init__(self, BasePath, ProjectPath):
        self.Base = XLSbase(BasePath)
        self.ProjectPath = ProjectPath
        self.__CheckPath()
        self.Device_list = []
        self.FastTools_list = []
     
    def __CheckPath(self, Path = []): 
        u'''Проверяет путь указанный как "путь проекта" и если данная папка не создана - создаёт'''
        folders = self.ProjectPath.split('\\')
        folders = folders + Path
        path = ''
        for folder in folders:
            path = path + folder if path == '' else path + '\\' + folder
            if not os.path.exists(path):
                os.mkdir(path)    
        
    def MakeXLS(self, Path, Table, FileName):
        u'''Запись значений переданных в двумерном массиве в таблицу по указанному пути в папке проекта'''
        try:
            self.__CheckPath(Path)
            wb = xlwt.Workbook()
            sheets = Table.keys()
            sheets.sort(key = lambda x: x.split('|')[0])        
            for sheet in sheets:
                ws = wb.add_sheet(sheet.split('|')[1])
                count_row = 0            
                for row in Table[sheet]:  
                    count_column = 0
                    for column in row:
                        ws.write(count_row,count_column, column)    
                        count_column += 1
                    count_row += 1   
            Path.append(FileName)
            wb.save(self.ProjectPath + '\\' + '\\'.join(Path))    
        except Exception as ex:
            print u'Проблемы с записью файла Excel', Path, row,  ex
        
    def MakeTextFile(self, Path, Rows, FileName):
        u'''Запись строк переданных в списке в текстовый файл по указанному пути в папке проекта'''
        row = ''
        try:
            self.__CheckPath(Path)
            Path.append(FileName)
            f = open(self.ProjectPath + '\\' + '\\'.join(Path),'w')        
            for row in Rows:
                f.write(row)
            f.close()    
        except Exception as ex:
            print u'Проблемы с записью файла txt', Path, row,  ex
        
    def main(self):
        for Name, Data in self.Base.Data.items():
            #print Name, Data
            self.Device_list.append(Device(Name,Data))

        for device in self.Device_list:
            FT = FastTools(device)
            self.FastTools_list.append(FT)

            self.MakeTextFile([device.Name, 'FastTools'], FT.LineRows, FT.LineName + '.qli')
            self.MakeTextFile([device.Name, 'FastTools'], FT.COMstatusRows, 'COMstatus.qli')
            self.MakeTextFile([device.Name, 'FastTools'], FT.StationRows, 'Station.qli')
            self.MakeTextFile([device.Name, 'FastTools'], FT.SectionsRows, 'Sections.qli')
            self.MakeTextFile([device.Name, 'FastTools'], FT.AOIRows, 'AOIs.qli')

            self.MakeTextFile([device.Name, 'FastTools'], FT.PointRows, 'Points.qli')
            self.MakeTextFile([device.Name, 'FastTools'], FT.ItemtRows, 'Items.qli')
            self.MakeTextFile([device.Name, 'FastTools'], FT.HystRows, 'History.qli')

            self.MakeTextFile([device.Name, 'FastTools'], FT.CMD_i_Rows, '_NewTags.cmd')
            self.MakeTextFile([device.Name, 'FastTools'], FT.CMD_r_Rows, '_REMOVE_ALL.cmd')
            self.MakeTextFile([device.Name, 'FastTools'], FT.CMD_m_Rows, '_UpdateTags.cmd')
            self.MakeTextFile([device.Name, 'FastTools'], FT.CMD_iH_Rows, '_AddHistory.cmd')
            self.MakeTextFile([device.Name, 'FastTools'], FT.CMD_rH_Rows, '_RemoveHistory.cmd')