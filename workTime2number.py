#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time
import datetime
import os
import csv
import locale

#locale.setlocale(locale.LC_ALL, "ru_RU")
locale.setlocale(locale.LC_ALL, "")

if len(sys.argv)<2:
  print("нужен один параметр - имя входного файла csv. Выход будет в файл с постфиксом _converted.csv и на экран")
  sys.exit(1)
with open(sys.argv[1], newline='\n') as csvfile:
  data = csv.DictReader(csvfile, delimiter=';')

  # создаём файл:
  out_file = open("%s_converted.csv"%sys.argv[1],"w+")
  print("Дата;Время работы;Задача")
  out_file.write("Дата;Время работы;Задача\n")
  for row in data:
    # переводим время в дробноче число часа:
    t = row['spent'].split(':')
    hours = float(int(t[0])*60+int(t[1]))/60
    print("%s;%s;%s"%(row['day'],locale.str(hours),row['task']))
    out_file.write("%s;%s;%s\n"%(row['day'],locale.str(hours),row['task']))
  out_file.close()
