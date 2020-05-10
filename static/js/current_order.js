function getCurrentOrder() {
    var key = "";
    var value = "";
    var i = 0;

    for (i = 0; i <= localStorage.length-1; i++) {
        key = localStorage.key(i);
        value = localStorage.getItem(key);
        if (key == 'name') //til dæmis
        	 {

        	 	// myndi þá fylla inn nafn í post request hér
			 }
    	else //ef að það passar ekki við hitt þá er þetta vara
			 {
				//vöru væri bætt við post hér
		}
    }
}

function AddItem(product_id) {
	var id = product_id;
	var count = document.forms.ShoppingList.data.value;
	localStorage.setItem(id, count);
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
