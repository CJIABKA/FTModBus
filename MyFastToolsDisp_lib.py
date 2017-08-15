#!/usr/bin/env python
# -*- coding: utf-8 -*-
blankXML = """<?xml version="1.0" encoding="utf-8" ?>
<visualization protocolVersion="10.1.0.0">
  <globalSection/>
  <coreObjectDefinition type="displayDefinition">
    <version type="version" value="10.1.0.0"/>
    <width>0</width>
    <height>0</height>
    <referenceCheck>0</referenceCheck>
    <defaultBgColor type="colorSet" r="255" g="255" b="255"/>
    <defaultFgColor type="colorSet" r="0" g="0" b="0"/>
    <visibilityGroup type="componentData">
      <name>Overview</name>
      <description>Always shown</description>
      <minimumZoomEnabled>true</minimumZoomEnabled>
      <minimumZoomFactor>10.0</minimumZoomFactor>
    </visibilityGroup>
    <visibilityGroup type="componentData">
      <name>Rough</name>
      <description>Shown when viewing viewing a large area</description>
      <minimumZoomEnabled>true</minimumZoomEnabled>
      <minimumZoomFactor>25.0</minimumZoomFactor>
    </visibilityGroup>
    <visibilityGroup type="componentData">
      <name>Standard</name>
      <description>Shown when using the default view setting</description>
      <minimumZoomEnabled>true</minimumZoomEnabled>
      <minimumZoomFactor>100.0</minimumZoomFactor>
    </visibilityGroup>
    <visibilityGroup type="componentData">
      <name>Detail</name>
      <description>Shown only when viewing a small area</description>
      <minimumZoomEnabled>true</minimumZoomEnabled>
      <minimumZoomFactor>400.0</minimumZoomFactor>
    </visibilityGroup>
    <visibilityGroup type="componentData">
      <name>Intricacies</name>
      <description>Shown only when viewing a very small area</description>
      <minimumZoomEnabled>true</minimumZoomEnabled>
      <minimumZoomFactor>1000.0</minimumZoomFactor>
    </visibilityGroup>
    <grid type="grid" gridVisible="true" snappingActive="true" verticalSnapInterval="8" horizontalSnapInterval="8" onTop="false">
      <color type="colorSet" r="0" g="0" b="0"/>
    </grid>
    <revisionHistory type="revisionHistory">
      <revision type="revision" who="ENG" when="2016.03.31 08:38:43.589 CEST" what="Created" where="stardom-PC"/>
    </revisionHistory>
    <blinkDelay>500</blinkDelay>
    <visualizationLayer type="componentData">
      <name>Layer1</name>
    </visualizationLayer>
    <componentCountHint>0</componentCountHint>{}
  </coreObjectDefinition>
</visualization>
"""

dataField ="""      <data type="data">{}        
      </data>"""

actionField = """<action type="actionConnectTo">
          <property type="property" name="{0}"/>
          <filter type="filter">
            <value>0.0</value>
          </filter>
          <connection type="connection">
            <direction>1</direction>
            <itemName>{1}</itemName>{2}            
          </connection>
        </action>"""

Sens_AI = """<symbolInstance.Sens_AI type="componentData">
      <config type="graphicInfo"/>
      <x>{0}</x>
      <y>{1}</y>
      <top>0.0</top>
      <bottom>-0.0</bottom>
      <left>0.0</left>
      <right>-0.0</right>
      <property type="componentProperty">
        <name>SENS_NAME</name>
        <value>{2}</value>
      </property>
      <property type="componentProperty">
        <name>SENS_ENG_UNIT</name>
        <value>{3}</value>
      </property>
      <property type="componentProperty">
        <name>SENS_COM_FLT</name>
        <value type="itemName">
          <value>{4}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>SENS_PV</name>
        <value type="itemName">
          <value>{5}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>SENS_A</name>
        <value type="itemName">
          <value>{6}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>SENS_DB</name>
        <value type="itemName">
          <value>{7}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>SENS_DB_Have</name>
        <value>{8}</value>
      </property>
      <property type="componentProperty">
        <name>SENS_HH</name>
        <value type="itemName">
          <value>{9}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>SENS_HH_Have</name>
        <value>{10}</value>
      </property>
      <property type="componentProperty">
        <name>SENS_HI</name>
        <value type="itemName">
          <value>{11}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>SENS_HI_Have</name>
        <value>{12}</value>
      </property>      
      <property type="componentProperty">
        <name>SENS_LO</name>
        <value type="itemName">
          <value>{13}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>      
      <property type="componentProperty">
        <name>SENS_LO_Have</name>
        <value>{14}</value>
      </property>
      <property type="componentProperty">
        <name>SENS_LL</name>
        <value type="itemName">
          <value>{15}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>SENS_LL_Have</name>
        <value>{16}</value>
      </property>
      <property type="componentProperty">
        <name>SENS_AOF</name>
        <value>{17}</value>
      </property>
    </symbolInstance.Sens_AI>"""

