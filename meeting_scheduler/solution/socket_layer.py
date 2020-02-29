import socket
import select
from meeting_model import Meeting_Factory
from db_layer import Db_Layer
from threading import Thread
from datetime import date
import json

def query_thread(client,query_type,data=None):
      print("query_thread called")
      res = db.query_db(query_type, data)
      print("res",res)
      if query_type == "save":
            client.send(b"server is happy")
      elif query_type == "get_day":
            client.send(json.dumps(res, default=lambda o: o.__dict__).encode())


#create db object
db = Db_Layer()


#read config file
file = open("configuration", "r")
config_data=[x.strip() for x in file.readlines()]
config_data[1] = int(config_data[1])

#init socket 
server = socket.socket()
server.bind((config_data[0], config_data[1]))
server.listen(5)
inputs = [server]
print("starting server..")


      
while inputs:
      readables, _, _ = select.select(inputs, [], [])
      for i in readables:
            #new client connected
            if i is server:
                  client, address = server.accept()
                  inputs.append(client)
                  print("connected to new client")
                  t = Thread(target=query_thread, args=(client,"get_day", date.today()))
                  t.start()
                  

            else:
                  #new messaga from client
                  try:
                        data = i.recv(1024)
                        dataLst = data.decode().split("%")
                        #get day message
                        if dataLst[0] == 'get_day':
                               t = Thread(target=query_thread, args=(i,"get_day", dataLst[1]))
                               t.start()
                                    
                        #new item from client     
                        else:
                              while("" in dataLst) : 
                                  dataLst.remove("")

                              new_item =  Meeting_Factory.create_meeting(dataLst[0],dataLst[1],int(dataLst[2]),dataLst[3],dataLst[4])

                              t = Thread(target=query_thread, args=(i,"save",new_item))
                              t.start()

                  #client disconnected             
                  except Exception as e:
                        print(e)
                        inputs.remove(i)
                        print(f"client {i.getpeername()} BYE")
                        i.close()
