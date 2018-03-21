from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from test_db_app.models import Product


def index(request):
    all_products = Product.objects.all()
    context = {'all_products': all_products,}
    return render(request, "products/index.html", context)


def detail(request, prodcutId):
    return HttpResponse("<h2>The Id of the prodcut is: " + prodcutId +"</h2>")




    """
    html =''
    for product in all_products:
        url = "/test_db_app/" +str(product.id)
        html += "<a href='"+ url +"'>"+product.productName+"</a><br>"
    
    """