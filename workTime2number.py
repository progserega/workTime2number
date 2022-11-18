#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time
import datetime
import os
import csv

if len(sys.argv)<2:
  print("нужен один параметр - имя входного файла csv. Выход будет на экран")
  sys.exit(1)
with open(sys.argv[1], newline='\n') as csvfile:
  data = csv.DictReader(csvfile, delimiter=';')
  for row in data:
    # переводим время в дробноче число часа:
    t = row['spent'].split(':')
    hours = float(int(t[0])*60+int(t[1]))/60
    print("%s;%f"%(row['day'],hours))
