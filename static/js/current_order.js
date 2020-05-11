function getCurrentOrder() {
    var key = "";
    var value = "";
    var i = 0;

    for (i = 0; i <= localStorage.length-1; i++) {
        key = localStorage.key(i);
        value = localStorage.getItem(key);
    }
}

$(document).ready(function() {
	if (top.location.pathname === '/order/') {
		console.log( "ready!" );
		var orderList = [];
		var i = 0;
		for (i = 0; i <= localStorage.length - 1; i++) {
			orderList.push(parseInt(localStorage.key(i)));
		};
		console.log( orderList );

		$.ajax( {
			url: '/order?order_list=' + orderList,
			type: 'GET',
			success: function (resp) {
				console.log( "success!" );
				var newHtml = resp.data.map(d => {
					var count = localStorage.getItem((d.id).toString())
					return `<div class="single_product">
							  <a href="/product/${d.id}">
								<tr>
								  <th scope="row">
									<div class="p-2">
									  <img src="${d.firstImage}" alt="Picture of product" class="img-fluid rounded shadow-sm gen_pic">
									  <div class="ml-3 d-inline-block align-middle">
										<h5 class="mb-0"><a href="#" class="text-dark d-inline-block">${d.name}</a></h5>
									  </div>
									</div>
								  </th>
								  <td class="align-middle"><strong>${d.price}</strong></td>
								  <td class="align-middle">
									  <div class='order_count'>
										  <button class='down_count btn btn-secondary btn-sm' title='Down'><i class='fa fa-minus'></i></button>
										  <input class='counter' type="text" value="${count}" />
										  <button class='up_count btn btn-secondary btn-sm' title='Up'><i class='fa fa-plus'></i></button>
										</div>
								  </td>
								  <td class="align-middle trash-can"><a href="#" class="text-dark"><i class="fa fa-trash"></i></a></td>
								</tr>
							  </a>
							</div>`
				});
				$('.order_products').html(newHtml.join(''));
			},
			error: function (xhr, status, error) {
				// TODO: error message
				console.error(error)

			}

		})
	}
});

function AddItem(product_id) {
	var id = product_id;
	if (localStorage.getItem(id) == null) {
		localStorage.setItem(id,1)
	}
	else {
		var count = localStorage.getItem(id);
		localStorage.setItem(id, parseInt(count)+ 1);
	}
}

function ModifyItemCount() {
	var name1 = document.forms.ShoppingList.name.value;
	var data1 = document.forms.ShoppingList.data.value;
	//check if name1 is already exists

//check if key exists
			if (localStorage.getItem(name1) != null)
			{
			  //update
			  localStorage.setItem(name1,data1);
			  document.forms.ShoppingList.data.value = localStorage.getItem(name1);
			}
}

function RemoveItem() {
	var name = document.forms.ShoppingList.name.value;
	document.forms.ShoppingList.data.value = localStorage.removeItem(name);
}

function ClearAllItems() {
	localStorage.clear();
}