Sens_DI = """<symbolInstance.Sens_DI type="componentData">
      <config type="graphicInfo"/>
      <x>{0}</x>
      <y>{1}</y>
      <top>0.0</top>
      <bottom>-0.0</bottom>
      <left>0.0</left>
      <right>-0.0</right>      
      <property type="componentProperty">
        <name>SENS_COM_FLT</name>
        <value type="itemName">
          <value>{2}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>SENS_BOOL</name>
        <value type="itemName">
          <value>{3}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>      
      <property type="componentProperty">
        <name>SENS_DB</name>
        <value type="itemName">
          <value>{4}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>SENS_DB_Have</name>
        <value>{5}</value>
      </property>
      <property type="componentProperty">
        <name>SENS_SCC</name>
        <value>{6}</value>
      </property>{7}
    </symbolInstance.Sens_DI>"""

Valve_01 = """<symbolInstance.Valve_01 type="componentData">
      <config type="graphicInfo"/>
      <scale>1.0</scale>
      <x>{0}</x>
      <y>{1}</y>
      <top>0.0</top>
      <bottom>-0.0</bottom>
      <left>0.0</left>
      <right>-0.0</right>      
      <property type="componentProperty">
        <name>Param_NamePosX</name>
        <value>0.0</value>
      </property>      
      <property type="componentProperty">
        <name>Param_NamePosY</name>
        <value>0.0</value>
      </property>  
      <property type="componentProperty">
        <name>Param_ObjectRotation</name>
        <value>0.0</value>
      </property>
      <property type="componentProperty">
        <name>Param_FP_Enable</name>
        <value>{2}</value>
      </property>      
      <property type="componentProperty">
        <name>VALVE_COM_FLT</name>
        <value type="itemName">
          <value>{3}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>      
      <property type="componentProperty">
        <name>VALVE_NAME</name>
        <value>{4}</value>
      </property>      
      <property type="componentProperty">
        <name>VALVE_COMMENT1</name>
        <value>{5}</value>
      </property>      
      <property type="componentProperty">
        <name>VALVE_COMMENT2</name>
        <value>{6}</value>
      </property>   
      <property type="componentProperty">
        <name>VALVE_CO</name>
        <value type="itemName">
          <value>{7}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>      
      <property type="componentProperty">
        <name>VALVE_CC</name>
        <value type="itemName">
          <value>{8}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>      
      <property type="componentProperty">
        <name>VALVE_CS</name>
        <value type="itemName">
          <value>{9}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>VALVE_CS_Have</name>
        <value>{10}</value>
      </property>      
      <property type="componentProperty">
        <name>VALVE_DB</name>
        <value type="itemName">
          <value>{11}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>      
      <property type="componentProperty">
        <name>VALVE_DB_have</name>
        <value>{12}</value>
      </property>      
      <property type="componentProperty">
        <name>VALVE_RP</name>
        <value type="itemName">
          <value>{13}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>       
      <property type="componentProperty">
        <name>VALVE_MODE_A</name>
        <value type="itemName">
          <value>{14}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>      
      <property type="componentProperty">
        <name>VALVE_MODE_M</name>
        <value type="itemName">
          <value>{15}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>Param_TypeModesChange</name>
        <value>{16}</value>
      </property>      
      <property type="componentProperty">
        <name>VALVE_SG_have</name>
        <value>{17}</value>
      </property> 
      <property type="componentProperty">
        <name>VALVE_SD_have</name>
        <value>{18}</value>
      </property>      
      <property type="componentProperty">
        <name>VALVE_SG</name>
        <value>false</value>
      </property>      
      <property type="componentProperty">
        <name>VALVE_SD</name>
        <value>false</value>
      </property>      
      <property type="componentProperty">
        <name>VALVE_CO_ALG</name>
        <value>false</value>
      </property>
      <property type="componentProperty">
        <name>VALVE_CC_ALG</name>
        <value>false</value>
      </property>      
      <property type="componentProperty">
        <name>VALVE_SO</name>
        <value>false</value>
      </property>      
      <property type="componentProperty">
        <name>VALVE_SC</name>
        <value>false</value>
      </property>
      <property type="componentProperty">
        <name>VALVE_SN</name>
        <value>false</value>
      </property> 
      <property type="componentProperty">
        <name>VALVE_NOPCL</name>
        <value>false</value>
      </property>
      <property type="componentProperty">
        <name>VALVE_PAZ</name>
        <value>false</value>
      </property>{19}
    </symbolInstance.Valve_01>"""

