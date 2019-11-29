	function btn_click(e){
		
	id = e.target.getAttribute("item_id");
		
		item = {
			item_details:$("#item"+id+"_details").text(),
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
	
	$.post("http://localhost:8000", data , function(data, status){
		console.log("Data: " + data + "Status: " + status);
		$("#item"+id+"_text_input").val("")
		$(e.target).parent().css("background-color", "#333300");
	});
	
	}
	
	function get_favorites(){
		$.get("http://192.168.1.11:8000" , function(data, status){
			
			$("#items_table tr").remove();
			$("#get_favorites_btn").remove();
			
			items = JSON.parse(data).reverse();
			for (i = 0; i <items.length; i++) {
				$("#items_table").append($('<tr>').append($('<td>').append("<p class='favorites' dir='rtl'>"+ 
				items[i].item_date +"   "+ 
				items[i].item_title +"   "+ 
				items[i].item_details +"   "+
				items[i].item_text_input +"   "+
				items[i].item_price +"   </p>")));
				}
		});
	}
	
	
	$(function(){
		
		$(".item_id").click(function(e){		
			console.log(e.target.innerText);	

			data={"item_id":e.target.innerText};
					
			$.post("http://localhost:8000", data , function(data, status){
					console.log(data + "Status: " + status);
					$("#item"+e.target.innerText+"_details").text(data);
				});
		});
		
	});