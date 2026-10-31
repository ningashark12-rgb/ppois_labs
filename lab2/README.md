# Lab 2: Transport Company Domain Model

This project implements a large-scale Object-Oriented model for a Transport Company. It demonstrates encapsulation, associations, custom exceptions, and domain logic across 50 classes.

## Architecture Overview

The system is divided into several subsystems:
- **Core Management**: `TransportCompany`, `Manager`, `Dispatcher`, `HRManager`
- **Logistics & Delivery**: `Order`, `Cargo`, `Route`, `Warehouse`, `Vehicle`
- **Personnel**: `Driver`, `Mechanic`, `Accountant`
- **Finance & Metrics**: `Payment`, `Invoice`, `CompanyFinance`, `Metrics`
- **Exceptions**: 12 custom exceptions for error handling.

## Class Blueprint

### 1. Main System
| Class | Fields | Methods | Associations |
|---|---|---|---|
| TransportCompany | 5 | 7 | Driver, Vehicle, Client, Order |
| Dispatcher | 4 | 5 | Order, Driver, Vehicle |
| Order | 7 | 5 | Client, Cargo, Driver, Vehicle |
| Client | 3 | 4 | Order |

### 2. Vehicles & Transport
| Class | Fields | Methods | Associations |
|---|---|---|---|
| Vehicle | 6 | 5 | Driver |
| Truck | 2 | 4 | Vehicle |
| Van | 2 | 4 | Vehicle |
| Trailer | 3 | 4 | Truck |
| ExpressDelivery | 4 | 3 | Order |

### 3. Cargo & Storage
| Class | Fields | Methods | Associations |
|---|---|---|---|
| Cargo | 4 | 3 | - |
| FragileCargo | 3 | 3 | Cargo |
| PerishableCargo | 3 | 3 | Cargo |
| Warehouse | 4 | 4 | Address, StorageUnit |
| StorageUnit | 4 | 4 | StorageZone |
| StorageZone | 4 | 3 | StorageUnit |
| Rack | 3 | 3 | - |

### 4. Personnel
| Class | Fields | Methods | Associations |
|---|---|---|---|
| Driver | 5 | 4 | DrivingLicense, Vehicle |
| Mechanic | 3 | 4 | Vehicle, MaintenanceRecord |
| Employee | 4 | 4 | - |
| Accountant | 4 | 4 | Payment, Invoice |
| HRManager | 4 | 4 | Employee |
| Manager | 3 | 4 | - |
| WarehouseManager | 3 | 4 | Warehouse |

### 5. Finance & Analytics
| Class | Fields | Methods | Associations |
|---|---|---|---|
| Payment | 4 | 4 | Client, Order |
| Invoice | 4 | 3 | - |
| Salary | 4 | 4 | Driver |
| BankAccount | 4 | 4 | - |
| CompanyFinance | 3 | 4 | - |
| ExpenseTracker | 2 | 4 | - |
| ProfitAnalyzer | 4 | 4 | - |
| TaxCalculator | 2 | 3 | - |

### 6. Utilities & Support
| Class | Fields | Methods | Associations |
|---|---|---|---|
| Address | 4 | 4 | GPSPosition |
| GPSPosition | 3 | 3 | - |
| Route | 4 | 4 | Address, GPSPosition |
| TrackingSystem | 2 | 4 | Vehicle |
| Insurance | 4 | 3 | Vehicle |
| MaintenanceRecord | 3 | 3 | Vehicle |
| Machine | 3 | 4 | Vehicle |

### 7. Metrics & Customer Service
| Class | Fields | Methods | Associations |
|---|---|---|---|
| Metrics | 4 | 4 | - |
| PerformanceMetric | 3 | 3 | - |
| FuelConsumption | 3 | 3 | - |
| TrafficInfo | 3 | 3 | - |
| CustomerService | 4 | 4 | - |
| CustomerFeedback | 2 | 4 | - |
| ServiceQualityMonitor | 2 | 3 | - |
| LoyaltyProgram | 2 | 3 | - |
| ServiceManagement | 4 | 4 | - |

## Custom Exceptions (12)
1. `TransportException` (Base)
2. `InsufficientFundsException`
3. `InvalidClientDataException`
4. `OrderNotFoundException`
5. `InvalidOrderDataException`
6. `InvalidCargoDataException`
7. `CargoOverweightException`
8. `VehicleOverloadException`
9. `VehicleNotAvailableException`
10. `DriverNotAvailableException`
11. `InvalidLicenseException`
12. `MaintenanceRequiredException`

## Domain Logic Example
The `TransportCompany` class manages the associations. When an `Order` is processed, the system ensures a `Driver` and `Vehicle` are available. If they are, it assigns them. If the `Driver` is busy, it throws a `DriverNotAvailableException`.