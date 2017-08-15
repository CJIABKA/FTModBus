#!/usr/bin/env python
# -*- coding: utf-8 -*-
from MyProject import Project

#Путь к базе проекта. Одинарный слеш "\", заменяется на двойной "\"
BasePath = u'C:\\Share\\FAM3\\Buf.xls'
#Путь к папке прокта. Одинарный слеш "\", заменяется на двойной "\"
ProjectPath = u'C:\\Share\\FAM3'

MB = Project(BasePath, ProjectPath)
MB.main()

print (u'Обработка закончена ')