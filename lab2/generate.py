import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "transport_company", "src")
EXC_DIR = os.path.join(SRC_DIR, "exceptions")

os.makedirs(SRC_DIR, exist_ok=True)
os.makedirs(EXC_DIR, exist_ok=True)
open(os.path.join(SRC_DIR, "__init__.py"), 'w').close()

# 1. The Blueprint with realistic fields and methods
# Format: ClassName, Fields, Methods, Parent Class (if any)
blueprint = [
    ("Accountant", ["name", "salary", "bank_account", "hire_date"], ["process_payment", "calculate_tax", "issue_invoice", "audit_books"]),
    ("Address", ["street", "city", "zip_code", "country"], ["to_string", "validate_address", "get_gps", "distance_to"]),
    ("BankAccount", ["account_number", "balance", "owner_name", "currency"], ["deposit", "withdraw", "transfer", "get_balance"]),
    ("Cargo", ["weight", "volume", "description", "is_fragile"], ["calculate_cost", "validate_weight", "get_description"]),
    ("Client", ["name", "phone", "email"], ["place_order", "make_payment", "get_contact_info", "update_details"]),
    ("CompanyFinance", ["total_revenue", "total_expenses", "tax_rate"], ["calculate_profit", "generate_report", "apply_tax", "forecast"]),
    ("CustomerService", ["open_tickets", "resolved_tickets", "feedback_score", "staff"], ["open_ticket", "resolve_ticket", "rate_service", "get_complaints"]),
    ("Dispatcher", ["name", "shift", "current_orders", "radio_channel"], ["assign_order", "call_driver", "track_delivery", "handle_emergency"]),
    ("Driver", ["name", "license", "is_available", "experience_years", "rating"], ["accept_order", "decline_order", "update_status", "get_rating"]),
    ("DrivingLicense", ["number", "category", "issue_date", "expiry_date"], ["is_valid", "renew", "get_category"]),
    ("Employee", ["name", "position", "salary", "hire_date"], ["work", "take_break", "get_payslip", "resign"]),
    ("ExpressDelivery", ["speed_priority", "guaranteed_time", "extra_fee", "order"], ["upgrade_speed", "calculate_extra_cost", "track_eta"]),
    ("FragileCargo", ["fragility_level", "special_packaging", "handling_instructions"], ["apply_packaging", "warn_handler", "charge_fragile_fee"]),
    ("GPSPosition", ["latitude", "longitude", "timestamp"], ["update_position", "get_distance", "is_same_location"]),
    ("HRManager", ["name", "department", "employees", "budget"], ["hire_employee", "fire_employee", "evaluate_staff", "approve_vacation"]),
    ("Insurance", ["policy_number", "premium", "coverage_amount", "expiry_date"], ["file_claim", "calculate_premium", "renew_policy"]),
    ("Invoice", ["invoice_number", "amount", "issue_date", "is_paid"], ["mark_paid", "generate_pdf", "apply_discount"]),
    ("LogisticsManager", ["name", "region", "routes", "warehouses"], ["optimize_route", "manage_warehouse", "plan_logistics", "coordinate_supply"]),
    ("Machine", ["machine_id", "type", "status"], ["start", "stop", "check_status", "repair"]),
    ("MaintenanceRecord", ["date", "description", "cost"], ["add_note", "calculate_cost", "schedule_next"]),
    ("Manager", ["name", "department", "team_size"], ["assign_task", "review_performance", "approve_budget", "conduct_meeting"]),
    ("Mechanic", ["name", "specialization", "hourly_rate"], ["fix_vehicle", "inspect_engine", "write_report", "order_parts"]),
    ("Metrics", ["total_distance", "avg_speed", "fuel_used", "time_elapsed"], ["calculate_efficiency", "track_progress", "reset_metrics", "get_summary"]),
    ("Order", ["order_id", "client", "cargo", "driver", "vehicle", "status", "price"], ["assign_driver", "assign_vehicle", "calculate_price", "complete_order", "cancel_order"]),
    ("Payment", ["amount", "payment_method", "date", "is_successful"], ["process_payment", "refund", "validate_card", "get_receipt"]),
    ("PerishableCargo", ["expiry_time", "temperature_required", "spoilage_risk"], ["check_temperature", "is_expired", "calculate_time_left"]),
    ("Route", ["start_address", "end_address", "distance_km", "estimated_time"], ["calculate_distance", "optimize_for_traffic", "get_eta", "add_waypoint"]),
    ("Salary", ["base_amount", "bonus", "overtime_hours", "tax_deduction"], ["calculate_total", "apply_tax", "add_bonus", "generate_payslip"]),
    ("ServiceManagement", ["total_feedback", "avg_rating", "loyalty_program", "active_tickets"], ["collect_feedback", "analyze_quality", "reward_loyalty_customers", "escalate_issue"]),
    ("StorageUnit", ["unit_id", "zone", "capacity_cubic_meters", "current_usage"], ["store_cargo", "retrieve_cargo", "check_capacity", "empty_unit"]),
    ("TrackingSystem", ["active_trackings", "history"], ["start_tracking", "update_location", "stop_tracking", "get_history"]),
    ("Trailer", ["max_weight", "volume", "number_of_axles"], ["attach_to_truck", "detach", "check_load", "get_capacity"]),
    ("TransportCompany", ["name", "fleet", "employees", "clients", "orders"], ["hire_staff", "buy_vehicle", "register_client", "process_order", "generate_report", "pay_salaries", "calculate_profit"]),
    ("Truck", ["max_weight", "axles"], ["start_engine", "stop_engine", "load_cargo", "unload_cargo"]),
    ("Van", ["max_volume", "sliding_door"], ["open_door", "load_packages", "deliver_parcel", "refuel"]),
    ("Vehicle", ["plate_number", "brand", "model", "year", "is_available", "mileage"], ["start", "stop", "refuel", "schedule_maintenance", "update_mileage"]),
    ("Warehouse", ["address", "capacity", "current_stock", "manager"], ["receive_goods", "ship_goods", "check_inventory", "optimize_space"]),
    ("WarehouseManager", ["name", "warehouse", "staff_count"], ["hire_workers", "manage_inventory", "report_to_logistics", "ensure_safety"]),
    ("ExpenseTracker", ["total_expenses", "categories"], ["add_expense", "get_total", "categorize", "export_data"]),
    ("ProfitAnalyzer", ["revenue", "expenses", "profit_margin", "growth_rate"], ["calculate_profit", "analyze_trends", "forecast", "generate_report"]),
    ("TaxCalculator", ["tax_rate", "deductions"], ["calculate_tax", "apply_exemption", "get_effective_rate"]),
    ("PerformanceMetric", ["metric_name", "value", "unit"], ["update_value", "compare", "get_status"]),
    ("FuelConsumption", ["liters_used", "distance_covered", "fuel_type"], ["calculate_mpg", "estimate_cost", "track_refill"]),
    ("TrafficInfo", ["severity", "location", "delay_minutes"], ["get_delay", "is_critical", "suggest_alternate"]),
    ("CustomerFeedback", ["rating", "comment"], ["submit", "analyze", "respond", "escalate"]),
    ("ServiceQualityMonitor", ["average_rating", "total_reviews"], ["analyze_feedback", "flag_issues", "report_metrics"]),
    ("LoyaltyProgram", ["points", "tier"], ["add_points", "redeem_points", "upgrade_tier"]),
    ("StorageZone", ["zone_name", "capacity", "temperature_controlled", "current_load"], ["assign_unit", "check_space", "monitor_temperature"]),
    ("Rack", ["rack_id", "max_weight", "shelf_count"], ["store_item", "retrieve_item", "check_weight_limit"]),
    ("InsurancePolicy", ["policy_id", "premium", "coverage", "expiry"], ["renew", "claim", "calculate_premium"])
]

