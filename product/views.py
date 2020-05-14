from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from product.forms.product_form import ProductCreateForm, ProductUpdateForm
from product.models import Product, ProductType, ProductSubTypes
from product.models import ProductImage
from product.models import SearchHistory
from datetime import date
from django.contrib.admin.views.decorators import staff_member_required




# Create your views here.
def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        if request.user.is_authenticated:
            form = SearchHistory()
            for prod in Product.objects.filter(name__icontains=search_filter):
                form.product_id = prod.id
                form.search_date = date.today()
                form.profile_id = request.user.id
                form.save()
        product = [ {
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage' : x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': product})

    context = {'products': Product.objects.all()}
    return render(request, 'product/index.html', context)

def index_by_name(request):

    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'product/index.html', context)

def index_by_price(request):
    context = {'products': Product.objects.all().order_by('price')}
    return render(request, 'product/index.html', context)


def info_index(request, id):


        return render(request, 'product/info.html', {
            'product': get_object_or_404(Product, pk=id),
            'category': get_object_or_404(ProductType, pk=id)
        })
    # categories = {
    #     "games": ProductType.objects.filter(id=1),
    #     "computers": ProductType.objects.filter(id=2),
    #     "accessory": ProductType.objects.filter(id=3),
    #     "spareparts": ProductType.objects.filter(id=4),
    #     }
    #'categories': ProductType.objects.all()
   # context = {'products': Product.objects.all(),
   #            'categories': ProductType.objects.all()}
   # return render(request, 'product/info.html', context)

# /product/1
def get_product_by_id(request, id):
   context = {'products': Product.objects.all()}
   return render(request, 'product/info.html',  {
       'product': get_object_or_404(Product, pk=id)
   })

#All games views
def get_all_games(request):
    context = {'products': Product.objects.filter(category_id=1)}
    return render(request, 'product/games.html', {
        'products': Product.objects.filter(category_id=1),
        'categories': Product.objects.filter(category_id=1)
    })


def games_by_name(request):
    context = {'product': Product.objects.filter(category_id=1).order_by('name')}
    return render(request, 'product/games.html', context)

def games_by_price(request):
    context = {'products': Product.objects.filter(category_id=1).order_by('price')}
    return render(request, 'product/games.html', context)


# All computer views
def get_all_computers(request):
    context = {'products': Product.objects.filter(category_id=2)}
    return render(request, 'product/computers.html', context)


def computers_by_name(request):
    context = {'products': Product.objects.filter(category_id=2).order_by('name')}
    return render(request, 'product/computers.html', context)

def computers_by_price(request):
    context = {'products': Product.objects.filter(category_id=2).order_by('price')}
    return render(request, 'product/computers.html', context)


#All accessory views
def get_all_accessory(request):
    context = {'products': Product.objects.filter(category_id=3)}
    return render(request, 'product/accessory.html', context)

def accessory_by_name(request):
    context = {'products': Product.objects.filter(category_id=3).order_by('name')}
    return render(request, 'product/accessory.html', context)

def accessory_by_price(request):
    context = {'products': Product.objects.filter(category_id=3).order_by('price')}
    return render(request, 'product/accessory.html', context)

#All spare parts views
def get_all_spareparts(request):
    context = {'products': Product.objects.filter(category_id=4)}
    return render(request, 'product/spere_parts.html', context)

def spareparts_by_name(request):
    context = {'products': Product.objects.filter(category_id=4).order_by('name')}
    return render(request, 'product/spere_parts.html', context)

def spareparts_by_price(request):
    context = {'products': Product.objects.filter(category_id=4).order_by('price')}
    return render(request, 'product/spere_parts.html', context)

#Get all products
def get_products(request):
    context = {'products': Product.objects.all()}
    return render(request, 'product/single_product.html', context)

@staff_member_required
def create_new_product(request):
    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)
        if form.is_valid():
            product = form.save()
            product_image = ProductImage(image=request.POST['image'], product=product)
            product_image.save()

            return redirect('product_index')
    else:
        form = ProductCreateForm()

    return render(request, 'product/create_product.html', {
        'form': form
    })

@staff_member_required
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('product_index')

@staff_member_required
def update_product(request, id):
    instance = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        form = ProductUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            product = form.save()
            product_image = ProductImage(image=request.POST['image'], product=product)
            product_image.save()

            return redirect('product_index')
    else:
        form = ProductUpdateForm(instance=instance)
    return render(request, 'product/update_product.html', {
        'form': form,
        'id': id
    })

#For admin to change product
@staff_member_required
def get_products_to_choose_from(request):
    context = {'products': Product.objects.all()}
    return render(request, 'product/choose_product_update.html', context)



# def get_subcategory_games(request, id):
#    product = Product.objects.all()
#    subcategories = ProductSubTypes.objects.all()
#    return render(request, 'product/games.html', {'subcategories': subcategories,
#                                                  'products': product})

