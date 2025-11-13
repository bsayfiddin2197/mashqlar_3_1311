class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.__available = available  

    def is_available(self):
        """Kitob mavjudligini tekshiradi (faqat Library orqali ishlatiladi)"""
        return self.__available

    def borrow(self):
        """Kitobni olish"""
        if self.__available:
            self.__available = False
            print(f"Kitob olindi: {self.title}")
        else:
            print(f"Xatolik: '{self.title}' hozir mavjud emas.")

    def return_book(self):
        """Kitobni qaytarish"""
        if not self.__available:
            self.__available = True
            print(f"Kitob qaytarildi: {self.title}")
        else:
            print(f"'{self.title}' allaqachon kutubxonada bor.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Kutubxonaga yangi kitob qo‘shish"""
        self.books.append(book)
        print(f"Yangi kitob qo‘shildi: {book.title} - {book.author}")

    def show_books(self):
        """Barcha kitoblar ro‘yxatini ko‘rsatish"""
        print("\nKutubxonadagi kitoblar:")
        for book in self.books:
            status = "Mavjud" if book.is_available() else "Band"
            print(f"- {book.title} ({book.author}) — {status}")

    def borrow_book(self, title):
        """Foydalanuvchi nomi bilan kitob olish"""
        for book in self.books:
            if book.title == title:
                book.borrow()
                return
        print(f"'{title}' nomli kitob topilmadi.")

    def return_book(self, title):
        """Kitobni qaytarish"""
        for book in self.books:
            if book.title == title:
                book.return_book()
                return
        print(f"'{title}' nomli kitob topilmadi.")


class User:
    def __init__(self, name, library):
        self.name = name
        self.library = library

    def borrow_book(self, title):
        """User faqat Library orqali kitob oladi"""
        print(f"\n{self.name} kitob olmoqchi: {title}")
        self.library.borrow_book(title)

    def return_book(self, title):
        """User faqat Library orqali kitobni qaytaradi"""
        print(f"\n{self.name} kitobni qaytarmoqchi: {title}")
        self.library.return_book(title)


lib = Library()
book1 = Book("Python Asoslari", "Aliyev")
book2 = Book("Sun'iy intellekt", "Valiyev")
book3 = Book("Algoritmlar", "Karimov")

lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)

lib.show_books()

user1 = User("Dilshod", lib)
user1.borrow_book("Python Asoslari")
user1.borrow_book("Python Asoslari")  

lib.show_books()

user1.return_book("Python Asoslari")
lib.show_books()
