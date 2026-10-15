from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("Главная страница новостей")


# def index(request):
#     return render(request, "News/index.html")


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
    context = {
        "title": "Главные новости дня",
        "articles": [
            "В городе открылся новый парк",
            "Учёные представили новую технологию",
            "В университете начался учебный год",
        ],
    }
    return render(request, "news/index.html", context)


def about(request):
    return HttpResponse("О нашем новостном издании")