Engine_01 = """<symbolInstance.Engine_01 type="componentData">
      <config type="graphicInfo"/>
      <scale>1.0000002</scale>
      <x>{0}</x>
      <y>{1}</y>
      <top>0</top>
      <bottom>-0</bottom>
      <left>0</left>
      <right>-0</right>
      <property type="componentProperty">
        <name>Param_NamePosX</name>
        <value>0.0</value>
      </property>
      <property type="componentProperty">
        <name>Param_NamePosY</name>
        <value>0.0</value>
      </property>      
      <property type="componentProperty">
        <name>Param_tube_left_right</name>
        <value>false</value>
      </property>
      <property type="componentProperty">
        <name>Param_tube_up_down</name>
        <value>false</value>
      </property>       
      <property type="componentProperty">
        <name>Param_FAN</name>
        <value>{2}</value>
      </property>      
      <property type="componentProperty">
        <name>Param_FP_ENABLE</name>
        <value>{3}</value>
      </property>   
      <property type="componentProperty">
        <name>ENGINE_COM_FLT</name>
        <value type="itemName">
          <value>{4}</value>
          <dataName>item_df</dataName>         
        </value>
      </property>      
      <property type="componentProperty">
        <name>ENGINE_NAME</name>
        <value>{5}</value>
      </property>
      <property type="componentProperty">
        <name>ENGINE_COMMENT1</name>
        <value>{6}</value>
      </property>      
      <property type="componentProperty">
        <name>ENGINE_COMMENT2</name>
        <value>{7}</value>
      </property> 
      <property type="componentProperty">
        <name>ENGINE_CR</name>
        <value type="itemName">
          <value>{8}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>      
      <property type="componentProperty">
        <name>ENGINE_CS</name>
        <value type="itemName">
          <value>{9}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>ENGINE_DB</name>
        <value type="itemName">
          <value>{10}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>ENGINE_DB_have</name>
        <value>{11}</value>
      </property>
      <property type="componentProperty">      
        <name>ENGINE_RP</name>
        <value type="itemName">
          <value>{12}</value>
          <dataName>item_df</dataName>          
        </value>
      </property> 
      <property type="componentProperty">
        <name>ENGINE_MODE_A</name>
        <value type="itemName">
          <value>{13}</value>
          <dataName>item_df</dataName>         
        </value>
      </property>      
      <property type="componentProperty">
        <name>ENGINE_MODE_M</name>
        <value type="itemName">
          <value>{14}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>Param_TypeModesChange</name>
        <value>{15}</value>
      </property>
      <property type="componentProperty">
        <name>ENGINE_SG_have</name>
        <value>{16}</value>
      </property>
      <property type="componentProperty">
        <name>ENGINE_SD_have</name>
        <value>{17}</value>
      </property>
      <property type="componentProperty">
        <name>ENGINE_SG</name>
        <value>false</value>
      </property> 
      <property type="componentProperty">
        <name>ENGINE_SD</name>
        <value>false</value>
      </property>    
      <property type="componentProperty">
        <name>ENGINE_CR_ALG</name>
        <value>false</value>
      </property>      
      <property type="componentProperty">
        <name>ENGINE_CS_ALG</name>
        <value>false</value>
      </property> 
      <property type="componentProperty">
        <name>ENGINE_SW</name>
        <value>false</value>
      </property>
      <property type="componentProperty">
        <name>ENGINE_SN</name>
        <value>false</value>
      </property>
      <property type="componentProperty">
        <name>ENGINE_NRS</name>
        <value>false</value>
      </property>
      <property type="componentProperty">
        <name>Engine_PAZ</name>
        <value>false</value>
      </property>{18}
    </symbolInstance.Engine_01>"""

