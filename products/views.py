import json
from django.http import JsonResponse

from django.views import View

from products.models import Menu, Category, Drink

class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        result     = []
        for category in categories:
            result.append({
                'name': category.name,
                'menu': category.menu.name
                })
            
        return JsonResponse({'result': result}, status = 200)

    def post(self, request):
        data     = json.loads(request.body)
        menu     = Menu.objects.create(name = data['menu'])
        category = Category.objects.create(
                name = data['category'],
                menu = menu
                )
        
        return JsonResponse({'MESSAGE': 'SUCCESS'}, status = 200)


class DrinkView(View):
    def get(self, request):
        drinks = Drink.objects.all()
        result = []
        for drink in drinks:
            result.append({
                'name': drink.name,
                'category': drink.category.name
                })
            
        return JsonResponse({'result': result}, status = 200)

    def post(self, request):
        data     = json.loads(request.body)
        menu     = Menu.objects.create(name = data['menu'])
        category = Category.objects.create(
                name = data['category'],
                menu = menu
                )
        drink = Drink.objects.create(
            name     = data['name'],
            category = category
            )
        
        return JsonResponse({'MESSAGE': 'SUCCESS'}, status = 200)
