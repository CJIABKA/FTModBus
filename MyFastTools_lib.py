#!/usr/bin/env python
# -*- coding: utf-8 -*-        
#from MyControllers_lib import Signal, VirtualSignal
#from MyFastToolsDisp_lib import *
#from MyFunctions import GiveMeLoopName

class FastTools(object):    
    u'''Фаст тулс )'''
    ProcAreas = 0
    ACKN_TYPE = "PROCESS_ACK"
    COL_GROUP = "ALL_ITEMS"    
    def __init__(self, Device):
        self.Device = Device
        self.__class__.ProcAreas += 1
        self.ProcArea = self.ProcAreas
        
        self.Sections = [self.Device.Name.upper()]
        self.AOIs = []
        
        self.CMD_i_Rows = []
        self.CMD_r_Rows = []
        self.CMD_m_Rows = []
        self.CMD_iH_Rows = []
        self.CMD_rH_Rows = []
        self.LineRows = []
        self.COMstatusRows = []
        self.StationRows = []
        self.SectionsRows = []
        self.AOIRows = []

        self.AIdisplay = []
        self.AISCCdisplay = []
        self.DIdisplay = []
        self.VALVEdisplay = []
        self.ENGINEdisplay = []
        self.OTdisplay = []
        self.PIDdisplay = []
        self.DOdisplay = []

        self.LabelsForTrend = []

        self.PointRows = ['@LANGUAGE\n', \
                          'ENGLISH\n', \
                          '!===========================================================================================================\n', \
                          '@FIELDS\n', \
                          'NAME,DESCRIPTION,IO_ADDRESS,EXTERNAL_RELATION,SCAN_TYPE\n', \
                          'CONV_TYPE,BITS,HAS_SIGN,SWAP_BYTES,SWAP_WORDS\n', \
                          'FLOAT_TYPE,ELEC_LOW,ELEC_HIGH,PHYS_LOW,PHYS_HIGH\n', \
                          '@MODBUS_POINT_DF\n']
                          
        self.ItemtRows = ['@LANGUAGE\n', \
                          'ENGLISH\n', \
                          '!===========================================================================================================\n', \
                          '@FIELDS\n', \
                          'NAME,DESCRIPTION,COMMENT_1,COMMENT_2,ENG_UNIT,VALUE_FORMAT,ITEM_REP\n', \
                          'POINT_NAME,ALARMING,STORAGE,OPC_VISIBLE,OPC_READ,OPC_WRITE,SCALE_LOW_LIMIT,SCALE_HIGH_LIMIT\n', \
                          'ACKN_TYPE, COL_GROUP,PROCESS_LIST,HIGH_HIGH_LIMIT,HIGH_LIMIT,LOW_LIMIT,LOW_LOW_LIMIT\n', \
                          'ITEM_STAT_1,ITEM_STAT_2,ITEM_STAT_3,ITEM_STAT_4,ITEM_STAT_5,ITEM_STAT_6\n', \
                          'ALARM_STATE_1,ALARM_STATE_2,ALARM_STATE_3,ALARM_STATE_4,ALARM_STATE_5,ALARM_STATE_6\n', \
                          'PRIORITY_1,PRIORITY_2,PRIORITY_3,PRIORITY_4,PRIORITY_5,PRIORITY_6\n', \
                          'ALARM_TEXT_1,ALARM_TEXT_2,ALARM_TEXT_3,ALARM_TEXT_4,ALARM_TEXT_5,ALARM_TEXT_6\n', \
                          'ALARM_COLOR_1,ALARM_COLOR_2,ALARM_COLOR_3,ALARM_COLOR_4,ALARM_COLOR_5,ALARM_COLOR_6\n', \
                          'MNEMONIC_1,MNEMONIC_2,MNEMONIC_3,MNEMONIC_4,MNEMONIC_5,MNEMONIC_6\n', \
                          'SHELVE_ENABLED_1,SHELVE_ENABLED_2,SHELVE_ENABLED_3,SHELVE_ENABLED_4,SHELVE_ENABLED_5,SHELVE_ENABLED_6\n', \
                          'AOI_1,AOI_2,AOI_3,AOI_4,AOI_5,AOI_6\n', \
                          'AOI_7,AOI_8,AOI_9,AOI_10,AOI_11,AOI_12\n', \
                          'AOI_13,AOI_14,AOI_15,AOI_16\n', \
                          '@ITEM_DF\n']

        self.HystRows = ['@LANGUAGE\n', \
                         'ENGLISH\n', \
                         '!===========================================================================================================\n', \
                         '@FIELDS\n', \
                         'NAME,TYPE,COL_STOR_TYPE,ROLLOVER_INT,LIFE_TIME,PRIORITY,DATA_COMP,STORE_QUALITY,SCAN_INTERVAL\n', \
                         '@HIS_GROUP_DF\n', \
                         '"EVENT_BOOL","Item","Event/Event","1 days","31 days",15,1,1,0\n\n', \
                         '"EVENT_REAL","Item","Scan/Time","1 days","31 days",15,1,0,1\n\n', \
                         '!===========================================================================================================\n', \
                         '@FIELDS\n', \
                         'NAME,STORE_VALUE,ON_VALUE_CHANGE,ON_STATUS_CHANGE\n',\
                         '@ITEM_HIS_DF\n']
        
        self.Points = {}
        self.Items = {}
        
        self.MakeLineFile()
        self.MakeCOMstatusFile()
        self.MakeStationFile()
        self.MakePointsAndItems()
        
        self.MakeSectionsFile()
        self.MakeAOIfile()
        self.MakeCMDfiles()

    def MakeCMDfiles(self):    
        self.CMD_i_Rows.append('echo off\n')
        self.CMD_i_Rows.append('COPY /Y Displays\*.* "%TLS_ALLUSERS_PATH%\wap\cfg\operatorInterfaces\DEPLOY\displays"\n')
        self.CMD_i_Rows.append('dssqld -i ' + self.LineName + ' -l\n')
        self.CMD_i_Rows.append('attrib *.qlo -R\n')
        self.CMD_i_Rows.append('del *.qlo\n')
        self.CMD_i_Rows.append('dssqld -i "Sections.qli" -l\n')
        self.CMD_i_Rows.append('dssqld -i "AOIs.qli" -l\n')
        self.CMD_i_Rows.append('dssqld -i "COMstatus.qli" -l\n')
        self.CMD_i_Rows.append('dssqld -i "Station.qli" -l\n')
        self.CMD_i_Rows.append('dssqld -i "Points.qli" -l\n')
        self.CMD_i_Rows.append('dssqld -i "Items.qli" -l\n')
        self.CMD_i_Rows.append('Exit\n')                
        
        self.CMD_r_Rows.append('attrib *.qlo -R\n')
        self.CMD_r_Rows.append('del *.qlo\n')
        self.CMD_r_Rows.append('dssqld -r "History.qli" -l\n')
        self.CMD_r_Rows.append('dssqld -r "Items.qli" -l\n')
        self.CMD_r_Rows.append('dssqld -r "Points.qli" -l\n')
        self.CMD_r_Rows.append('dssqld -r "Station.qli" -l\n')
        self.CMD_r_Rows.append('dssqld -r "COMstatus.qli" -l\n')
        self.CMD_r_Rows.append('dssqld -r "AOIs.qli" -l\n')  
        self.CMD_r_Rows.append('dssqld -r "Sections.qli" -l\n') 
        self.CMD_r_Rows.append('dssqld -r ' + self.LineName + ' -l\n')
        self.CMD_r_Rows.append('Exit\n')

        self.CMD_m_Rows.append('attrib *.qlo -R\n')
        self.CMD_m_Rows.append('del *.qlo\n')
        self.CMD_m_Rows.append('dssqld -m "Points.qli" -l\n')
        self.CMD_m_Rows.append('dssqld -m "Items.qli" -l\n')
        self.CMD_m_Rows.append('Exit\n')

        self.CMD_iH_Rows.append('attrib *.qlo -R\n')
        self.CMD_iH_Rows.append('del *.qlo\n')
        self.CMD_iH_Rows.append('dssqld -i "History.qli" -l\n')
        self.CMD_iH_Rows.append('Exit\n')

        self.CMD_rH_Rows.append('attrib *.qlo -R\n')
        self.CMD_rH_Rows.append('del *.qlo\n')
        self.CMD_rH_Rows.append('dssqld -r "History.qli" -l\n')
        self.CMD_rH_Rows.append('Exit\n')
    
    def MakeSectionsFile(self):
        CreatedSections = []
        self.SectionsRows.append('@LANGUAGE\n')
        self.SectionsRows.append('ENGLISH\n')
        self.SectionsRows.append('!==================================================================================================================================\n')
        self.SectionsRows.append('@FIELDS\n')
        self.SectionsRows.append('NAME,OPC_VISIBLE\n')
        self.SectionsRows.append('@SECTION_DF\n')
        for sections in self.Sections:
            section = ''
            for sect in sections.split('.'):
                section = section + (sect if section == '' else '.' + sect)
                if section not in CreatedSections:
                    self.SectionsRows.append('"' + section + '",1\n')
                    CreatedSections.append(section)
                    
    def MakeAOIfile(self):
        CreatedAOIs = []
        self.AOIRows.append('@LANGUAGE\n')
        self.AOIRows.append('ENGLISH\n')
        self.AOIRows.append('!==================================================================================================================================\n')
        self.AOIRows.append('@FIELDS\n')
        self.AOIRows.append('NAME,DESCRIPTION\n')        
        self.AOIRows.append('@ALARM_AOI_DF\n')
        for AOI in self.AOIs:
            if AOI not in CreatedAOIs:
                self.AOIRows.append('"' + AOI + '","' + AOI + '"\n')
                CreatedAOIs.append(AOI)
    
    def MakeLineFile(self):
        self.LineName = 'EQP' + self.Device.Name.upper()
        self.LineRows.append('@LANGUAGE\n')
        self.LineRows.append('ENGLISH\n')
        self.LineRows.append('!==================================================================================================================================\n')
        self.LineRows.append('@FIELDS\n')
        self.LineRows.append('NAME,EQUIPMENT_MAN\n')
        self.LineRows.append('\n')
        self.LineRows.append('@MODBUS_LINE_DF\n')
        self.LineRows.append('"' + str(self.LineName) + '","' + str(self.LineName) + '"\n')
        self.LineRows.append('\n')
        self.LineRows.append('!==================================================================================================================================\n')
        self.LineRows.append('@FIELDS\n')
        self.LineRows.append('NAME,SCAN_INTERVAL\n')
        self.LineRows.append('\n')
        self.LineRows.append('@MODBUS_SCAN_TYPE_DF\n')
        self.LineRows.append('"SCAN_1000ms",1000')
        
    def MakeCOMstatusFile(self):        
        self.COMstatus   = 'STATIONS.COMMUNICATION.' + str(self.Device.Name).upper()
        self.COMstatusL1 = 'STATIONS.COMMUNICATION.' + str(self.Device.Name).upper() + '_L1'
        self.COMstatusL2 = 'STATIONS.COMMUNICATION.' + str(self.Device.Name).upper() + '_L2'
        self.Sections.append('STATIONS.COMMUNICATION')
        self.COMstatusRows.append('@LANGUAGE\n')
        self.COMstatusRows.append('ENGLISH\n')
        self.COMstatusRows.append('!==================================================================================================================================\n')
        self.COMstatusRows.append('@FIELDS\n')
        self.COMstatusRows.append('NAME,DESCRIPTION,ITEM_REP,ACKN_TYPE,COL_GROUP,ALARMING,OPC_VISIBLE,OPC_READ,OPC_WRITE\n')
        self.COMstatusRows.append('ITEM_STAT_1,ITEM_STAT_2,ALARM_STATE_1,ALARM_STATE_2,PRIORITY_1,PRIORITY_2,ALARM_COLOR_1,ALARM_COLOR_2,MNEMONIC_1,MNEMONIC_2\n')
        self.COMstatusRows.append('ALARM_TEXT_1,ALARM_TEXT_2\n')
        self.COMstatusRows.append('@ITEM_DF\n')
        self.COMstatusRows.append('"' + self.COMstatus + '","Статус связи","Boolean","' + self.ACKN_TYPE + '","' + self.COL_GROUP + '","1","1","1","0",\\\n')
        self.COMstatusRows.append('"BOOLEAN 1","BOOLEAN 0","Normal","Alarm 1","0","1","limegreen","red","NR","ALR",\\\n')
        self.COMstatusRows.append('"Связь в норме","Нет связи"\n')
        self.COMstatusRows.append('\n')
        self.COMstatusRows.append('"' + self.COMstatusL1 + '","статус 1 линии связи","Boolean","' + self.ACKN_TYPE + '","' + self.COL_GROUP + '","1","1","1","0",\\\n')
        self.COMstatusRows.append('"BOOLEAN 1","BOOLEAN 0","Normal","Alarm 1","0","1","limegreen","red","NR","ALR",\\\n')
        self.COMstatusRows.append('"' + str(self.Device.Name) + ' 1 линия связи в норме","' + str(self.Device.Name) + ' отказ 1 линии связи"\n')
        self.COMstatusRows.append('\n')
        self.COMstatusRows.append('"' + self.COMstatusL2 + '","статус 2 линии связи","Boolean","' + self.ACKN_TYPE + '","' + self.COL_GROUP + '","1","1","1","0",\\\n')
        self.COMstatusRows.append('"BOOLEAN 1","BOOLEAN 0","Normal","Alarm 1","0","1","limegreen","red","NR","ALR",\\\n')
        self.COMstatusRows.append('"' + str(self.Device.Name) + ' 2 линия связи в норме","' + str(self.Device.Name) + ' отказ 2 линии связи"\n')
        
    def MakeStationFile(self):
        self.StationRows.append('@LANGUAGE\n')
        self.StationRows.append('ENGLISH\n')
        self.StationRows.append('!==================================================================================================================================\n')
        self.StationRows.append('@FIELDS\n')
        self.StationRows.append('NAME,DESCRIPTION,LINE\n')
        self.StationRows.append('STATUS_ITEM,LINE_1_ITEM,LINE_2_ITEM\n')
        self.StationRows.append('@MODBUS_STATION_DF\n')
        self.StationRows.append('"' + str(self.Device.Name).upper() + '","","' + self.LineName + '",\\\n')
        self.StationRows.append('"' + self.COMstatus + '","' + self.COMstatusL1 + '","' + self.COMstatusL2 + '"\n')
        
    def MakePoint(self, Point, Description, Address, Conversion, Bits = 16,Sign = 0, SwapB = 0, SwapW = 0):
        self.PointRows.append('"' + Point + '","' + Description + '","' + str(Address) + '","Input + Output","SCAN_1000ms",\\\n')
        self.PointRows.append('"' + Conversion + '","' + str(Bits) + '","' + str(Sign) + '","' + str(SwapB) + '","' + str(SwapW) + '",\\\n')
        self.PointRows.append('"Intel","-1000000","1000000","-1000000","1000000"\n')
         
    def MakeItem(self, Frow, Srow = {}, Trow = {}, ALR = {}, AOIs = ['']):
        IT_ST = ['']*6
        AL_ST = ['']*6
        PRIOR = ['']*6
        AL_TXT = ['']*6
        AL_CLR = ['']*6
        MNEM = ['']*6
        SH_EN = ['']*6                
        for i in range(len(ALR)):
            IT_ST[i]  = ALR[i]['IT_ST']
            AL_ST[i]  = ALR[i]['AL_ST']
            PRIOR[i]  = ALR[i]['PRIOR']                
            AL_CLR[i] = ALR[i]['AL_CLR']
            MNEM[i]   = ALR[i]['MNEM']
            SH_EN[i]  = ALR[i]['SH_EN']                
            if type(ALR[i]['AL_TXT']) == unicode:
                AL_TXT[i] = ALR[i]['AL_TXT'].encode('utf-8')
            elif type(ALR[i]['AL_TXT']) == str:
                AL_TXT[i] = ALR[i]['AL_TXT']            
        
        aoi = ['']*16
        for i in range(len(AOIs)):
            aoi[i] = AOIs[i]
            
        frow = ['']*7
        frow[0] = Frow['Name']        if Frow.get('Name')        else 'DUMBitem'
        frow[1] = Frow['Description'] if Frow.get('Description') else ''
        frow[2] = Frow['Com_1']       if Frow.get('Com_1')       else ''
        frow[3] = Frow['Com_2']       if Frow.get('Com_2')       else ''
        frow[4] = Frow['EU']          if Frow.get('EU')          else ''
        frow[5] = Frow['V_format']    if Frow.get('V_format')    else ''
        frow[6] = Frow['It_repr']     if Frow.get('It_repr')     else 'Boolean'
        
        srow = ['']*8
        srow[0] = Srow['P_Name']  if Srow.get('P_Name')   else ''
        srow[1] = '1' if len(ALR)>0 else ''
        srow[2] = Srow['Storage'] if Srow.get('Storage')  else '0'
        srow[3] = Srow['OPC_Vis'] if Srow.get('OPC_Vis')  else '1'
        srow[4] = Srow['OPC_Rd']  if Srow.get('OPC_Rd')   else '1'
        srow[5] = Srow['OPC_Wt']  if Srow.get('OPC_Wt')   else '0'
        srow[6] = Srow['SL']      if Srow.get('SL')       else ''
        srow[7] = Srow['SH']      if Srow.get('SH')       else ''
        
        trow = ['']*7
        trow[0] = Trow['ACKN_TYPE']    if Trow.get('ACKN_TYPE')    else self.ACKN_TYPE
        trow[1] = Trow['COL_GROUP']    if Trow.get('COL_GROUP')    else self.COL_GROUP
        trow[2] = Trow['PROCESS_LIST'] if Trow.get('PROCESS_LIST') else str(self.ProcArea)
        trow[3] = Trow['HH']           if Trow.get('HH')           else ''
        trow[4] = Trow['H']            if Trow.get('H')            else ''
        trow[5] = Trow['L']            if Trow.get('L')            else ''
        trow[6] = Trow['LL']           if Trow.get('LL')           else ''
        
        self.ItemtRows.append('"{}","{}","{}","{}","{}","{}","{}",\\\n'.format(frow[0], frow[1], frow[2], frow[3], frow[4], frow[5], frow[6] ) )              #NAME,  DESCRIPTION,  COMMENT_1,  COMMENT_2,  ENG_UNIT,  VALUE_FORMAT,  ITEM_REP  
        self.ItemtRows.append('"{}","{}","{}","{}","{}","{}","{}","{}",\\\n'.format(srow[0], srow[1], srow[2], srow[3], srow[4], srow[5], srow[6], srow[7]) ) #POINT_NAME,  ALARMING,  STORAGE,  OPC_VISIBLE,  OPC_READ,  OPC_WRITE,  SCALE_LOW_LIMIT,  SCALE_HIGH_LIMIT  
        self.ItemtRows.append('"{}","{}","{}","{}","{}","{}","{}",\\\n'.format(trow[0], trow[1], trow[2], trow[3], trow[4], trow[5], trow[6]) )               #ACKN_TYPE,   COL_GROUP,  PROCESS_LIST,  HIGH_HIGH_LIMIT,  HIGH_LIMIT,  LOW_LIMIT,  LOW_LOW_LIMIT
        
        self.ItemtRows.append('"{}","{}","{}","{}","{}","{}",\\\n'.format(IT_ST[0], IT_ST[1], IT_ST[2], IT_ST[3], IT_ST[4], IT_ST[5]))       #ITEM_STAT_1,  ITEM_STAT_2,  ITEM_STAT_3,  ITEM_STAT_4,  ITEM_STAT_5,  ITEM_STAT_6  
        self.ItemtRows.append('"{}","{}","{}","{}","{}","{}",\\\n'.format(AL_ST[0], AL_ST[1], AL_ST[2], AL_ST[3], AL_ST[4], AL_ST[5]))       #ALARM_STATE_1,  ALARM_STATE_2,  ALARM_STATE_3,  ALARM_STATE_4,  ALARM_STATE_5,  ALARM_STATE_6        
        self.ItemtRows.append('"{}","{}","{}","{}","{}","{}",\\\n'.format(PRIOR[0], PRIOR[1], PRIOR[2], PRIOR[3], PRIOR[4], PRIOR[5]))       #PRIORITY_1,  PRIORITY_2,  PRIORITY_3,  PRIORITY_4,  PRIORITY_5,  PRIORITY_6 
        self.ItemtRows.append('"{}","{}","{}","{}","{}","{}",\\\n'.format(AL_TXT[0], AL_TXT[1], AL_TXT[2], AL_TXT[3], AL_TXT[4], AL_TXT[5])) #ALARM_TEXT_1,  ALARM_TEXT_2,  ALARM_TEXT_3,  ALARM_TEXT_4,  ALARM_TEXT_5,  ALARM_TEXT_6  
        self.ItemtRows.append('"{}","{}","{}","{}","{}","{}",\\\n'.format(AL_CLR[0], AL_CLR[1], AL_CLR[2], AL_CLR[3], AL_CLR[4], AL_CLR[5])) #ALARM_COLOR_1,  ALARM_COLOR_2,  ALARM_COLOR_3,  ALARM_COLOR_4,  ALARM_COLOR_5,  ALARM_COLOR_6  
        self.ItemtRows.append('"{}","{}","{}","{}","{}","{}",\\\n'.format(MNEM[0], MNEM[1], MNEM[2], MNEM[3], MNEM[4], MNEM[5]))             #MNEMONIC_1,  MNEMONIC_2,  MNEMONIC_3,  MNEMONIC_4,  MNEMONIC_5,  MNEMONIC_6  
        self.ItemtRows.append('"{}","{}","{}","{}","{}","{}",\\\n'.format(SH_EN[0], SH_EN[1], SH_EN[2], SH_EN[3], SH_EN[4], SH_EN[5]))       #SHELVE_ENABLED_1,  SHELVE_ENABLED_2,  SHELVE_ENABLED_3,  SHELVE_ENABLED_4,  SHELVE_ENABLED_5,  SHELVE_ENABLED_6  
        
        self.ItemtRows.append('"{}","{}","{}","{}","{}","{}",\\\n'.format(aoi[0], aoi[1], aoi[2], aoi[3], aoi[4], aoi[5]))   #AOI_1,  AOI_2,  AOI_3,  AOI_4,   AOI_5,   AOI_6  
        self.ItemtRows.append('"{}","{}","{}","{}","{}","{}",\\\n'.format(aoi[6], aoi[7], aoi[8], aoi[9], aoi[10], aoi[11])) #AOI_7,  AOI_8,  AOI_9,  AOI_10,  AOI_11,  AOI_12
        self.ItemtRows.append('"{}","{}","{}","{}"\n'.format(aoi[12], aoi[13], aoi[14], aoi[15]))                            #AOI_13, AOI_14, AOI_15, AOI_16
        self.ItemtRows.append('\n')

        if frow[6] == 'Boolean':
            self.HystRows.append('"EVENT_BOOL:' + str(frow[0]) + '",1,1,1\n\n')
        else:
            self.HystRows.append('"EVENT_REAL:' + str(frow[0]) + '",1,0,0\n\n')
        
    def PaIforSignal(self, signal, section, aois = []):
        Frow = {}
        Srow = {}
        Trow = {}
        
        AOIs = aois[:]
            
        signal.Point = signal.Tag.upper() + '_POINT'
        self.Points[signal.Point] = signal
        
        if signal.Description:
            Comment_1 = signal.Description[:20]
            Comment_2 = signal.Description[20:40]
            Description = signal.Description[:40]
        else:
            Description = ''
            Comment_1 = ''
            Comment_2 = ''

        if '|' in signal.Description:
            Comment_1, Comment_2 = signal.Description.split('|')
            Comment_1 = Comment_1.strip()
            Comment_2 = Comment_2.strip()
            Description = Comment_1 + ' ' + Comment_2
        

        if max(abs(float(signal.SH )), abs(float(signal.SL)))>0:
            Value_Format = '9.999'
        if max(abs(float(signal.SH )), abs(float(signal.SL)))>10:
            Value_Format = '99.99'
        if max(abs(float(signal.SH )), abs(float(signal.SL)))>100:
            Value_Format = '999.9'
        if max(abs(float(signal.SH )), abs(float(signal.SL)))>1000:
            Value_Format = '9999'
        
        if signal.Unit:
            Eng_Un = signal.Unit[:3]
        else:
            Eng_Un = '' 
            
        if signal.AOI_1:
            AOIs.append(signal.AOI_1)
        if signal.AOI_2:
            AOIs.append(signal.AOI_2)
        if signal.AOI_3:
            AOIs.append(signal.AOI_3)
        if signal.AOI_4:
            AOIs.append(signal.AOI_4)
        if signal.AOI_5:
            AOIs.append(signal.AOI_5)
        if signal.AOI_6:
            AOIs.append(signal.AOI_6)
        if signal.AOI_7:
            AOIs.append(signal.AOI_7)
        if signal.AOI_8:
            AOIs.append(signal.AOI_8)
        if signal.AOI_9:
            AOIs.append(signal.AOI_9)
        if signal.AOI_10:
            AOIs.append(signal.AOI_10)
        if signal.AOI_11:
            AOIs.append(signal.AOI_11)
        if signal.AOI_12:
            AOIs.append(signal.AOI_12)
        if signal.AOI_13:
            AOIs.append(signal.AOI_13)
        if signal.AOI_14:
            AOIs.append(signal.AOI_14)
        if signal.AOI_15:
            AOIs.append(signal.AOI_15)
        if signal.AOI_16:
            AOIs.append(signal.AOI_16)

        for aoi in AOIs:
            if aoi not in self.AOIs:
                self.AOIs.append(aoi)
        
        if section not in self.Sections:
            self.Sections.append(section)

        Point = str(self.Device.Name).upper() + ':' + str(signal.Point)

        if signal.MBType == 'COIL':
            Address = 'DO:' + signal.IOAdress
        elif signal.MBType == 'DSCI':
            Address = 'DI:' + signal.IOAdress
        elif signal.MBType == 'HREG':
            Address = 'RO:' + signal.IOAdress
        elif signal.MBType == 'IREG':
            Address = 'RI:' + signal.IOAdress

        if signal.DataType == 'Bool' or signal.DataType == 'Boolean':
            Conversion = 'Digital'
            Bits = 16
            Representation = 'Boolean'
        elif signal.DataType == 'Int' or signal.DataType == 'Integer':
            Conversion = 'Linear'
            Bits = 16
            Representation = 'Integer'
        elif signal.DataType == 'Float':
            Conversion = 'Float'
            Bits = 32
            Representation = 'Real'

        self.MakePoint(Point, Description, Address, Conversion, Bits, signal.Sign, signal.SWB, signal.SWW)

        signal.Item = section + '.' + str(signal.Tag)
        self.Items[signal.Item] = signal
        Frow['Name']        = signal.Item
        Frow['Description'] = Description
        Frow['Com_1']       = Comment_1
        Frow['Com_2']       = Comment_2
        Frow['EU']          = Eng_Un
        Frow['V_format']    = Value_Format  
        Frow['It_repr']     = Representation
        
        Srow['P_Name']  = Point  
        Srow['SL']      = signal.SL if signal.SL else ''
        Srow['SH']      = signal.SH if signal.SH else ''

        Trow['HH'] = signal.HH if signal.HH else ''
        Trow['H']  = signal.HI if signal.HI else ''
        Trow['L']  = signal.LO if signal.LO else ''
        Trow['LL'] = signal.LL if signal.LL else ''

        self.MakeItem(Frow, Srow, Trow, signal.Alarming, AOIs)

    def MakePointsAndItems(self):
        for signal in self.Device.Signals:
            if not signal.Tag:
                continue
            section = str(self.Device.Name).upper() + ('.' + signal.Section) if signal.Section else ''
            self.PaIforSignal(signal, section, [])

