import csv
import base64
from libs.dira_item import Dira

def save_list_encoded(myData):
      with open('data//data.csv', 'w') as myFile:
          writer = csv.writer(myFile)
          writer.writerows([base64.b64encode(i.encode()) for i in convert_to_strings(myData)])

def save_to_favorite(data):
      with open('data//favorite_items.txt', 'a', encoding="utf-8") as myFile:
          myFile.write(data)

def read_encoded_as_list():
      new_list = []
      with open('data//data.csv', newline='') as File:  
          reader = csv.reader(File)
          for row in reader:
              new_list.append(base64.b64decode(bytes("".join([chr(int(i)) for i in row]), 'utf-16', "ignore")).decode("utf-8"))
      return convert_to_obj([x for x in new_list if x])

def sync_data_to_file(data):
      save_list_encoded(data)
      return read_encoded_as_list()

def convert_to_strings(obj_list):
      return [i.Get_String() for i in obj_list]

def convert_to_obj(str_list):
      obj_lst = []
      for i in str_list:
            dataLst = i.split("\n")
            dira_item = Dira(dataLst[0], dataLst[1], dataLst[2], dataLst[3], dataLst[4], dataLst[5], dataLst[6])
            obj_lst.append(dira_item)
      return obj_lst
