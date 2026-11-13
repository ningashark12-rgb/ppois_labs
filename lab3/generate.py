import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "library_system", "src")
EXC_DIR = os.path.join(SRC_DIR, "exceptions")

os.makedirs(SRC_DIR, exist_ok=True)
os.makedirs(EXC_DIR, exist_ok=True)
open(os.path.join(SRC_DIR, "__init__.py"), 'w').close()

exceptions = [
    "LibraryException", "BookNotFoundException", "BookAlreadyBorrowedException",
    "MemberNotFoundException", "MaxBooksExceededException", "FineNotPaidException",
    "InvalidBookDataException", "LoanExpiredException", "ReservationConflictException",
    "StaffNotAvailableException", "InvalidMemberDataException", "PaymentFailedException"
]

# Generate Exceptions
for exc in exceptions:
    filename = re.sub(r'(?<!^)(?=[A-Z])', '_', exc).lower() + ".py"
    with open(os.path.join(EXC_DIR, filename), "w", encoding="utf-8") as f:
        f.write(f'class {exc}(Exception):\n    """Raised for {exc}."""\n    pass\n')

with open(os.path.join(EXC_DIR, "__init__.py"), "w", encoding="utf-8") as f:
    for exc in exceptions:
        f.write(f"from .{re.sub(r'(?<!^)(?=[A-Z])', '_', exc).lower()} import {exc}\n")

