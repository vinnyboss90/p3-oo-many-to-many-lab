from many_to_many import Author, Book, Contract
import pytest

def test_author_and_book():
    """Test init author and book"""
    author = Author("John Doe")
    book = Book("Test Book")

    assert author.name == "John Doe"
    assert len(author.contracts) == 0
    assert len(author.books) == 0
    assert isinstance(author.books, set)
    assert isinstance(author.contracts, set)
    assert isinstance(book.authors, set)
    assert isinstance(book.contracts, set)

    assert book.title == "Test Book"
    assert len(book.contracts) == 0
    assert len(book.authors) == 0

def test_author_sign_contract():
    """Test author sign contract"""

    author = Author("John Doe")
    book = Book("Test Book")
    date = "2023-05-03"
    royalties = 100

    author.sign_contract(book, date, royalties)

    assert len(author.contracts) == 1
    assert book in author.books

    contract = next(iter(author.contracts))
    assert contract.author == author
    assert contract.book == book
    assert contract.date == date
    assert contract.royalties == royalties

    assert len(book.contracts) == 1
    assert author in book.authors

def test_add_author():
    """Test book.add_author"""

    # Test when adding a valid Author object
    author = Author("John Doe")
    book = Book("Test Book 1")
    book.add_author(author)
    assert author in book.authors

    # Invalid object
    with pytest.raises(TypeError):
        book.add_author("Not an Author object")

def test_total_royalties():
    """Test total_royalties"""

    author = Author("John Doe")
    book1 = Book("Test Book 1")
    book2 = Book("Test Book 2")
    date = "2023-05-03"

    author.sign_contract(book1, date, 100)
    author.sign_contract(book2, date, 200)

    assert author.total_royalties() == 300

def test_contracts_by_date():
    """Test Contract.contracts_by_date"""

    author = Author("John Doe")
    book = Book("Test Book")
    date1 = "2023-05-01"
    date2 = "2023-05-02"

    author.sign_contract(book, date1, 100)
    author.sign_contract(book, date2, 200)

    contracts_date1 = Contract.contracts_by_date(date1)
    contracts_date2 = Contract.contracts_by_date(date2)

    assert len(contracts_date1) == 1
    assert contracts_date1[0].date == date1
    assert contracts_date1[0].royalties == 100

    assert len(contracts_date2) == 1
    assert contracts_date2[0].date == date2
    assert contracts_date2[0].royalties == 200
