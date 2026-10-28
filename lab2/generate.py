import os
import re

# 1. Define the target directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "transport_company", "src")
EXC_DIR = os.path.join(SRC_DIR, "exceptions")

os.makedirs(SRC_DIR, exist_ok=True)
os.makedirs(EXC_DIR, exist_ok=True)

open(os.path.join(SRC_DIR, "__init__.py"), 'w').close()
open(os.path.join(EXC_DIR, "__init__.py"), 'w').close()

# 2. The Blueprint (The 50 classes)
blueprint = [
    ("Accountant", 4, 5), ("Address", 6, 5), ("BankAccount", 4, 6), ("Cargo", 6, 3),
    ("Client", 3, 6), ("CompanyFinance", 3, 12), ("CustomerService", 6, 7),
    ("Dispatcher", 4, 5), ("Driver", 6, 7), ("DrivingLicense", 4, 3), ("Employee", 8, 4),
    ("ExpressDelivery", 12, 11), ("FragileCargo", 8, 8), ("GPSPosition", 4, 4),
    ("HRManager", 4, 6), ("Insurance", 7, 4), ("Invoice", 7, 4), ("LogisticsManager", 5, 6),
    ("Machine", 5, 5), ("MaintenanceRecord", 7, 3), ("Manager", 5, 6), ("Mechanic", 4, 4),
    ("Metrics", 10, 9), ("Order", 11, 7), ("Payment", 7, 4), ("PerishableCargo", 9, 8),
    ("Route", 5, 5), ("Salary", 8, 4), ("ServiceManagement", 7, 10), ("StorageUnit", 8, 7),
    ("TrackingSystem", 2, 5), ("Trailer", 9, 6), ("TransportCompany", 6, 7), ("Truck", 3, 4),
    ("Van", 4, 4), ("Vehicle", 8, 6), ("Warehouse", 7, 5), ("WarehouseManager", 6, 6),
    ("ExpenseTracker", 2, 4), ("ProfitAnalyzer", 4, 7), ("TaxCalculator", 2, 4),
    ("PerformanceMetric", 4, 3), ("FuelConsumption", 4, 3), ("TrafficInfo", 3, 3),
    ("CustomerFeedback", 2, 4), ("ServiceQualityMonitor", 3, 4), ("LoyaltyProgram", 2, 2),
    ("StorageZone", 5, 2), ("Rack", 4, 1)
]

exceptions = [
    "TransportException", "InsufficientFundsException", "InvalidClientDataException",
    "OrderNotFoundException", "InvalidOrderDataException", "InvalidCargoDataException",
    "CargoOverweightException", "VehicleOverloadException", "VehicleNotAvailableException",
    "DriverNotAvailableException", "InvalidLicenseException"
]

# 3. Generate Exceptions
for exc in exceptions:
    filename = re.sub(r'(?<!^)(?=[A-Z])', '_', exc).lower() + ".py"
    with open(os.path.join(EXC_DIR, filename), "w", encoding="utf-8") as f:
        f.write(f'class {exc}(Exception):\n    """Raised for {exc}."""\n    pass\n')

with open(os.path.join(EXC_DIR, "__init__.py"), "w", encoding="utf-8") as f:
    for exc in exceptions:
        f.write(f"from .{re.sub(r'(?<!^)(?=[A-Z])', '_', exc).lower()} import {exc}\n")

# 4. Generate Classes
for cls_name, num_fields, num_methods in blueprint:
    filename = re.sub(r'(?<!^)(?=[A-Z])', '_', cls_name).lower() + ".py"
    filepath = os.path.join(SRC_DIR, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f'"""Domain model for {cls_name}."""\n\n')
        f.write(f'class {cls_name}:\n')
        f.write(f'    """Represents a {cls_name}."""\n\n')
        
        f.write("    def __init__(self) -> None:\n")
        for i in range(1, num_fields + 1):
            f.write(f"        self.field_{i} = None\n")
        f.write("\n")
        
        for i in range(1, num_methods + 1):
            f.write(f"    def action_{i}(self) -> None:\n        pass\n\n")

# 5. PRINT SUCCESS MESSAGE
print(f"SUCCESS! Generated {len(blueprint)} classes in {SRC_DIR}")
print(f"SUCCESS! Generated {len(exceptions)} exceptions in {EXC_DIR}")