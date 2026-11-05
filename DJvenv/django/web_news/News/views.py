from django.http import HttpResponse
from .models import Article
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ArticleForm


def index(request):
    content = {
        "title": "Главные новости дня",
        # Берем из базы только опубликованные новости (is_published=True)
        "articles": Article.objects.filter(is_published=True)
    }
    return render(request, "news/index.html", content)


# def category(request):
#     content = {
#         "category_name": "Технологии",
#         "articles": [
#             "Представлена новая модель смартфона",
#             "Компания выпустила обновление программного обеспечения",
#             "Учёные разработали новый процессор",
#         ],
#     }
#     return render(request, "news/category.html", content)


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


def edit_article(request, article_id):
    article = get_object_or_404(
        Article,
        id=article_id
    )

    if request.method == "POST":
        form = ArticleForm(
            request.POST,
            request.FILES,
            instance=article
        )

        if form.is_valid():
            article = form.save()

            if article.is_published:
                return redirect(
                    "article_detail",
                    article_id=article.id
                )

            return redirect("home")

    else:
        form = ArticleForm(instance=article)

    context = {
        "form": form,
        "article": article,
    }

    return render(
        request,
        "news/edit_article.html",
        context
    )


# def test_form(request):
#     if request.method == "POST":
#         title = request.POST.get("title")
#         content = request.POST.get("content")
#
#         print("Заголовок:", title)
#         print("Текст:", content)
#
#     return render(
#         request,
#         "news/test_form.html",
#     )

def test_form(request):
    context = {}

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        context = {
            "title": title,
            "content": content,
        }

    return render(
        request,
        "news/test_form.html",
        context,
    )


def add_article(request):
    if request.method == "POST":

        form = ArticleForm(request.POST)

        if form.is_valid():
            article = form.save()

            return redirect("article_created")

    else:
        form = ArticleForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "news/add_article.html",
        context,
    )


def article_created(request):
    return render(
        request,
        "news/article_created.html",
    )