# 2. Generate Exceptions
exceptions = [
    "TransportException", "InsufficientFundsException", "InvalidClientDataException",
    "OrderNotFoundException", "InvalidOrderDataException", "InvalidCargoDataException",
    "CargoOverweightException", "VehicleOverloadException", "VehicleNotAvailableException",
    "DriverNotAvailableException", "InvalidLicenseException", "MaintenanceRequiredException"
]

for exc in exceptions:
    filename = re.sub(r'(?<!^)(?=[A-Z])', '_', exc).lower() + ".py"
    with open(os.path.join(EXC_DIR, filename), "w", encoding="utf-8") as f:
        f.write(f'class {exc}(Exception):\n    """Raised for {exc}."""\n    pass\n')

with open(os.path.join(EXC_DIR, "__init__.py"), "w", encoding="utf-8") as f:
    for exc in exceptions:
        f.write(f"from .{re.sub(r'(?<!^)(?=[A-Z])', '_', exc).lower()} import {exc}\n")

# 3. Generate Classes
for cls_name, fields, methods in blueprint:
    filename = re.sub(r'(?<!^)(?=[A-Z])', '_', cls_name).lower() + ".py"
    filepath = os.path.join(SRC_DIR, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f'"""Domain model for {cls_name}."""\n\n')
        f.write(f'class {cls_name}:\n')
        f.write(f'    """Represents a {cls_name}."""\n\n')
        
        # Build the __init__
        f.write("    def __init__(self")
        for field in fields:
            # Make some fields required and some optional with defaults
            if field in ["name", "order_id", "plate_number", "account_number", "unit_id", "rack_id", "policy_id"]:
                f.write(f", {field}: str")
            else:
                f.write(f", {field}=None")
        f.write(") -> None:\n")
        
        for field in fields:
            f.write(f"        self.{field} = {field}\n")
        f.write("\n")
        
        # Build the methods
        for method in methods:
            f.write(f"    def {method}(self) -> None:\n")
            f.write(f'        """Behavior for {cls_name} {method}."""\n')
            f.write("        pass\n\n")

print(f"SUCCESS! Generated {len(blueprint)} classes in {SRC_DIR}")
print(f"SUCCESS! Generated {len(exceptions)} exceptions in {EXC_DIR}")