Mixer_01 = """<symbolInstance.Mixer_01 type="componentData">
      <config type="graphicInfo"/>
      <x>{0}</x>
      <y>{1}</y>
      <top>0.0</top>
      <bottom>-0.0</bottom>
      <left>0.0</left>
      <right>-0.0</right>
      <property type="componentProperty">
        <name>Param_NamePosX</name>
        <value>0.0</value>
      </property>
      <property type="componentProperty">
        <name>Param_NamePosY</name>
        <value>0.0</value>
      </property>   
      <property type="componentProperty">
        <name>Param_ObjectRotation</name>
        <value>0.0</value>
      </property>       
      <property type="componentProperty">
        <name>Param_FP_ENABLE</name>
        <value>{2}</value>
      </property>   
      <property type="componentProperty">
        <name>ENGINE_COM_FLT</name>
        <value type="itemName">
          <value>{3}</value>
          <dataName>item_df</dataName>         
        </value>
      </property>      
      <property type="componentProperty">
        <name>ENGINE_NAME</name>
        <value>{4}</value>
      </property>
      <property type="componentProperty">
        <name>ENGINE_COMMENT1</name>
        <value>{5}</value>
      </property>      
      <property type="componentProperty">
        <name>ENGINE_COMMENT2</name>
        <value>{6}</value>
      </property> 
      <property type="componentProperty">
        <name>ENGINE_CR</name>
        <value type="itemName">
          <value>{7}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>      
      <property type="componentProperty">
        <name>ENGINE_CS</name>
        <value type="itemName">
          <value>{8}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>ENGINE_DB</name>
        <value type="itemName">
          <value>{9}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>ENGINE_DB_have</name>
        <value>{10}</value>
      </property>
      <property type="componentProperty">      
        <name>ENGINE_RP</name>
        <value type="itemName">
          <value>{11}</value>
          <dataName>item_df</dataName>          
        </value>
      </property> 
      <property type="componentProperty">
        <name>ENGINE_MODE_A</name>
        <value type="itemName">
          <value>{12}</value>
          <dataName>item_df</dataName>         
        </value>
      </property>      
      <property type="componentProperty">
        <name>ENGINE_MODE_M</name>
        <value type="itemName">
          <value>{13}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>Param_TypeModesChange</name>
        <value>{14}</value>
      </property>
      <property type="componentProperty">
        <name>ENGINE_SG_have</name>
        <value>{15}</value>
      </property>
      <property type="componentProperty">
        <name>ENGINE_SD_have</name>
        <value>{16}</value>
      </property>
      <property type="componentProperty">
        <name>ENGINE_SG</name>
        <value>false</value>
      </property> 
      <property type="componentProperty">
        <name>ENGINE_SD</name>
        <value>false</value>
      </property>    
      <property type="componentProperty">
        <name>ENGINE_CR_ALG</name>
        <value>false</value>
      </property>      
      <property type="componentProperty">
        <name>ENGINE_CS_ALG</name>
        <value>false</value>
      </property> 
      <property type="componentProperty">
        <name>ENGINE_SW</name>
        <value>false</value>
      </property>
      <property type="componentProperty">
        <name>ENGINE_SN</name>
        <value>false</value>
      </property>
      <property type="componentProperty">
        <name>ENGINE_NRS</name>
        <value>false</value>
      </property>
      <property type="componentProperty">
        <name>Engine_PAZ</name>
        <value>false</value>
      </property>{17}
    </symbolInstance.Mixer_01>"""

