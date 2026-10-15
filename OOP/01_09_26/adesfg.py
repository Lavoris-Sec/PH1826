class baseClass1:
    pass


class baseClass2:
    pass


class derivedClass(baseClass1, baseClass2):
    pass


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def show_info(self):
        return f"{self.title}\nAuthor - {self.author}\nPages - {self.pages}"


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


book1 = Book(title="War and piece",
             author="Lev Tolstoi",
             pages=900
             )

file1 = File(3, 4534534)

print(book1.show_info())
print(file1.show_info())

print("---")

ebook1 = Ebook("jgjtg", "hbdgfdf", 66, 89, 45852134323545682687675)

print(ebook1.show_info())

print(Ebook.mro())
