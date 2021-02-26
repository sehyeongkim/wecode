from django.urls import path

from products.views import CategoryView, DrinkView

urlpatterns = [
        path('/category', CategoryView.as_view()),
        path('/drink', DrinkView.as_view())
    ]

