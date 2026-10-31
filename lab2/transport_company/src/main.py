"""Command-line interface for the Transport Company domain."""

from __future__ import annotations

from .transport_company import TransportCompany
from .driver import Driver
from .vehicle import Vehicle
from .order import Order
from .exceptions import TransportException

MENU_OPTIONS = (
    ("1", "Hire a driver"),
    ("2", "Buy a vehicle"),
    ("3", "Create an order"),
    ("4", "Process next order"),
    ("5", "Company report"),
    ("0", "Exit"),
)


def _print_menu() -> None:
    print("\n=== Transport Company ===")
    for key, label in MENU_OPTIONS:
        print(f"{key}. {label}")


def _hire_driver(company: TransportCompany) -> None:
    name = input("Driver name: ").strip()
    company.hire_staff(Driver(name=name))
    print(f"Driver '{name}' hired.")


def _buy_vehicle(company: TransportCompany) -> None:
    plate = input("Vehicle plate number: ").strip()
    company.buy_vehicle(Vehicle(plate_number=plate))
    print(f"Vehicle '{plate}' added to fleet.")


def _create_order(company: TransportCompany) -> None:
    order_id = input("Order ID: ").strip()
    company.orders.append(Order(order_id=order_id))
    print(f"Order '{order_id}' created and queued.")


def _process_next_order(company: TransportCompany) -> None:
    pending = [o for o in company.orders if o.status == "Pending"]
    if not pending:
        print("No pending orders.")
        return
    order = pending[0]
    try:
        company.process_order(order)
        print(f"Order {order.order_id} processed. Driver: {order.driver.name}.")
    except TransportException as exc:
        print(f"Processing failed: {exc}")
    except Exception as exc:
        print(f"Processing failed: {exc}")


def main() -> None:
    """Run the interactive menu."""
    company = TransportCompany("Fast Logistics")

    handlers = {
        "1": lambda: _hire_driver(company),
        "2": lambda: _buy_vehicle(company),
        "3": lambda: _create_order(company),
        "4": lambda: _process_next_order(company),
        "5": lambda: print(company.generate_report()),
    }

    while True:
        _print_menu()
        choice = input("Choose: ").strip()

        if choice == "0":
            print("Goodbye!")
            return

        handler = handlers.get(choice)
        if handler is None:
            print("Invalid choice.")
            continue
        handler()


if __name__ == "__main__":  # pragma: no cover
    main()