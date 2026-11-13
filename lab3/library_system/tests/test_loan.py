from src.loan import Loan
from src.book import Book
from src.member import Member

def test_loan_complete():
    book = Book(isbn="1", title="Test")
    member = Member(member_id="M1", name="John")
    member.borrowed_books.append(book)
    loan = Loan(loan_id="L1", book=book, member=member)
    loan.complete_loan()
    assert loan.is_returned is True
    assert len(member.borrowed_books) == 0

def test_loan_calculate_fine():
    loan = Loan(loan_id="L1")
    assert loan.calculate_fine(5) == 7.5

def test_loan_extend():
    loan = Loan(loan_id="L1")
    loan.extend_loan(7) # Just covers the pass