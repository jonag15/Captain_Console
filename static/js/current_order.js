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
			if ( parseInt(localStorage.key(i)) !== NaN)  {
				if (parseInt(localStorage.key(i)) !== null) {
				orderList.push(parseInt(localStorage.key(i)));
				};
			};
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
					console.log(d.name)
					return  `<tr>
								  <th scope="row">
									<div class="p-2">
									  <img src="${d.firstImage}" alt="Picture of product" class="img-fluid rounded shadow-sm gen_pic">
									  <div class="ml-3 d-inline-block align-middle">
										<h5 class="mb-0"><a href="href="/product/${d.id}" class="text-dark d-inline-block">${d.name}</a></h5>
									  </div>
									</div>
								  </th>
								  <td class="align-middle price" value="${total_price}" ><strong>${d.price} kr</strong>
								  </td>
								  <td id="price_${d.id}" class="align-middle" value="${d.price}">
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

function totalPrice() {
	var sumPrice = 0;
    var allPrices = $(".price");
	for(var i = 0; i < allPrices.length; i++){
    	sumPrice += parseInt(allPrices[i]['attributes'][1]['nodeValue']);
	}
	localStorage.setItem('total_price', sumPrice)
    $("#total_price_num").val(sumPrice);
}

function upCount(product_id) {
	if (localStorage.getItem(product_id) != null) {
		var count = localStorage.getItem(product_id);
		localStorage.setItem(product_id, parseInt(count) + 1);
		$('#counter_' + product_id).val(parseInt(count) + 1);
		var change_amount = parseInt($('#price_' + product_id)[0]['attributes'][2]['nodeValue']);
		value = localStorage.getItem('total_price');
		new_value = parseInt(value) + change_amount;
		localStorage.setItem('total_price', new_value);
		$("#total_price_num").val(new_value)
	}
}

function downCount(product_id) {
	if (localStorage.getItem(product_id) != null) {
		var count = localStorage.getItem(product_id);
		if (count - 1 >= 1) {
			localStorage.setItem(product_id, parseInt(count) - 1);
			$('#counter_' + product_id).val(parseInt(count) - 1);
			var change_amount = parseInt($('#price_' + product_id)[0]['attributes'][2]['nodeValue']);
			value = localStorage.getItem('total_price');
			new_value = parseInt(value) - change_amount;
			localStorage.setItem('total_price', new_value);
			$("#total_price_num").val(new_value)
		}
	}
}

function RemoveItem(product_id) {
	if (localStorage.getItem(product_id) != null) {
		localStorage.removeItem(product_id)
		updateOrder()
	}
}

$(document).ready(function() {
	if (top.location.pathname === '/order/payment/overview/complete') {
		localStorage.clear()
	}
});

$(document).ready(function() {
    $('#cancel_btn').on( 'click',  function() {
    	console.log("cancel")
    	localStorage.clear();
    });
});




$(document).ready(function() {

    $('#save_user_info').on( 'click',  function() {
		var first_name_element = document.getElementById('id_first_name')
		var first_name = first_name_element.value;
		localStorage.setItem('first_name', first_name);

		var last_name_element = document.getElementById('id_last_name')
		var last_name = last_name_element.value;
		localStorage.setItem('last_name', last_name);

		var email_element = document.getElementById('id_email')
		var email = email_element.value;
		localStorage.setItem('email', email);

		var address_element = document.getElementById('id_address')
		var address = address_element.value;
		localStorage.setItem('address', address);

		var zip_code_element = document.getElementById('id_zip_code')
		var zip_code = zip_code_element.value;
		localStorage.setItem('zip_code', zip_code);

		var country_element = document.getElementById('id_country')
		var country = country_element.value;
		localStorage.setItem('country', country);

		var card_number_element = document.getElementById('id_card_number')
		var card_number = card_number_element.value;
		localStorage.setItem('card_number', card_number);

		var valid_month_element = document.getElementById('id_valid_month')
		var valid_month = valid_month_element.value;
		localStorage.setItem('valid_month', valid_month);

		var valid_year_element = document.getElementById('id_valid_year')
		var valid_year = valid_year_element.value;
		localStorage.setItem('valid_year', valid_year);

		var cvc_element = document.getElementById('id_cvc')
		var cvc = cvc_element.value;
		localStorage.setItem('cvc', cvc);
});
});

$(document).ready(function() {
	if (top.location.pathname === '/order/payment/') {
		if (localStorage.getItem('first_name') != null) {
			$("#id_first_name").val(localStorage.getItem('first_name'));
		}
		if (localStorage.getItem('last_name') != null) {
			$("#id_last_name").val(localStorage.getItem('last_name'));
		}
		if (localStorage.getItem('email') != null) {
			$("#id_email").val(localStorage.getItem('email'));
		}
		if (localStorage.getItem('address') != null) {
			$("#id_address").val(localStorage.getItem('address'));
		}
		if (localStorage.getItem('zip_code') != null) {
			$("#id_zip_code").val(localStorage.getItem('zip_code'));
		}
		if (localStorage.getItem('country') != null) {
			$("#id_country").val(localStorage.getItem('country'));
		}

		if (localStorage.getItem('card_number') != null) {
			$("#id_card_number").val(localStorage.getItem('card_number'));
		}
		if (localStorage.getItem('valid_month') != null) {
			$("#id_valid_month").val(localStorage.getItem('valid_month'));
		}
		if (localStorage.getItem('country') != null) {
			$("#id_valid_year").val(localStorage.getItem('valid_year'));
		}
		if (localStorage.getItem('cvc') != null) {
			$("#id_cvc").val(localStorage.getItem('cvc'));
		}
	};
});

$(document).ready(function() {
	if (top.location.pathname === '/order/payment/overview') {
        $("#id_first_name_view").val(localStorage.getItem('first_name'));
		$("#id_last_name_view").val(localStorage.getItem('last_name'));
		$("#id_email_view").val(localStorage.getItem('email'));
		$("#id_address_view").val(localStorage.getItem('address'));
		$("#id_zip_code_view").val(localStorage.getItem('zip_code'));
		$("#id_country_view").val(localStorage.getItem('country'));

		$("#id_card_number_view").val(localStorage.getItem('card_number'));
		$("#id_valid_month_view").val(localStorage.getItem('valid_month'));
		$("#id_valid_year_view").val(localStorage.getItem('valid_year'));
		$("#id_cvc_view").val(localStorage.getItem('cvc'));
		$("#total_price_num_view").val('Heildarverð: ' + localStorage.getItem('total_price') + ' kr');

		var csrftoken = getCookie('csrftoken');
		var orderList = [];
		var i = 0;
		for (i = 0; i <= localStorage.length - 1; i++) {
			if ( parseInt(localStorage.key(i)) !== NaN)  {
				if (parseInt(localStorage.key(i)) != null) {
					orderList.push(parseInt(localStorage.key(i)));
				}
			}
		};


		$.ajaxSetup({
    	beforeSend: function(xhr, settings) {
        	if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            	xhr.setRequestHeader("X-CSRFToken", csrftoken);
        		}
    		}
		});
		$.ajax( {
			url: '/order/payment/overview',
			type: 'POST',
			ContentType: 'application/json',
			data: {'orderList': JSON.stringify({ paramName: orderList })},
			success: function (response) {
				var newHtml = response.data.map(d => {
					var count = localStorage.getItem((d.id).toString())
					return   `<tr>
							  <th scope="row">
								<div class="p-2">
								  <div class="ml-3 d-inline-block align-middle">
									<h5 class="mb-0"><a href="href="/product/${d.id}" class="text-dark d-inline-block">${d.name}</a></h5>
								  </div>
								</div>
							  </th>
							  <td class="align-middle price">${d.price} kr</td>
							  <td class="align-middle price">${count}</td>
							</tr>`
				});
				$('.order_products_overview').html(newHtml.join(''));
			},
			error: function (xhr, status, error) {
				// TODO: error message
			}
		})
	}
});

$(document).ready(function() {
	$('#order_confirmed').on('click', function () {
		console.log("clicked")
		var csrftoken = getCookie('csrftoken');
		var product_form = {};
		var i = 0;
		var id;
		for (i = 0; i <= localStorage.length - 1; i++) {
			if (localStorage.key(i) === 'total_price') {
				product_form[localStorage.key(i)] = parseInt(localStorage.getItem(localStorage.key(i)))
			}
			else if (parseInt(localStorage.key(i)) !== NaN) {
				if (parseInt(localStorage.key(i)) != null) {

					product_form[parseInt(localStorage.key(i))] = parseInt(localStorage.getItem(localStorage.key(i)))
				}
			}
		}

		console.log(product_form)
		$.ajaxSetup({
			beforeSend: function (xhr, settings) {
				if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
					xhr.setRequestHeader("X-CSRFToken", csrftoken);
				}
			}
		});
		$.ajax({
			url: '/order/payment/overview',
			type: 'POST',
			ContentType: 'application/json',
			data: {'product_form': JSON.stringify(product_form)},
			success: function (response) {
				var  test = response.data.map(d => {
					console.log(d['order_id'])
				})
				send_user_info()
				/*var url = window.location.href
				console.log(url + '/complete')
				window.location.assign(url + '/complete')*/
			},
			error: function (xhr, status, error) {
				// TODO: error message
			}
		});
	});
});

function send_user_info() {
	var user_info = document.getElementById("user_info");
	console.log(user_info)
}