Valve_PID_01 = """<symbolInstance.Valve_PID_01 type="componentData">
      <config type="graphicInfo"/>
      <scale>1.0</scale>
      <x>{0}</x>
      <y>{1}</y>
      <top>0.0</top>
      <bottom>-0.0</bottom>
      <left>0.0</left>
      <right>-0.0</right>      
      <property type="componentProperty">
        <name>Param_NamePosX</name>
        <value>0.0</value>
      </property>
      <property type="componentProperty">
        <name>Param_NamePosY</name>
        <value>0.0</value>
      </property>
      <property type="componentProperty">
        <name>Param_MVPosX</name>
        <value>0.0</value>
      </property>
      <property type="componentProperty">
        <name>Param_MVPosY</name>
        <value>0.0</value>
      </property>      
      <property type="componentProperty">
        <name>Param_ObjectRotation</name>
        <value>0.0</value>
      </property>
      <property type="componentProperty">
        <name>Param_FP_Enable</name>
        <value>{2}</value>
      </property>
      <property type="componentProperty">
        <name>PID_COM_FLT</name>
        <value type="itemName">
          <value>{3}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>      
      <property type="componentProperty">
        <name>PID_NAME</name>
        <value>{4}</value>
      </property>      
      <property type="componentProperty">
        <name>PID_MODE</name>
        <value type="itemName">
          <value>{5}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>PID_MV</name>
        <value type="itemName">
          <value>{6}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>      
      <property type="componentProperty">
        <name>PID_SV</name>
        <value type="itemName">
          <value>{7}</value>
          <dataName>item_df</dataName>          
        </value>
      </property> 
      <property type="componentProperty">
        <name>PID_kP</name>
        <value type="itemName">
          <value>{8}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>PID_kI</name>
        <value type="itemName">
          <value>{9}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>PID_kD</name>
        <value type="itemName">
          <value>{10}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>      
      <property type="componentProperty">
        <name>PID_DB</name>
        <value type="itemName">
          <value>{11}</value>
          <dataName>item_df</dataName>         
        </value>
      </property>
      <property type="componentProperty">
        <name>PID_DB_Have</name>
        <value>{12}</value>
      </property> 
      <property type="componentProperty">
        <name>PID_POS</name>
        <value type="itemName">
          <value>{13}</value>
          <dataName>item_df</dataName>         
        </value>
      </property>      
      <property type="componentProperty">
        <name>PID_POS_HAVE</name>
        <value>{14}</value>
      </property>      
      <property type="componentProperty">
        <name>PID_OOP</name>
        <value>false</value>
      </property>
      <property type="componentProperty">
        <name>PID_PAZ</name>
        <value>false</value>
      </property>   
      <property type="componentProperty">
        <name>VALVE_SG_Have</name>
        <value>{15}</value>
      </property>
      <property type="componentProperty">
        <name>VALVE_SD_Have</name>
        <value>{16}</value>
      </property>
      <property type="componentProperty">
        <name>VALVE_SG</name>
        <value>false</value>
      </property>
      <property type="componentProperty">
        <name>VALVE_SD</name>
        <value>false</value>
      </property>
      <property type="componentProperty">
        <name>VALVE_SN</name>
        <value>false</value>
      </property>  
      <property type="componentProperty">
        <name>SENS_PV</name>
        <value type="itemName">
          <value>{17}</value>
          <dataName>item_df</dataName>         
        </value>
      </property>      
      <property type="componentProperty">
        <name>SENS_ENG_UNIT</name>
        <value>{18}</value>
      </property>      
      <property type="componentProperty">
        <name>SENS_A</name>
        <value type="itemName">
          <value>{19}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>SENS_AOF</name>
        <value type="itemName">
          <value>{20}</value>
          <dataName>item_df</dataName>         
        </value>
      </property>      
      <property type="componentProperty">
        <name>SENS_HH</name>
        <value type="itemName">
          <value>{21}</value>
          <dataName>item_df</dataName>         
        </value>
      </property>
      <property type="componentProperty">
        <name>SENS_HH_Have</name>
        <value>{22}</value>
      </property>
      <property type="componentProperty">
        <name>SENS_HI</name>
        <value type="itemName">
          <value>{23}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>SENS_HI_Have</name>
        <value>{24}</value>
      </property>
      <property type="componentProperty">
        <name>SENS_LO</name>
        <value type="itemName">
          <value>{25}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>SENS_LO_Have</name>
        <value>{26}</value>
      </property>
      <property type="componentProperty">
        <name>SENS_LL</name>
        <value type="itemName">
          <value>{27}</value>
          <dataName>item_df</dataName>         
        </value>
      </property>
      <property type="componentProperty">
        <name>SENS_LL_Have</name>
        <value>{28}</value>
      </property>{29}      
    </symbolInstance.Valve_PID_01>"""
    
