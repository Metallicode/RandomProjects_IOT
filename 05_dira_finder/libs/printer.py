def Notify_Admin(new_data, print_items=False):
      if len(new_data)>0:
            print(f"you have new data! {len(new_data)} items!")
            if print_items:
                  for i in new_data:
                        print(i.Get_String())
      else:
            print("Nothing New..")

def Print_All_Data(data):
      for i in data:
            print(i.Get_String())
            print("************************\n")

def Make_HTML(data):
      style = "<link rel='stylesheet' type='text/css' href='style.css'>"    
      strTable = f"<html>"+style+"<body><h1>Metallibord</h1><table><tr><th></th></tr>"
 
      for i in range(len(data)):
            item_id = f"<a class='item_id' id='item{data[i].item_id}_id'>{data[i].item_id}</a>"
            item_title = f"<h3 id='item{data[i].item_id}_title'><a href='https://www.google.co.il/maps/place/{data[i].title}'>{data[i].title}</a></h3>"
            item_subtitle = f"<p id='item{data[i].item_id}_subtitle'>{data[i].subtitle}</p>"
            item_num_spec = f"<p>rooms:<b id='item{data[i].item_id}_room_num'>{data[i].room_num}</b>      size:<b id='item{data[i].item_id}_size'>{data[i].size}</b></p>"
            item_price = f"<h5 id='item{data[i].item_id}_price'>{data[i].price}</h5>"
            item_date = f"<p id='item{data[i].item_id}_date'>{data[i].date}</p>"
            text_input = f"<input class='item_text_input' id='item{data[i].item_id}_text_input' type='text'/>"
            item_save_btn = f"<input type='button' item_id='{data[i].item_id}' onclick='btn_click(event)' class='button' value='Save'/>"
            
            strRW = f"<tr><td dir='rtl'>"+f"{item_date}{item_title}{item_subtitle}{item_num_spec}{item_id}{item_price}{text_input}{item_save_btn}"+ "</td></tr>"

            strTable = strTable+strRW

      page_script = """<script
            src="https://code.jquery.com/jquery-3.4.1.min.js"
            integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo="
            crossorigin="anonymous"></script>
            <script src="script.js"></script>"""
 
      strTable = strTable+f"</table>{page_script}</body></html>"
 
      with open("html//view_data.html", 'w', encoding="utf-8") as hs:
           hs.write(strTable)
 
