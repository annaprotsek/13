class Book:
    def __init__(self, title, author, publisher, year, pages):
        """Конструктор класу"""
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.pages = pages

    def change_year(self, new_year):
        """Метод для зміни року видання"""
        self.year = new_year

    def change_pages(self, new_pages):
        """Метод для зміни кількості сторінок"""
        self.pages = new_pages

    def __str__(self):
        """Форматований вивід інформації про книгу"""
        return f"Назва: {self.title}, Автор: {self.author}, Видавництво: {self.publisher}, Рік: {self.year}, Сторінок: {self.pages}"
class Library:
    def __init__(self):
        """Конструктор для списку книг"""
        self.books = []

    def add_book(self, book):
        """Додати книгу до списку"""
        self.books.append(book)

    def remove_book(self, title):
        """Видалити книгу зі списку за назвою"""
        self.books = [book for book in self.books if book.title != title]

    def display_books(self):
        """Вивести список усіх книг"""
        if not self.books:
            print("Список книг порожній.")
        else:
            for book in self.books:
                print(book)
library = Library()
book1 = Book("Гаррі Поттер", "Дж. К. Роулінг", "Блумсбері", 1997, 309)
book2 = Book("1984", "Джордж Орвелл", "Сейкер і Уорбург", 1949, 328)

library.add_book(book1)
library.add_book(book2)
print("Список книг у бібліотеці:")
library.display_books()
book1.change_year(1998)
book1.change_pages(320)
library.remove_book("1984")
print("\nОновлений список книг:")
library.display_books()
