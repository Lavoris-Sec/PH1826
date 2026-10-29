from django.http import HttpResponse
from .models import Article
from django.shortcuts import render, get_object_or_404


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
    return render(request, "news/about.html", content)  # ← about.html


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


def article_detail(request, article_id):
    article = get_object_or_404(
        Article,
        id=article_id,
        is_published=True,
    )

    context = {
        "article": article,
    }

    return render(
        request,
        "news/article_detail.html",
        context,
    )


def category(request, category_name=None):
    if category_name is None:
        articles = Article.objects.filter(
            is_published=True
        ).order_by("-created_at")

        category_name = "Все категории"
    else:
        articles = Article.objects.filter(
            is_published=True,
            category__iexact=category_name,
        ).order_by("-created_at")

    context = {
        "articles": articles,
        "category_name": category_name,
    }

    return render(
        request,
        "news/category.html",
        context,
    )
