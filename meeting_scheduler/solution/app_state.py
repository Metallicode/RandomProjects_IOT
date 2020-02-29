from datetime import date
import socket
from models.day_schedule_model import Day_Schedule

class App_State:
    def __init__(self):
        file = open("configuration", "r")
        config_data=[x.strip() for x in file.readlines()]
        config_data[1] = int(config_data[1])
        config_data[2] = config_data[2].split(',')
    
        self.users = config_data[2]

        self.socket_client =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_client.connect((config_data[0], config_data[1]))
   
        self.day_schedule = Day_Schedule(self.socket_client.recv(1024))
        
        self.current_user = self.users[0]
        self.selected_date = date.today()
        self.selected_hour = self.day_schedule.schedule[0].time
        
        self.selected_length = 0
        self.meeting_info = None
        self.text_element = None

    def set_date(self, date):
        self.selected_date = date

    def max_available(self, time):
        counter = 0
        count = False          
        for i in self.day_schedule.schedule:
            if i.time == time:               
                count = True
            if count:
                if i.title != "":
                    count = False
                    break
                counter+=1

        print("counter",counter)
        return counter
        
            

    def send_message(self, data):
        print(f"new Meeting: {data}")
        self.socket_client.send(data)
        print(self.socket_client.recv(1024))  

    def refresh_list(self):
        self.socket_client.send(f"get_day%{self.selected_date}".encode())       
        self.day_schedule = Day_Schedule(self.socket_client.recv(1024))
