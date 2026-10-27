from django.http import HttpResponse
from .models import Article
from django.shortcuts import render


# def index(request):
#     return HttpResponse("Главная страница новостей")


# def index(request):
#     return render(request, "news/index.html")


# def index(request):
#     context = {
#         "title": "В городе открылся новый парк",
#         "text": (
#             "В центральной части города открылся новый парк "
#             "с прогулочными дорожками и детской площадкой."
#         ),
#         "author": "Редакция",
#     }
#     return render(request, "news/index.html", context)


def index(request):
    content = {
        "title": "Главные новости дня",
        # Берем из базы только опубликованные новости (is_published=True)
        "articles": Article.objects.filter(is_published=True)
    }
    return render(request, "news/index.html", content)


def category(request):
    content = {
        "category_name": "Технологии",
        "articles": [
            "Представлена новая модель смартфона",
            "Компания выпустила обновление программного обеспечения",
            "Учёные разработали новый процессор",
        ],
    }
    return render(request, "news/category.html", content)


def about(request):
    content = {
        "title": "О нас",
        "articles": [
            "IT Step",
            "Продаем бананы и людей",
            "Бананов нет",
        ],
    }
    return render(request, "news/about.html", content)      # ← about.html



def contacts(request):
    content = {
        "title": "Контакты",
        "articles": [
            "+375 29 123-45-67",
            "example@gmail.com",
            "@PavelDurov",
        ],
    }
    return render(request, "news/contacts.html", content)