Sens_PID_01 = """<symbolInstance.Sens_PID_01 type="componentData">
      <config type="graphicInfo"/>
      <x>{0}</x>
      <y>{1}</y>
      <top>0.0</top>
      <bottom>-0.0</bottom>
      <left>0.0</left>
      <right>-0.0</right>      
      <property type="componentProperty">
        <name>Param_FP_Enable</name>
        <value>{2}</value>
      </property>      
      <property type="componentProperty">
        <name>PID_COM_FLT</name>
        <value type="itemName">
          <value>{3}</value>
          <dataName>item_df</dataName>         
        </value>
      </property>         
      <property type="componentProperty">
        <name>PID_NAME</name>
        <value>{4}</value>
      </property>
      <property type="componentProperty">
        <name>PID_MODE</name>
        <value type="itemName">
          <value>{5}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>      
      <property type="componentProperty">
        <name>PID_MV</name>
        <value type="itemName">
          <value>{6}</value>
          <dataName>item_df</dataName>         
        </value>
      </property>
      <property type="componentProperty">
        <name>PID_SV</name>
        <value type="itemName">
          <value>{7}</value>
          <dataName>item_df</dataName>         
        </value>
      </property>
      <property type="componentProperty">
        <name>PID_kP</name>
        <value type="itemName">
          <value>{8}</value>
          <dataName>item_df</dataName>         
        </value>
      </property>      
      <property type="componentProperty">
        <name>PID_kI</name>
        <value type="itemName">
          <value>{9}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>PID_kD</name>
        <value type="itemName">
          <value>{10}</value>
          <dataName>item_df</dataName>         
        </value>
      </property>
      <property type="componentProperty">
        <name>PID_DB</name>
        <value type="itemName">
          <value>{11}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>PID_DB_Have</name>
        <value>{12}</value>
      </property>   
      <property type="componentProperty">
        <name>PID_PAZ</name>
        <value>false</value>
      </property>
      <property type="componentProperty">
        <name>SENS_PV</name>
        <value type="itemName">
          <value>{13}</value>
          <dataName>item_df</dataName>          
        </value>
      </property> 
      <property type="componentProperty">
        <name>SENS_NAME</name>
        <value>{14}</value>
      </property>      
      <property type="componentProperty">
        <name>SENS_ENG_UNIT</name>
        <value>{15}</value>
      </property>      
      <property type="componentProperty">
        <name>SENS_A</name>
        <value type="itemName">
          <value>{16}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>      
      <property type="componentProperty">
        <name>SENS_AOF</name>
        <value type="itemName">
          <value>{17}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>      
      <property type="componentProperty">
        <name>SENS_HH</name>
        <value type="itemName">
          <value>{18}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>SENS_HH_Have</name>
        <value>{19}</value>
      </property>      
      <property type="componentProperty">
        <name>SENS_HI</name>
        <value type="itemName">
          <value>{20}</value>
          <dataName>item_df</dataName>          
        </value>
      </property> 
      <property type="componentProperty">
        <name>SENS_HI_Have</name>
        <value>{21}</value>
      </property>      
      <property type="componentProperty">
        <name>SENS_LO</name>
        <value type="itemName">
          <value>{22}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>SENS_LO_Have</name>
        <value>{23}</value>
      </property>      
      <property type="componentProperty">
        <name>SENS_LL</name>
        <value type="itemName">
          <value>{24}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>SENS_LL_Have</name>
        <value>{25}</value>
      </property>{26}  
    </symbolInstance.Sens_PID_01>"""

Palarm = """<symbolInstance.Palarm type="componentData">
      <config type="graphicInfo"/>
      <scale>1.0</scale>
      <x>{0}</x>
      <y>{1}</y>
      <top>0.0</top>
      <bottom>0.0</bottom>
      <left>0.0</left>
      <right>0.0</right>      
      <property type="componentProperty">
        <name>Param_Sound</name>
        <value>{2}</value>
      </property>
      <property type="componentProperty">
        <name>ALARM_COM_FLT</name>
        <value type="itemName">
          <value>{3}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>ALARM_BOOL</name>
        <value type="itemName">
          <value>{4}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>ALARM_DB</name>
        <value type="itemName">
          <value>{5}</value>
          <dataName>item_df</dataName>          
        </value>
      </property>
      <property type="componentProperty">
        <name>ALARM_DBhave</name>
        <value>{6}</value>
      </property>
      <property type="componentProperty">
        <name>ALARM_SCC</name>
        <value>false</value>
      </property>{7}      
    </symbolInstance.Palarm>"""

Label = """<text type="componentData">      
      <value>{2}</value>
      <font type="font" name="Arial" size="16"/>
      <stroke type="stroke" width="1.0"/>
      <x>{0}</x>
      <y>{1}</y>
      <top>12.0</top>
      <bottom>0.0</bottom>
      <left>0.0</left>
      <right>60.0</right>
      <keepOriginalSize>true</keepOriginalSize>{3}
    </text>"""

ToggleButton = """<toggleButton type="componentData" x="{0}" y="{1}" top="16.0" bottom="16.0" left="72.0" right="72.0">
      <label>{2}</label>
      <data type="data">
        <action type="actionConnectTo">
          <property type="property" name="toggleButton.value"/>
          <filter type="filter">
            <value>0.0</value>
          </filter>
          <connection type="connection">
            <itemName>{3}</itemName>            
            <itemAttribute>ItemValue</itemAttribute>
          </connection>
        </action>
      </data>
    </toggleButton>"""
    
