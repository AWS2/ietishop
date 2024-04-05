from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.
def product_list(request):
	productes = Producte.objects.all()
	return render(request, "product_list.html", {"productes":productes})
	