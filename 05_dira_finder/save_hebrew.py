import csv
import base64

def save_list_encoded(myData):
      myFile = open('data.csv', 'w')
      with myFile:
          writer = csv.writer(myFile)
          writer.writerows([base64.b64encode(i.encode()) for i in myData])


def read_encoded_as_list():
      new_list = []
      with open('data.csv', newline='') as File:  
          reader = csv.reader(File)
          for row in reader:
              new_list.append(base64.b64decode(bytes("".join([chr(int(i)) for i in row]), 'utf-16', "ignore")).decode("utf-8"))
      return [x for x in new_list if x]


def sync_data_to_file(data):
      save_list_encoded(data)
      return read_encoded_as_list()


