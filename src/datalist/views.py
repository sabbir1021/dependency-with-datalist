from ast import Sub
from django.shortcuts import render, redirect
from .models import Category, SubCategory , Product
from django.db import IntegrityError
from django.contrib import messages


def datalist(request):
    categorylist = Category.objects.all()
    subcategorylist = SubCategory.objects.all()
    if request.method=="POST":
        name=request.POST.get("name")
        category=request.POST.get("category")
        subcategory=request.POST.get("subcategory")
        if not Category.objects.filter(name=category).exists():
            category = Category.objects.create(name=category)
        else:
            category = Category.objects.get(name=category)
        if not SubCategory.objects.filter(name=subcategory).exists():
            subcategory = SubCategory.objects.create(name=subcategory, category=category)
        else:
            subcategory = SubCategory.objects.get(name=subcategory)
        try:
            Product.objects.create(name=name, category=category, subcategory=subcategory)
            messages.success(request, 'successfully created ')
        except IntegrityError as e:
            messages.success(request, 'Already exists this product with category and sub category')
            return redirect("datalist:datalist")
    return render(request, "index.html", {"category":categorylist, "subcategory":subcategorylist})