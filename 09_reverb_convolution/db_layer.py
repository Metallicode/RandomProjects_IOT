import sqlite3
from meeting_model import Meeting, Meeting_Factory
from day_schedule_model import Day_Schedule

from datetime import date

class Db_Layer:
 
    def __init__(self, table_name ="meetings"):
        self.table_name = table_name
        self.init_db()

        
    def init_db(self):
        self.connect_to_db()
        c = self.conn.cursor()
        c.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} (date TEXT, time TEXT, length INTEGER, info TEXT, employee_name TEXT)")
        self.conn.commit()
        self.close_connection()

        
    def connect_to_db(self):
        self.conn = sqlite3.connect('meeting_scheduler.db')

   
    def close_connection(self):
        self.conn.close()


    def query_db(self, qtype, data=None):
        res = None
        if qtype == "save":
            res = self.save_to_db(data)
        elif qtype == "read":
            res = self.read_from_db(data)
        elif qtype == "get_day":
            res = self.get_day_schedule(data)
        elif qtype == "delete":
            res = self.delete_from_db(data)
        elif qtype == "update":
            res = self.update_db(data)
        return res


    def save_to_db(self, data):
        self.connect_to_db()
        c = self.conn.cursor()
        c.execute(f"INSERT INTO {self.table_name} VALUES ('{data.date}','{data.time.strip()}',{data.length},'{data.info}','{data.employee_name}')")
        self.conn.commit()
        self.close_connection()


    def read_from_db(self, date):
        self.connect_to_db()
        c = self.conn.cursor()
        res = None
        if date is None:
            c.execute(f"SELECT * FROM {self.table_name}")
        else:
            c.execute(f"SELECT * FROM {self.table_name} WHERE date = '{date}'")

        data = c.fetchall()
        if len(data)>0:
            res = [Meeting_Factory.create_meeting(x[0],x[1],x[2],x[3],x[4]) for x in data]

        self.close_connection()
        return res


    def get_day_schedule(self,date=date.today()):
        return Day_Schedule(self.read_from_db(date))


    def is_available(meeting):
        pass


    def delete_from_db(self):
        self.connect_to_db()
        #todo..
        self.close_connection()


    def update_db(self):
        self.connect_to_db()
        #todo..
        self.close_connection()

    
    def clear_db(self):
        self.connect_to_db()
        c = self.conn.cursor()
        c.execute(f"DELETE FROM {self.table_name}")
        self.conn.commit()
        self.close_connection()



if __name__ == "__main__":
    db = Db_Layer()

    
