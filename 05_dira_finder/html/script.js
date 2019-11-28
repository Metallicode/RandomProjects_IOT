	function btn_click(e){
		
	id = e.target.getAttribute("item_id");
		
		item = {
			item_id:$("#item"+id+"_id").text(),
			item_title:$("#item"+id+"_title").text(),
			item_subtitle:$("#item"+id+"_subtitle").text(),
			item_room_num:$("#item"+id+"_room_num").text(),
			item_size:$("#item"+id+"_size").text(),
			item_price:$("#item"+id+"_price").text(),
			item_date:$("#item"+id+"_date").text(),
			item_text_input:$("#item"+id+"_text_input").val()
		}	
	
	data={"message": JSON.stringify(item)};
	
	$.post("http://192.168.1.11:8000", data , function(data, status){
		console.log("Data: " + data + "Status: " + status);
		$("#item"+id+"_text_input").val("")
	});
	
	}
	
	$(function(){
		
		$(".item_id").click(function(e){		
			console.log(e.target.innerText);	

			data={"item_id":e.target.innerText};
					
			$.post("http://192.168.1.11:8000", data , function(data, status){
					console.log(data + "Status: " + status);
					$("#item"+e.target.innerText+"_id").text(data);
				});
		});
		
	});