from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from product.forms.product_form import ProductCreateForm, ProductUpdateForm
from product.models import Product
from product.models import ProductImage



# Create your views here.
def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        product = list(Product.objects.filter(name__icontains=search_filter).values)
        return JsonResponse({'data': product})
    context = {'products': Product.objects.all()}
    return render(request, 'product/index.html', context)

def index_by_name(request):
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'product/index.html', context)

def index_by_price(request):
    context = {'products': Product.objects.all().order_by('price')}
    return render(request, 'product/index.html', context)


# def info_index(request):
#    context = {'products': Product.objects.all()}
#    return render(request, 'product/info.html', context)

# /product/1
def get_product_by_id(request, id):
   context = {'products': Product.objects.all()}
   return render(request, 'product/info.html',  {
       'product': get_object_or_404(Product, pk=id)
   })

def get_all_games(request):
    context = {'products': Product.objects.all()}
    return

#Get all products
def get_products(request):
    context = {'products': Product.objects.all()}
    return render(request, 'product/single_product.html', context)

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

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('product_index')

def update_product(request, id):
    instance = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        form = ProductUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('get_product_by_id', id=id)
    else:
        form = ProductUpdateForm(instance=instance)
    return render(request, 'product/update_product.html', {
        'form': form,
        'id': id
    })

#For admin to change product
def get_products_to_choose_from(request):
    context = {'products': Product.objects.all()}
    return render(request, 'product/choose_product_update.html', context)