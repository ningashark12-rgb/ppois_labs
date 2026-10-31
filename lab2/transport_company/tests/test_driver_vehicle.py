"""Unit tests for Driver and Vehicle classes."""

import pytest
from src.driver import Driver
from src.vehicle import Vehicle
from src.exceptions import DriverNotAvailableException, VehicleNotAvailableException


def test_driver_accept_order():
    driver = Driver(name="John")
    driver.accept_order()
    assert driver.is_available is False


def test_driver_accept_order_fails_if_busy():
    driver = Driver(name="John", is_available=False)
    with pytest.raises(DriverNotAvailableException):
        driver.accept_order()


def test_driver_update_status():
    driver = Driver(name="John")
    driver.update_status(False)
    assert driver.is_available is False


def test_vehicle_start():
    vehicle = Vehicle(plate_number="ABC")
    vehicle.start()
    assert vehicle.is_available is False


def test_vehicle_start_fails_if_busy():
    vehicle = Vehicle(plate_number="ABC", is_available=False)
    with pytest.raises(VehicleNotAvailableException):
        vehicle.start()


def test_vehicle_stop():
    vehicle = Vehicle(plate_number="ABC", is_available=False)
    vehicle.stop()
    assert vehicle.is_available is True


def test_vehicle_update_mileage():
    vehicle = Vehicle(plate_number="ABC", mileage=100)
    vehicle.update_mileage(50)
    assert vehicle.mileage == 150

def test_vehicle_refuel():
    vehicle = Vehicle(plate_number="ABC")
    vehicle.refuel()
    assert vehicle.is_available is True

def test_vehicle_schedule_maintenance():
    vehicle = Vehicle(plate_number="ABC")
    vehicle.schedule_maintenance()
    assert vehicle.is_available is False