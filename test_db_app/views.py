from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import Http404
from test_db_app.models import Product


def index(request):
    all_products = Product.objects.all()
    context = {'all_products': all_products,}
    return render(request, "products/index.html", context)


def detail(request, prodcutId):
    # product = Product.objects.get(pk=prodcutId)    
    #except Product.DoesNotExist:
    #raise Http404("Product does not exist")
    
    product = get_object_or_404(Product,pk=prodcutId)
    
    context = {"product":product}
    return render(request, "products/product.html", context)




    """
    html =''
    for product in all_products:
        url = "/test_db_app/" +str(product.id)
        html += "<a href='"+ url +"'>"+product.productName+"</a><br>"
    
    """