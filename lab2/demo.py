"""A quick demonstration of the Transport Company system."""

from transport_company.src.transport_company import TransportCompany
from transport_company.src.driver import Driver
from transport_company.src.vehicle import Vehicle
from transport_company.src.order import Order
from transport_company.src.exceptions import DriverNotAvailableException, VehicleNotAvailableException

def run_demo():
    print("--- Starting Transport Company Demo ---")
    
    # 1. Create the company
    company = TransportCompany("Fast Logistics")
    
    # 2. Hire a driver and buy a vehicle
    driver1 = Driver(name="John Doe", experience_years=5)
    truck1 = Vehicle(plate_number="ABC-123", brand="Volvo")
    
    company.hire_staff(driver1)
    company.buy_vehicle(truck1)
    
    # 3. Create an order
    order1 = Order(order_id="ORD-001")
    
    # 4. Process the order (this automatically finds the driver and vehicle)
    try:
        company.process_order(order1)
        print(f"Success! Order {order1.order_id} is assigned to {order1.driver.name} in vehicle {order1.vehicle.plate_number}.")
        print(f"Order Price: ${order1.price}")
    except Exception as e:
        print(f"Failed to process order: {e}")

    # 5. Try to assign the same driver to a second order (should fail)
    print("\n--- Trying to assign the busy driver to a new order ---")
    order2 = Order(order_id="ORD-002")
    try:
        company.process_order(order2)
        print("Success! (Wait, this shouldn't happen...)")
    except Exception as e:
        print(f"Expected Failure: {e}")

    # 6. Show the company report
    print("\n--- Company Report ---")
    print(company.generate_report())

    # 7. Complete the first order (this frees up the driver and vehicle)
    order1.complete_order()
    print("\n--- After completing ORD-001 ---")
    print(f"Driver available? {order1.driver.is_available}")
    print(f"Vehicle available? {order1.vehicle.is_available}")

if __name__ == "__main__":
    run_demo()