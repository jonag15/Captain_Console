function getCurrentOrder() {
    var key = "";
    var value = "";
    var i = 0;

    for (i = 0; i <= localStorage.length-1; i++) {
        key = localStorage.key(i);
        value = localStorage.getItem(key);
    }
}

function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = cookies[i].trim();
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function updateOrder() {
		var csrftoken = getCookie('csrftoken');
		var orderList = [];
		var i = 0;
		for (i = 0; i <= localStorage.length - 1; i++) {
			orderList.push(parseInt(localStorage.key(i)));
		};
		$.ajaxSetup({
    	beforeSend: function(xhr, settings) {
        	if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            	xhr.setRequestHeader("X-CSRFToken", csrftoken);
        		}
    		}
		});
		$.ajax( {
			url: '/order/',
			type: 'POST',
			ContentType: 'application/json',
			data: {'orderList': JSON.stringify({ paramName: orderList })},
			success: function (response) {
				var newHtml = response.data.map(d => {
					var count = localStorage.getItem((d.id).toString())
					var total_price = d.price * count
					return  `<tr>
								  <th scope="row">
									<div class="p-2">
									  <img src="${d.firstImage}" alt="Picture of product" class="img-fluid rounded shadow-sm gen_pic">
									  <div class="ml-3 d-inline-block align-middle">
										<h5 class="mb-0"><a href="href="/product/${d.id}" class="text-dark d-inline-block">${d.name}</a></h5>
									  </div>
									</div>
								  </th>
								  <td id="price_${d.id}" class="align-middle price" value=${total_price}><strong>${d.price} kr</strong></td>
								  <td class="align-middle">
									  <div class='order_count'>
										  <button class='down_count btn btn-secondary btn-sm' title='Down' onclick="downCount(${d.id})"><i class='fa fa-minus'></i></button>
										  <input id="counter_${d.id}"  class='counter' type="text" value=${count} />
										  <button class='up_count btn btn-secondary btn-sm' title='Up' onclick="upCount(${d.id})"><i class='fa fa-plus'></i></button>
										</div>
								  </td>
								  <td class="align-middle trash-can"><a class="text-dark" onclick="RemoveItem(${d.id})" ><i class="fa fa-trash"></i></a></td>
								</tr>`


				});
				$('.order_products').html(newHtml.join(''));
				totalPrice()
			},
			error: function (xhr, status, error) {
				// TODO: error message
			}
		})
}

function totalPrice() {
	var sumPrice = 0;
    var allPrices = $(".price");
	for(var i = 0; i < allPrices.length; i++){
    	sumPrice += parseInt(allPrices[i]['attributes'][2]['nodeValue']);
	}
    $("#total_price").val("Heildarverð: " + sumPrice + " kr");
}

$(document).ready(function() {
	if (top.location.pathname === '/order/') {
		updateOrder()
	}
});

function AddItem(product_id) {
	if (localStorage.getItem(product_id) == null) {
		localStorage.setItem(product_id, 1)
	}
	else {
		var count = localStorage.getItem(product_id);
		localStorage.setItem(product_id, parseInt(count)+ 1);
	}
}



function upCount(product_id) {
	if (localStorage.getItem(product_id) != null) {
		var count = localStorage.getItem(product_id);
		localStorage.setItem(product_id, parseInt(count) + 1);
		$('#counter_' + product_id).val(parseInt(count) + 1);
		var old_total_price = parseInt($('#price_' + product_id)[0]['attributes'][2]['nodeValue']);
		var price_to_add = old_total_price / count
		var id_str = "price_" + product_id
		console.log(id_str)
		$("#"+id_str).val(old_total_price + price_to_add);
		totalPrice()

	}
}

function downCount(product_id) {
	if (localStorage.getItem(product_id) != null) {
		var count = localStorage.getItem(product_id);
		if (count - 1 >= 1) {
			localStorage.setItem(product_id, parseInt(count) - 1);
			$('#counter_' + product_id).val(parseInt(count) - 1);
			var old_total_price = parseInt($('#price_' + product_id)[0]['attributes'][2]['nodeValue']);
			var price_to_subtract = old_total_price / count
			var new_total_price = old_total_price - price_to_subtract
			console.log(new_total_price)
			var id_str = "price_" + product_id
			console.log(id_str)
			$("#"+id_str).val(new_total_price);
			console.log($("#"+id_str))
			totalPrice()
		}
	}
}

function RemoveItem(product_id) {
	if (localStorage.getItem(product_id) != null) {
		localStorage.removeItem(product_id)
		updateOrder()
	}
}

function ClearAllItems() {
	localStorage.clear();
}
