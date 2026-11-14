# Lab 3: Library Management System

This project implements a large-scale Object-Oriented model for a Library Management System. It demonstrates encapsulation, associations, custom exceptions, and domain logic across 50 classes.

## Architecture Overview

The system is divided into several subsystems:
- **Core Management**: `Library`, `Librarian`, `Member`, `Manager`
- **Catalog & Items**: `Book`, `Magazine`, `DVD`, `Author`, `Publisher`, `Genre`
- **Loans & Transactions**: `Loan`, `Reservation`, `Fine`, `Receipt`, `Transaction`
- **Storage**: `Shelf`, `Section`, `Building`, `Address`
- **Staff**: `Staff`, `Janitor`, `SecurityGuard`, `ITTechnician`, `Accountant`
- **Finance**: `FinanceManager`, `Budget`, `ExpenseTracker`, `Report`
- **Utilities**: `Notification`, `Event`, `Schedule`, `Catalog`, `Database`, `Logger`, `SearchEngine`, `Inventory`, `Procurement`, `Supplier`, `BookBinder`, `Restoration`, `DigitalArchive`, `Volunteer`, `LibraryEvent`, `NotificationService`, `BookCondition`, `LoanHistory`, `MemberCard`, `LibraryCard`

## Class Blueprint

| Class | Fields | Methods | Associations |
|---|---|---|---|
| Library | 5 | 7 | Member, Book, Staff, Loan |
| Librarian | 4 | 4 | Loan, Member, Book |
| Member | 5 | 5 | Loan, Reservation, Fine |
| Manager | 3 | 3 | Staff, Library |
| Book | 6 | 4 | Author, Publisher, Genre |
| Magazine | 3 | 2 | Publisher |
| DVD | 2 | 2 | - |
| Author | 3 | 2 | Book |
| Publisher | 3 | 2 | Book |
| Genre | 2 | 1 | Book |
| Review | 3 | 2 | Book, Member |
| Rating | 2 | 1 | Review |
| Loan | 5 | 3 | Book, Member, Librarian |
| Reservation | 4 | 3 | Book, Member |
| Fine | 3 | 3 | Member, Loan |
| Receipt | 3 | 2 | Loan |
| Transaction | 3 | 2 | - |
| Shelf | 3 | 3 | Section |
| Section | 2 | 2 | Building |
| Building | 3 | 3 | - |
| Address | 4 | 2 | Building |
| Staff | 3 | 2 | - |
| Janitor | 2 | 2 | - |
| SecurityGuard | 2 | 2 | - |
| ITTechnician | 2 | 3 | - |
| Accountant | 2 | 2 | Fine, Receipt |
| FinanceManager | 2 | 2 | Fine, Receipt |
| Budget | 3 | 2 | - |
| ExpenseTracker | 2 | 2 | - |
| Report | 3 | 2 | Library |
| Notification | 3 | 2 | Member |
| Event | 3 | 2 | - |
| Schedule | 3 | 2 | - |
| Catalog | 2 | 3 | Book |
| Database | 2 | 3 | - |
| Logger | 2 | 2 | - |
| BookCondition | 2 | 1 | Book |
| LoanHistory | 1 | 2 | Loan |
| MemberCard | 2 | 2 | Member |
| LibraryCard | 2 | 2 | Member |
| NotificationService | 2 | 2 | Notification |
| SearchEngine | 2 | 3 | Book |
| Inventory | 2 | 2 | Book |
| Procurement | 2 | 2 | Supplier |
| Supplier | 2 | 2 | Book |
| BookBinder | 2 | 2 | Book |
| Restoration | 2 | 2 | Book |
| DigitalArchive | 2 | 3 | Book |
| Volunteer | 2 | 2 | Event |
| LibraryEvent | 2 | 2 | Event |

## Custom Exceptions (12)
1. `LibraryException` (Base)
2. `BookNotFoundException`
3. `BookAlreadyBorrowedException`
4. `MemberNotFoundException`
5. `MaxBooksExceededException`
6. `FineNotPaidException`
7. `InvalidBookDataException`
8. `LoanExpiredException`
9. `ReservationConflictException`
10. `StaffNotAvailableException`
11. `InvalidMemberDataException`
12. `PaymentFailedException`

## Domain Logic Example
The `Library` class manages the catalog, members, and loans. When a `Member` requests a `Book`, the `Library` checks if the book is available. If the member has unpaid fines, a `FineNotPaidException` is thrown. If the book is already borrowed, a `BookAlreadyBorrowedException` is thrown.
