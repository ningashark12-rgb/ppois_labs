"""Unit tests for the Order class."""

import pytest
from src.order import Order
from src.driver import Driver
from src.exceptions import DriverNotAvailableException
from src.vehicle import Vehicle

def test_order_assigns_driver():
    order = Order(order_id="123")
    driver = Driver(name="Alice")
    
    order.assign_driver(driver)
    
    assert order.driver == driver
    assert driver.is_available is False

def test_order_raises_if_driver_busy():
    order = Order(order_id="123")
    driver = Driver(name="Alice", is_available=False)
    
    with pytest.raises(DriverNotAvailableException):
        order.assign_driver(driver)

def test_order_complete():
    order = Order(order_id="1")
    order.complete_order()
    assert order.status == "Completed"


def test_order_cancel():
    order = Order(order_id="1")
    order.cancel_order()
    assert order.status == "Cancelled"

def test_order_calculate_price_no_cargo():
    order = Order(order_id="1")
    price = order.calculate_price(base_rate=10.0)
    assert price == 10.0

def test_order_calculate_price_with_cargo():
    class MockCargo:
        weight = 5
    order = Order(order_id="1", cargo=MockCargo())
    price = order.calculate_price(base_rate=10.0)
    assert price == 50.0

def test_order_complete_with_driver_and_vehicle():
    driver = Driver(name="John", is_available=False)
    vehicle = Vehicle(plate_number="ABC", is_available=False)
    order = Order(order_id="1", driver=driver, vehicle=vehicle)
    order.complete_order()
    assert order.status == "Completed"
    assert driver.is_available is True
    assert vehicle.is_available is True