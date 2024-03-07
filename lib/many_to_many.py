from datetime import datetime

class Author:

    all = []

    def __init__(self,name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self ]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        if isinstance(book, Book):
            contract = Contract(self, book, date, royalties)
            return contract
        # comparing what was asked with what was in the test file was confusing.
        # test file stated isinstance(contract, Contract) which led me down a path of literally asserting contract, Contract
        # just needed to valideate the book was instance of Book

    def total_royalties(self):
        total_royalties = 0
        for contract in Contract.all:
            if self == contract.author:
                total_royalties += contract.royalties
        return total_royalties

        

class Book:
    
    def __init__(self,title):
        self.title = title


    def contracts(self):
        return [ contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:

    all = []
    
    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author) and isinstance(book, Book) and isinstance(date, str) and isinstance(royalties, int):
            self.author = author
            self.book = book
            self.date = date
            self.royalties = royalties
            Contract.all.append(self)
        else:
            raise Exception

    @classmethod
    def contracts_by_date(cls, date):
        target_date_dt = datetime.strptime(date, "%m/%d/%Y")
        
        # Filter contracts to those exactly matching the target_date
        filtered_contracts = [contract for contract in cls.all if datetime.strptime(contract.date, "%m/%d/%Y") == target_date_dt]
        
        # Return the filtered list (sorting is not necessary if we're only returning matches for a specific date)
        return filtered_contracts
        
   