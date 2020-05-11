$(document).ready(function() {

    $('#searchbutton').on( 'click',  function(event) {
        event.preventDefault();
        let searchText = $('#searchbar').val();
        $.ajax(  {
                url: '/product?search_filter=' + searchText,
                type: 'GET',
                success: function(response) {
                    let newHtml = response.data.map(d => {
                        return `<div class="card mb-3 shadow-sm product">
                                    <a href="/product/${d.id}">
                                <img class="image-product card-img-top" src="${d.firstImage}" alt="ProductImage" />
                                <h4>${d.name}</h4>
                                </a>
                            </div>`
                    });
                    $('#product').html(newHtml.join(''));
                    $('#searchbar').val('');

            },
                error: function(xhr, status, error) {
                    //TODO: Show toastr
                    console.error(error);
            }

        })

    });
});