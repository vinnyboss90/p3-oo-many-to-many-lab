class Author:
    def __init__(self, name, books=None):
        self.name = name
        self.contracts = set()
        self.books = books if books else set()

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of the Book class")

        contract = Contract(self, book, date, royalties)
        self.contracts.add(contract)
        self.add_book(book)
        book.contracts.add(contract)
        book.add_author(self)

    def books(self):
        return {contract.book for contract in self.contracts}

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts)

    def add_book(self, book):
        self.books.add(book)

    def __repr__(self):
        return f'Author({self.name})'



class Book:
    def __init__(self, title, authors=None):
        self.title = title
        self.contracts = set()
        self.authors = authors if authors else set()



    def add_author(self, author):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of the Author class")
        self.authors.add(author)

    def __repr__(self):
        return f'Book({self.title})'

class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of the Author class")
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of the Book class")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)


    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

    def __repr__(self):
        return f'Contract {self.author}, {self.book}, Date: {self.date}, Royalties: {self.royalties} '
