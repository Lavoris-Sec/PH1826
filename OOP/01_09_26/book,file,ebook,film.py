class baseClass1:
    pass


class baseClass2:
    pass


class derivedClass(baseClass1, baseClass2):
    pass


class Book:
    def __init__(self, title, author, pages, feedbacksN):
        self.title = title
        self.author = author
        self.pages = pages
        self.feedbacksN = feedbacksN

    def __eq__(self, other):
        if self.author == other.author and self.title == other.title:
            return True
        else:
            return "111"

    def __ne__(self, other):
        if self.author != other.author and self.title == other.title:
            return True
        else:
            return "222"

    def __lt__(self, other):
        if self.author < other.author and self.title < other.title:
            return True
        else:
            return "333"

    def __le__(self, other):
        if self.author <= other.author and self.title <= other.title:
            return True
        else:
            return "444"

    def __gt__(self, other):
        if self.author > other.author and self.title > other.title:
            return True
        else:
            return "555"

    def __ge__(self, other):
        if self.author >= other.author and self.title >= other.title:
            return True
        else:
            return "666"

    # __eq__ ==
    # __ne__ !=
    # __lt__ <
    # __le__ <=
    # __gt__ >
    # __ge__ >=

    def __str__(self):
        return f"Title: {self.title}, author: {self.author},pages: {self.pages}\n" \
               f"Number of feedbacks by month(1-12): > {', '.join(map(str, self.feedbacksN))} <"

    def __getitem__(self, key):
        # if not (1 <= key <= 12):
        #     return -1
        return -1 if not (1 <= key <= 12) else f"{self.feedbacksN[key]}"
        # return f"{self.feedbacksN[key]}"

    def show_info(self):
        return f"{self.title}\nAuthor - {self.author}\nPages - {self.pages}\n"


class File:
    def __init__(self, size, src):
        self.size = size
        self.src = src

    def show_info(self):
        return f"\n{self.size} KB\n{self.src}"


class Ebook(Book, File):
    def __init__(self, title, author, pages, size, src):
        Book.__init__(self, title, author, pages)
        File.__init__(self, size, src)

    def show_info(self):
        return f"{Book.show_info(self) + File.show_info(self)}"


class Film:
    def __init__(self, originalTitle, director, genre):
        self.originalTitle = originalTitle
        self.director = director
        self.genre = genre

    def show_info(self):
        return f"{self.originalTitle}\nDirector - {self.director}\nGenre - {self.genre}\n"


# book1 = Book(title="War and piece",
#              author="Lev Tolstoi",
#              pages=900
#              )
#
# file1 = File(3, 4534534)
#
# print(book1.show_info())
# print(file1.show_info())
#
# print("---")
#
# ebook1 = Ebook(title="jgjtg",
#                author="hbdgfdf",
#                pages=66,
#                size=89,
#                src=45852134323545682687675
#                )
#
# print(ebook1.show_info())
#
# print(Ebook.mro())

sss = [1, 22, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

book1 = Book(title="War and piece",
             author="Lev Tolstoi",
             pages=900,
             feedbacksN=sss
             )

book2 = Book(title="ce",
             author="i",
             pages=0,
             feedbacksN=sss
             )

film1 = Film(
    originalTitle="Interstellar",
    director="Christopher Nolan",
    genre="sci-fi"
)

# print(book1.show_info())
# print(film1.show_info())
# for item in (film1, book1):
#     print(item.show_info())

# print(book1+book2)

# print(book1 == book2)


print(book1)
print(book1[20])
