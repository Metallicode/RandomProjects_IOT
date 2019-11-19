def Notify_User(new_data, print_items=False):
      if len(new_data)>0:
            print(f"you have new data! {len(new_data)} items!")
            if print_items:
                  for i in new_data:
                        print(i)
      else:
            print("Nothing New..")

def Print_All_Data(data):
      for i in data:
            print(i)
            print("************************\n")

def Make_HTML(data):

      style = "<link rel='stylesheet' type='text/css' href='style.css'>"
      
      strTable = "<html>"+style+"<body><h1>דירות מיד2</h1><table><tr><th></th></tr>"
 
      for i in range(len(data)):
            dataLst = data[i].split("\n")
            item_id = dataLst[0]
            item_title = f"<h3><a href='https://www.google.co.il/maps/place/{dataLst[1]}{dataLst[2]}'>{dataLst[1]}</a></h3>"
            item_subtitle = f"<p>{dataLst[2]}</p>"
            item_num_spec = f"<p>rooms:{dataLst[3]}      size:{dataLst[4]}</p>"
            item_price = f"<h5>{dataLst[5]}</h5>"
            item_date = f"<p>{dataLst[6]}</p>"
            
            strRW = "<tr><td dir='rtl'>"+f"{item_date}{item_title}{item_subtitle}{item_num_spec}{item_price}{item_id}"+ "</td></tr>"
      
            strTable = strTable+strRW
 
      strTable = strTable+"</table></body></html>"
 
      with open("view_data.html", 'w', encoding="utf-8") as hs:
           hs.write(strTable)
 

      
