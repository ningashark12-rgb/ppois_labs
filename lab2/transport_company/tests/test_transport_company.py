"""Unit tests for TransportCompany class."""
import pytest

from src.transport_company import TransportCompany
from src.driver import Driver
from src.vehicle import Vehicle
from src.order import Order


def test_hire_staff():
    company = TransportCompany(name="Fast")
    driver = Driver(name="John")
    company.hire_staff(driver)
    assert len(company.employees) == 1


def test_buy_vehicle():
    company = TransportCompany(name="Fast")
    vehicle = Vehicle(plate_number="ABC")
    company.buy_vehicle(vehicle)
    assert len(company.fleet) == 1


def test_register_client():
    company = TransportCompany(name="Fast")
    company.register_client("Client1")
    assert len(company.clients) == 1


def test_process_order_success():
    company = TransportCompany(name="Fast")
    company.hire_staff(Driver(name="John"))
    company.buy_vehicle(Vehicle(plate_number="ABC"))
    order = Order(order_id="1")
    
    company.process_order(order)
    
    assert order.driver.name == "John"
    assert order.vehicle.plate_number == "ABC"
    assert order.status == "Pending" # Still pending until completed


def test_process_order_fails_no_drivers():
    company = TransportCompany(name="Fast")
    company.buy_vehicle(Vehicle(plate_number="ABC"))
    order = Order(order_id="1")
    
    with pytest.raises(Exception): # Generic exception from our code
        company.process_order(order)


def test_generate_report():
    company = TransportCompany(name="Fast")
    report = company.generate_report()
    assert "Fast" in report