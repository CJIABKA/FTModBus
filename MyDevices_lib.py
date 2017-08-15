#!/usr/bin/env python
# -*- coding: utf-8 -*-
from MyFunctions import ReplaceCirilic

class Device(object):
    Data = None
    Name = u'None'
    def __init__(self, Name, Data):
        #print Name,Data
        self.Name = ReplaceCirilic(Name).encode('utf8').strip()
        self.Data = Data
        self.Signals = []
        for attr in Data:
            self.Signals.append(Signal(attr))

class Signal(object):
    u'''Signal from XLS'''
    IOAdress = '1'
    MBType = 'COIL'
    DataType = 'Bool'
    SWB = 0
    SWW = 0
    Sign = 1
    Tag = None
    Description = None
    Unit = None
    SL = 0
    SH = 100
    LL = None
    LO = None
    HI = None
    HH = None
    Section = None
    Alarming = []
    AOI_1 = None
    AOI_2 = None
    AOI_3 = None
    AOI_4 = None
    AOI_5 = None
    AOI_6 = None
    AOI_7 = None
    AOI_8 = None
    AOI_9 = None
    AOI_10 = None
    AOI_11 = None
    AOI_12 = None
    AOI_13 = None
    AOI_14 = None
    AOI_15 = None
    AOI_16 = None

    def __init__(self, Attributes):
        u'''Создаем  asdf с переданными аттрибутами'''
        for attr, value in Attributes.items():
            self.__dict__[attr] = value

        self.CheckData()

    def CheckData(self):
        if self.Tag:
            self.Tag = ReplaceCirilic(self.Tag).encode('utf8').strip()
            if self.Tag == '':
                self.Tag == None

        if self.Description:
            if type(self.Description) == unicode:
                self.Description = self.Description.encode('utf8').strip()
            if self.Description == '':
                self.Description = None

        if self.Unit:
            if type(self.Unit) == unicode:
                self.Unit = self.Unit.encode('utf8').strip()
            if self.Unit == '':
                self.Unit = None

        if self.IOAdress:
            if type(self.IOAdress) == unicode:
                self.IOAdress = self.IOAdress.encode('utf8').strip()
            elif type(self.IOAdress) == int:
                self.IOAdress = str(self.IOAdress)
            elif type(self.IOAdress) == float:
                self.IOAdress = str(self.IOAdress).split('.')[0]
        if not self.IOAdress or self.IOAdress == '':
            self.IOAdress = '1'

        if self.Section:
            if type(self.Section) == unicode:
                self.Section = self.Section.encode('utf8').strip()
            if self.Section == '':
                self.Section = None

        if self.Alarming:
            if type(self.Alarming) == unicode:
                self.Alarming = self.Alarming.encode('utf8').strip().lower()
            if self.Alarming == '':
                self.Alarming = []
        if self.Alarming == 'bool':
            self.Alarming = [{'IT_ST':'BOOLEAN 0', 'AL_ST':'Normal', 'PRIOR':'0', 'AL_CLR':'gray', 'MNEM':'NR', 'SH_EN':'', 'AL_TXT': u'0'},
                             {'IT_ST':'BOOLEAN 1', 'AL_ST':'Normal', 'PRIOR':'0', 'AL_CLR':'green', 'MNEM':'NR', 'SH_EN':'', 'AL_TXT': u'1'}]
        elif self.Alarming == 'sensdino':
            self.Alarming = [{'IT_ST':'BOOLEAN 0', 'AL_ST':'Normal', 'PRIOR':'0', 'AL_CLR':'green', 'MNEM':'NR', 'SH_EN':'', 'AL_TXT': u'В норме'},
                             {'IT_ST':'BOOLEAN 1', 'AL_ST':'Alarm 1', 'PRIOR':'1', 'AL_CLR':'red', 'MNEM':'ALR', 'SH_EN':'', 'AL_TXT': u'Авария'}]
        elif self.Alarming == 'sensdinc':
            self.Alarming = [{'IT_ST':'BOOLEAN 0', 'AL_ST':'Alarm 1', 'PRIOR':'1', 'AL_CLR':'red', 'MNEM':'ALR', 'SH_EN':'', 'AL_TXT': u'Авария'},
                             {'IT_ST':'BOOLEAN 1', 'AL_ST':'Normal', 'PRIOR':'0', 'AL_CLR':'green', 'MNEM':'NR', 'SH_EN':'', 'AL_TXT': u'В норме'}]
        elif self.Alarming == 'sensai':
            self.Alarming = [{'IT_ST':'OPEN INPUT+', 'AL_ST':'Alarm 1', 'PRIOR':'1', 'AL_CLR':'cyan',   'MNEM':'IOP+', 'SH_EN':'', 'AL_TXT': u'КЗ'},
                             {'IT_ST':'OPEN INPUT-', 'AL_ST':'Alarm 1', 'PRIOR':'1', 'AL_CLR':'cyan',   'MNEM':'IOP-', 'SH_EN':'', 'AL_TXT': u'Обрыв'},
                             {'IT_ST':'HIGH HIGH',   'AL_ST':'Alarm 3', 'PRIOR':'2', 'AL_CLR':'red',    'MNEM':'HH',   'SH_EN':'', 'AL_TXT': u'Верхний аварийный порог'},
                             {'IT_ST':'HIGH',        'AL_ST':'Alarm 2', 'PRIOR':'3', 'AL_CLR':'yellow', 'MNEM':'HI',   'SH_EN':'', 'AL_TXT': u'Верхний предупредительный порог'},
                             {'IT_ST':'LOW',         'AL_ST':'Alarm 2', 'PRIOR':'3', 'AL_CLR':'yellow', 'MNEM':'LO',   'SH_EN':'', 'AL_TXT': u'Нижний предупредительный порог'},
                             {'IT_ST':'LOW LOW',     'AL_ST':'Alarm 3', 'PRIOR':'2', 'AL_CLR':'red',    'MNEM':'LL',   'SH_EN':'', 'AL_TXT': u'Нижний аварийный порог'}]
        else:
            self.Alarming = []

        if self.MBType:
            if type(self.MBType) == unicode:
                self.MBType = self.MBType.encode('utf8').strip().upper()
        if not self.MBType or self.MBType == '':
            self.MBType = 'COIL'

        if self.DataType:
            if type(self.DataType) == unicode:
                self.DataType = self.DataType.encode('utf8').strip().capitalize()
        if not self.DataType or self.DataType == '':
            self.DataType = 'Bool'

        if self.SWB:
            if type(self.SWB) == unicode:
                self.SWB = self.SWB.encode('utf8').strip().lower()
            if self.SWB == '':
                self.SWB = 0
        if self.SWB == 'true' or self.SWB == 't':
            self.SWB == 1
        elif self.SWB == 'false' or self.SWB == 'f':
            self.SWB == 0
        else:
            try:
                self.SWB = int(self.SWB)
            except:
                self.SWB = 0

        if self.SWW:
            if type(self.SWW) == unicode:
                self.SWW = self.SWW.encode('utf8').strip().lower()
            if self.SWW == '':
                self.SWW = 0
        if self.SWW == 'true' or self.SWW == 't':
            self.SWW == 1
        elif self.SWW == 'false' or self.SWW == 'f':
            self.SWW == 0
        else:
            try:
                self.SWW = int(self.SWW)
            except:
                self.SWW = 0

        if self.Sign:
            if type(self.Sign) == unicode:
                self.Sign = self.Sign.encode('utf8').strip().lower()
            if self.Sign == '':
                self.Sign = 1
        if self.Sign == 'true' or self.Sign == 't':
            self.Sign == 1
        elif self.Sign == 'false' or self.Sign == 'f':
            self.Sign == 0
        else:
            try:
                self.Sign = int(self.Sign)
            except:
                self.Sign = 1

        if self.SL:
            if type(self.SL) == unicode:
                self.SL = self.SL.encode('utf8').strip().replace(',','.')
            elif type(self.SL) == str:
                self.SL = self.SL.strip().replace(',','.')
            try:
                self.SL = float(self.SL)
            except:
                self.SL = 0
        else:
            self.SL = 0

        if self.SH:
            if type(self.SH) == unicode:
                self.SH = self.SH.encode('utf8').strip().replace(',','.')
            elif type(self.SH) == str:
                self.SH = self.SH.strip().replace(',','.')
            try:
                self.SH = float(self.SH)
            except:
                self.SH = 100
        else:
            self.SH = 100

        if self.HH:
            if type(self.HH) == unicode:
                self.HH = self.HH.encode('utf8').strip().replace(',','.')
            elif type(self.HH) == str:
                self.HH = self.HH.strip().replace(',','.')
            try:
                self.HH = float(self.HH)
            except:
                self.HH = None

        if self.HI:
            if type(self.HI) == unicode:
                self.HI = self.HI.encode('utf8').strip().replace(',','.')
            elif type(self.HI) == str:
                self.HI = self.HI.strip().replace(',','.')
            try:
                self.HI = float(self.HI)
            except:
                self.HI = None

        if self.LO:
            if type(self.LO) == unicode:
                self.LO = self.LO.encode('utf8').strip().replace(',','.')
            elif type(self.LO) == str:
                self.LO = self.LO.strip().replace(',','.')
            try:
                self.LO = float(self.LO)
            except:
                self.LO = None

        if self.LL:
            if type(self.LL) == unicode:
                self.LL = self.LL.encode('utf8').strip().replace(',','.')
            elif type(self.LL) == str:
                self.LL = self.LL.strip().replace(',','.')
            try:
                self.LL = float(self.LL)
            except:
                self.LL = None

        if self.AOI_1:
            self.AOI_1 = ReplaceCirilic(self.AOI_1).encode('utf8').strip()
            if self.AOI_1 == '':
                self.AOI_1 == None

        if self.AOI_2:
            self.AOI_2 = ReplaceCirilic(self.AOI_2).encode('utf8').strip()
            if self.AOI_2 == '':
                self.AOI_2 == None

        if self.AOI_3:
            self.AOI_3 = ReplaceCirilic(self.AOI_3).encode('utf8').strip()
            if self.AOI_3 == '':
                self.AOI_3 == None

        if self.AOI_4:
            self.AOI_4 = ReplaceCirilic(self.AOI_4).encode('utf8').strip()
            if self.AOI_4 == '':
                self.AOI_4 == None

        if self.AOI_5:
            self.AOI_5 = ReplaceCirilic(self.AOI_5).encode('utf8').strip()
            if self.AOI_5 == '':
                self.AOI_5 == None

        if self.AOI_6:
            self.AOI_6 = ReplaceCirilic(self.AOI_6).encode('utf8').strip()
            if self.AOI_6 == '':
                self.AOI_6 == None

        if self.AOI_7:
            self.AOI_7 = ReplaceCirilic(self.AOI_7).encode('utf8').strip()
            if self.AOI_7 == '':
                self.AOI_7 == None

        if self.AOI_8:
            self.AOI_8 = ReplaceCirilic(self.AOI_8).encode('utf8').strip()
            if self.AOI_8 == '':
                self.AOI_8 == None

        if self.AOI_9:
            self.AOI_9 = ReplaceCirilic(self.AOI_9).encode('utf8').strip()
            if self.AOI_9 == '':
                self.AOI_9 == None

        if self.AOI_10:
            self.AOI_10 = ReplaceCirilic(self.AOI_10).encode('utf8').strip()
            if self.AOI_10 == '':
                self.AOI_10 == None

        if self.AOI_11:
            self.AOI_11 = ReplaceCirilic(self.AOI_11).encode('utf8').strip()
            if self.AOI_11 == '':
                self.AOI_11 == None

        if self.AOI_12:
            self.AOI_12 = ReplaceCirilic(self.AOI_12).encode('utf8').strip()
            if self.AOI_12 == '':
                self.AOI_12 == None

        if self.AOI_13:
            self.AOI_13 = ReplaceCirilic(self.AOI_13).encode('utf8').strip()
            if self.AOI_13 == '':
                self.AOI_13 == None

        if self.AOI_14:
            self.AOI_14 = ReplaceCirilic(self.AOI_14).encode('utf8').strip()
            if self.AOI_14 == '':
                self.AOI_14 == None

        if self.AOI_15:
            self.AOI_15 = ReplaceCirilic(self.AOI_15).encode('utf8').strip()
            if self.AOI_15 == '':
                self.AOI_15 == None

        if self.AOI_16:
            self.AOI_16 = ReplaceCirilic(self.AOI_16).encode('utf8').strip()
            if self.AOI_16 == '':
                self.AOI_16 == None

