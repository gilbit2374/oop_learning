class Book():
    def __init__(self,title,author,isbn):#create a book
        self.title=title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False
    def check_out(self):#take a book
        if self.is_checked_out:
            print(f"The {self.title} book is already taken")
        else:
            self.is_checked_out=True
            print("The book is checked out have a good day!")
    def return_book(self):#return a book
        if self.is_checked_out:
            self.is_checked_out=False
            print(f"Thank you for returning the book have a good day!")
        else:
            print("The book is not checked out")
    def __str__(self):#display the book
        return f'the book title: {self.title}  author: {self.author}   isbn: {self.isbn}   is the book checked out: {"yes" if self.is_checked_out else "no"}'
TGG=Book("The Great Gatsby","F. Scott Fitzgerald",9780743273565)
NEF=Book('1984','George Orwell',9780451524935)
TKM=Book("To Kill a Mockingbird","Harper Lee",9780061120084)

class Library:
    def __init__(self):
        self.catalog = []
    def add_book(self, book):
        self.catalog.append(book)
    def find_book(self, search_isbn):
        for i in self.catalog:
            if i.isbn==search_isbn:
                return i
    def list_all_books(self):
        for i in self.catalog:
            print(f'{self.catalog.index(i)+1}. {i}')
        return ""


WL=Library()
WL.add_book(TGG)
WL.add_book(NEF)
WL.add_book(TKM)
print(WL.find_book(9780743273565))
WL.list_all_books()
TGG.check_out()
TGG.check_out()
WL.list_all_books()
TGG.return_book()
TGG.return_book()
WL.list_all_books()






