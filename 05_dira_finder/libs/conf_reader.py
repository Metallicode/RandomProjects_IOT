import csv

def Get_Search_Data():
      with open("config.txt", "r") as file:
            f = [x.split(",") for x in file.read().split()]
            search_data = {"City":f[2][1], "Min_Rooms":f[1][1], "Max_Price":f[0][1]}
            return search_data

def Get_HTML_File_Location():
      with open("config.txt", "r") as file:
            f = [x.split(",") for x in file.read().split()]
            return f[3][1]

def Get_Bot_Key():
      with open("config.txt", "r") as file:
            f = [x.split(",") for x in file.read().split()]
            return f[4][1]

def Set_Config(key, value):
      configs = []
      print(key, value)
      with open("config.txt", "r") as file:
            file = [x.split(",") for x in file.read().split()]
            for row in file:
                  if key == row[0]:
                        row[1]=value
            configs = file
            
      with open('config.txt', 'w') as file:
          writer = csv.writer(file)
          writer.writerows(configs)
