import json
from django.http import JsonResponse

from django.views import View

from products.models import Category, Drink

class CategoryView(View):
    def get(self, request):
        result = list(Category.objects.values())

        return JsonResponse({'result': result}, status='200')

class DrinkView(View):
    def get(self, request):
        result = list(Drink.objects.values())

        return JsonResponse({'result': result}, status='200')
