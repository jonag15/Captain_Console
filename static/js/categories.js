$(document).ready(function() {
    $(".category_select").change(function() {
        if(this.checked) {
            var url = window.location.href
            var type_id = $(this).val();
            $.ajax( {

                url: '/?type_filter=' + type_id,
                type: 'GET',
                success: function (response) {
                    var newHtml = response.data.map(d => {
                        return `<div class="col-md-6">
                                <div class="card mb-3 shadow-sm">
                                  <div class="card-body">
                            
                                    <div class="productInfo">
                                        <img class="image-product card-img-top" width="300px" height="250px" src="${d.firstImage}">
                            
                                        <h4 class="card-text productInfo">${d.name}</h4>
                                        <h4 class="card-text productInfo">${d.price} kr</h4>
                                    </div>
                                    <div class="d-flex justify-content-between align-items-center">
                                        <div class="btn-group">
                                            <button type="button" class="btn btn-sm btn-outline-secondary btn-order"
                                                    onclick="AddItem(${d.id})">Setja í körfu
                                            </button>
                                            <a class="btn btn-primary btn-sm btn-outline-secondary btn-info"
                                               href="{% url 'product_info' product.id %}" role="button">Upplýsingar</a>
                                        </div>
                                  </div>
                                </div>
                                </div>
                                </div>`
                    });
                    $('.product_display').html(newHtml.join(''));
                },
                error: function (xhr, status, error) {
                    console.error(error)
                }
            })
        }
    });
});

$(document).ready(function() {
    $(".age_select").change(function() {
        if(this.checked) {
            var url = window.location.href
            var type_id = $(this).val();
            $.ajax( {
                url: '/?age_filter=' + type_id,
                type: 'GET',
                success: function (response) {
                    var newHtml = response.data.map(d => {
                        return `<div class="col-md-6">
                                <div class="card mb-3 shadow-sm">
                                  <div class="card-body">
                            
                                    <div class="productInfo">
                                        <img class="image-product card-img-top" width="300px" height="250px" src="${d.firstImage}">
                            
                                        <h4 class="card-text productInfo">${d.name}</h4>
                                        <h4 class="card-text productInfo">${d.price} kr</h4>
                                    </div>
                                    <div class="d-flex justify-content-between align-items-center">
                                        <div class="btn-group">
                                            <button type="button" class="btn btn-sm btn-outline-secondary btn-order"
                                                    onclick="AddItem(${d.id})">Setja í körfu
                                            </button>
                                            <a class="btn btn-primary btn-sm btn-outline-secondary btn-info"
                                               href="{% url 'product_info' product.id %}" role="button">Upplýsingar</a>
                                        </div>
                                  </div>
                                </div>
                                </div>
                                </div>`
                    });
                    $('.product_display').html(newHtml.join(''));
                },
                error: function (xhr, status, error) {
                    console.error(error)
                }
            })
        }
    });
});