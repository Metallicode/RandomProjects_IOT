def Get_Search_Url():
      with open("config.txt", "r") as file:
            f = [x.split(",") for x in file.read().split()]
            Site_URL=f[0][1]
            Max_Price=f[3][1]
            Min_Rooms=f[4][1]
            Property_Type=f[5][1]
            City=f[6][1]
            URL_FORMAT = f"{Site_URL}?city={City}&property={Property_Type}&rooms={Min_Rooms}--1&price=-1-{Max_Price}"
            return URL_FORMAT

def Get_API_Str():
      with open("config.txt", "r") as file:
            f = [x.split(",") for x in file.read().split()]
            return f[1][1]

def Get_HTML_File_Location():
      with open("config.txt", "r") as file:
            f = [x.split(",") for x in file.read().split()]
            return f[2][1]

def Get_Bot_Key():
      with open("config.txt", "r") as file:
            f = [x.split(",") for x in file.read().split()]
            return f[7][1]
