"""Unit tests for the Order class."""

import pytest
from src.order import Order
from src.driver import Driver
from src.exceptions import DriverNotAvailableException

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