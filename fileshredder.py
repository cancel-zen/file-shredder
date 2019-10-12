# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 10:12:31 2019

@author: cs
"""

import os
import random
file_name = input("输入要粉碎的文件路径：  ")
cycles = int(input("输入复写次数（至少1次）： "))
def shred():
   f = open(file_name,'wb+')
   f.read()
   len= f.tell()
   data_temp=[] 
   for i in range(len):
      data_temp.append(random.randint(0,1))
   data=''.join(data_temp)
   f.seek(0)
   f.write(data.encode('UTF-8'))
   f.close()
for i in range(0,cycles):
    shred()
os.rename(file_name,'asdfasdfasf')
os.unlink('asdfasdfasf')
print(file_name + " 文件粉碎成功")