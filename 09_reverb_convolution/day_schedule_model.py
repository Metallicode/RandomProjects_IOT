from hour_block_model import Hour_Block
import json

class Day_Schedule:
    
    def __init__(self, data=None):
        self.schedule = []

        self.schedule.append(Hour_Block("09:00 - 10:00"))
        self.schedule.append(Hour_Block("10:00 - 11:00"))
        self.schedule.append(Hour_Block("11:00 - 12:00"))
        self.schedule.append(Hour_Block("12:00 - 13:00"))
        self.schedule.append(Hour_Block("13:00 - 14:00"))
        self.schedule.append(Hour_Block("14:00 - 15:00"))
        self.schedule.append(Hour_Block("15:00 - 16:00"))
        self.schedule.append(Hour_Block("16:00 - 17:00"))
        self.schedule.append(Hour_Block("17:00 - 18:00"))

        
        if data is not None:
            if type(data) == list: 
                self.fit_data(data)
            else:               
                days = json.loads(data.decode())["schedule"]            
                for i in range(len(self.schedule)):
                    self.schedule[i].title = days[i]['title']
                    self.schedule[i].info = days[i]['info']

    def get_hour_data(self, hour):
        for i in self.schedule:
            if i.time == hour:
                return i
    
    def fit_data(self, data):
        day_as_list = []
   
        for i in data:
            time_index = 0
            
            for k in self.schedule:           
                if k.time == i.time:
                    break
                time_index+=1        

            for j in range(i.length):
                day_as_list.append((self.schedule[time_index+j].time, i.employee_name, i.info))
                    
        for i in day_as_list:
            for j in self.schedule:
                if j.time == i[0]:
                    j.title = i[1]
                    j.info = i[2]
                
        if len(day_as_list)==0:
            print("no data")

                
