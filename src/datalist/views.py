from ast import Sub
from unicodedata import category
from django.shortcuts import render, HttpResponse
from .models import Category, SubCategory , Product
from .forms import ProductForm

# Create your views here.

def datalist(request):
    categorylist = Category.objects.all()
    subcategorylist = SubCategory.objects.all()
    if request.method=="POST":
        name=request.POST.get("name")
        category=request.POST.get("category")
        subcategory=request.POST.get("subcategory")
        # print(name,category,subcategory)
        if not Category.objects.filter(name=category).exists():
            category = Category.objects.create(name=category)
            if not SubCategory.objects.filter(name=subcategory).exists():
                subcategory = SubCategory.objects.create(name=subcategory, category=category)
                Product.objects.create(name=name, category=category,subcategory=subcategory)

        else:
            category = Category.objects.get(name=category)
            if not SubCategory.objects.filter(name=subcategory).exists():
                subcategory = SubCategory.objects.create(name=subcategory, category=category)
                Product.objects.create(name=name, category=category,subcategory=subcategory)
            else:
                subcategory = SubCategory.objects.get(name=subcategory)
                try:
                    Product.objects.create(name=name, category=category, subcategory=subcategory)
                except Exception as e:
                    return HttpResponse("unique problem")
    
        
        
       
    return render(request, "index.html", {"category":categorylist, "subcategory":subcategorylist})