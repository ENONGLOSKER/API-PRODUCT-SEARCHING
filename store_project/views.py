from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from store_app.models import Product

class ProductListView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)