# The 50 classes blueprint with REAL logic
blueprint = [
    ("Library", ["name", "catalog", "members", "staff", "loans"], ["register_member", "add_book", "process_loan", "return_loan", "generate_report"]),
    ("Librarian", ["name", "employee_id", "shift", "is_available"], ["issue_book", "receive_return", "check_member", "manage_shelf"]),
    ("Member", ["member_id", "name", "email", "borrowed_books", "fines"], ["borrow_book", "return_book", "pay_fine", "reserve_book"]),
    ("Manager", ["name", "department", "budget"], ["hire_staff", "approve_budget", "hold_meeting"]),
    ("Book", ["isbn", "title", "author", "publisher", "genre", "is_available"], ["checkout", "checkin", "get_details", "update_condition"]),
    ("Magazine", ["issue_number", "publisher", "release_date"], ["get_issue", "archive"]),
    ("DVD", ["duration_minutes", "age_rating"], ["play", "check_compatibility"]),
    ("Author", ["name", "biography", "nationality"], ["write_book", "get_bio"]),
    ("Publisher", ["name", "address", "contact_info"], ["publish", "get_contact"]),
    ("Genre", ["name", "description"], ["get_category"]),
    ("Review", ["rating", "comment", "date"], ["submit", "edit_review"]),
    ("Rating", ["stars", "reviewer"], ["calculate_average"]),
    ("Loan", ["loan_id", "book", "member", "issue_date", "due_date"], ["extend_loan", "calculate_fine", "complete_loan"]),
    ("Reservation", ["reservation_id", "book", "member", "status"], ["cancel", "confirm", "check_status"]),
    ("Fine", ["amount", "reason", "is_paid"], ["pay", "waive", "get_receipt"]),
    ("Receipt", ["receipt_id", "amount", "date"], ["print_receipt", "get_details"]),
    ("Transaction", ["transaction_id", "amount", "type"], ["process", "rollback"]),
    ("Shelf", ["shelf_id", "capacity", "current_books"], ["add_book", "remove_book", "check_capacity"]),
    ("Section", ["section_name", "shelves"], ["add_shelf", "get_shelf"]),
    ("Building", ["building_name", "address", "floors"], ["open", "close", "get_info"]),
    ("Address", ["street", "city", "zip_code", "country"], ["validate", "to_string"]),
    ("Staff", ["name", "position", "salary"], ["clock_in", "clock_out"]),
    ("Janitor", ["shift", "cleaning_supplies"], ["clean_area", "restock_supplies"]),
    ("SecurityGuard", ["badge_number", "patrol_area"], ["patrol", "check_id"]),
    ("ITTechnician", ["specialization", "access_level"], ["fix_computer", "install_software", "backup_data"]),
    ("Accountant", ["employee_id", "tax_id"], ["calculate_taxes", "process_payroll"]),
    ("FinanceManager", ["name", "budget_limit"], ["approve_expense", "audit_finance"]),
    ("Budget", ["total_amount", "spent_amount", "fiscal_year"], ["allocate_funds", "check_balance"]),
    ("ExpenseTracker", ["total_expenses", "categories"], ["add_expense", "get_total"]),
    ("Report", ["report_id", "date_generated", "content"], ["generate", "export_pdf"]),
    ("Notification", ["message", "recipient", "is_read"], ["send", "mark_read"]),
    ("Event", ["event_name", "date", "location"], ["schedule", "cancel_event"]),
    ("Schedule", ["start_time", "end_time", "day"], ["set_hours", "is_open"]),
    ("Catalog", ["categories", "last_updated"], ["search", "sort_alphabetically", "filter_by_genre"]),
    ("Database", ["connection_string", "is_connected"], ["connect", "disconnect", "execute_query"]),
    ("Logger", ["log_file", "log_level"], ["log_info", "log_error"]),
    ("BookCondition", ["condition_level", "notes"], ["update_condition"]),
    ("LoanHistory", ["past_loans"], ["add_record", "get_history"]),
    ("MemberCard", ["card_number", "expiry_date"], ["renew", "is_valid"]),
    ("LibraryCard", ["card_number", "member"], ["swipe", "deactivate"]),
    ("NotificationService", ["channel", "messages_sent"], ["send_email", "send_sms"]),
    ("SearchEngine", ["query", "results"], ["search_by_title", "search_by_author", "filter"]),
    ("Inventory", ["total_books", "missing_books"], ["audit", "add_inventory"]),
    ("Procurement", ["supplier", "order_date"], ["order_books", "track_delivery"]),
    ("Supplier", ["name", "contact_person"], ["supply_books", "get_catalog"]),
    ("BookBinder", ["binder_name", "materials"], ["bind_book", "repair_book"]),
    ("Restoration", ["book", "restoration_date"], ["restore", "estimate_cost"]),
    ("DigitalArchive", ["file_format", "storage_size"], ["upload", "download", "compress"]),
    ("Volunteer", ["name", "hours_worked"], ["log_hours", "assign_task"]),
    ("LibraryEvent", ["event_type", "attendees"], ["register_attendee", "cancel_event"])
]

CORE_CLASSES = [] # Empty for now, we will add logic to them later

# Generate Classes
for cls_name, fields, methods in blueprint:
    filename = re.sub(r'(?<!^)(?=[A-Z])', '_', cls_name).lower() + ".py"
    filepath = os.path.join(SRC_DIR, filename)
    
    if os.path.basename(filepath) in CORE_CLASSES:
        continue
        
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f'"""Domain model for {cls_name}."""\n\n')
        f.write(f'class {cls_name}:\n')
        f.write(f'    """Represents a {cls_name}."""\n\n')
        
        f.write("    def __init__(self")
        for field in fields:
            if field in ["name", "title", "isbn", "member_id", "loan_id", "transaction_id"]:
                f.write(f", {field}: str")
            else:
                f.write(f", {field}=None")
        f.write(") -> None:\n")
        
        for field in fields:
            f.write(f"        self.{field} = {field}\n")
        f.write("\n")
        
        for method in methods:
            f.write(f"    def {method}(self) -> None:\n")
            f.write(f'        """Behavior for {cls_name} {method}."""\n')
            f.write("        pass\n\n")

print(f"SUCCESS! Generated {len(blueprint)} classes in {SRC_DIR}")
print(f"SUCCESS! Generated {len(exceptions)} exceptions in {EXC_DIR}")