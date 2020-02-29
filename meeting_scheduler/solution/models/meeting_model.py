class Meeting:
 
    def __init__(self,date,time,length,info,employee_name):
        self.date = date
        self.time = time
        self.length = length
        self.info = info
        self.employee_name = employee_name

    def __repr__(self):
        return f"{self.date} {self.time} {self.length} {self.info} {self.employee_name}"


class Meeting_Factory:

    min_hour = 9
    max_hour = 21
    min_length = 1
    max_length = 5
    
    @staticmethod
    def create_meeting(date,time,length,info,employee_name):
        if True:
             return Meeting(date,time,length,info,employee_name)


    @staticmethod
    def meeting_to_string(meeting):
        return f"{meeting.date}%{meeting.time}%{meeting.length}%{meeting.info}%{meeting.employee_name}%"

    


    
