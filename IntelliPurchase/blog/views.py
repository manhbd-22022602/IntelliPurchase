from django.shortcuts import render
from .models import Product
# Create your views here.
def list(request):
    Data = {'Products': Product.objects.all().order_by('-product_id')}
    return render(request, 'blog/blog.html', Data)