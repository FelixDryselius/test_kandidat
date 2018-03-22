from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import Http404
from .models import Product, Batch


def index(request):
    all_products = Product.objects.all()
    context = {'all_products': all_products,}
    return render(request, "products/index.html", context)


def detail(request, productId):
    # product = Product.objects.get(pk=productId)    
    #except Product.DoesNotExist:
    #raise Http404("Product does not exist")
    
    product = get_object_or_404(Product,pk=productId)
    
    context = {"product":product}
    return render(request, "products/product.html", context)


def favorite(request, productId):
    product = get_object_or_404(Product,pk=productId)
    
    try:
        selectedBatch = product.batch_set.get(pk=request.POST['batch'])
    except(KeyError, Batch.DoesNotExist):
        return render(request, "products/product.html", {
            "product": product,
            'error_message': 'YOU DID NOT SELECT A BATCH...',
            })
    else:
        selectedBatch.is_favorite = True
        selectedBatch.save()
    return render(request, "products/product.html", { "product": product })
    

"""
html =''
for product in all_products:
    url = "/test_db_app/" +str(product.id)
    html += "<a href='"+ url +"'>"+product.productName+"</a><br>"

"""