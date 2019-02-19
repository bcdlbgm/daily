#不成大佬不改名
#-*- coding:utf-8 -*-
#!/usr/bin/env python3
import time
import os
import threading
# dict={
#      'a':"s",
#      'r':'q'
# }
#
# for i in dict:
#      print(i)

# def Averaged_data(data):
#      print(type(data))
#
#      Decrement_quantity = 0
#      # data_Quantity = len(data)
#      data_false = data/ 10
#      while type(data_false)!=int:
#           data -= 1
#
#           Decrement_quantity +=1
#           print(Decrement_quantity)





#      print(Decrement_quantity)
#      # print(data_Quantity)
#      print(data_false)
#
# Averaged_data(12453)

def recursion_file(catalog,suffix=".txt"):
     File_list=[]
     file_list = os.listdir(catalog)
     for i in file_list:
          if os.path.isdir(i):
               recursion_file(i)
          elif suffix in os.path.splitext(i):
               File_list.append(i)
     return File_list

def dir_txt(path,recursion=False):
     file_list = []
     path,file=os.path.split(path)
     print(path,"   ",file)
     if  file=='*':
          print(3)
          if recursion==True:
               print(0)
               file_list = recursion_file(path)
               return file_list
          else:
               print(1)
               li = os.listdir(path)
               for i in li:
                    if os.path.isfile(i) and ".txt" in os.path.splitext(i):
                         file_list.append(i)
               return file_list
     elif file==True:
          print(7)
          file = file.split(',')
          for i in file:
               file.append(os.path.join(path,i))
          return file_list


a = dir_txt("F:\\字典\\*")
print(a)

