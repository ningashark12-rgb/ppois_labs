"""Unit tests for the CLI main.py."""

from unittest.mock import patch
from src.main import (
    main,
    _hire_driver,
    _buy_vehicle,
    _create_order,
    _process_next_order,
)
from src.transport_company import TransportCompany
from src.vehicle import Vehicle
from src.order import Order


def _feed(*inputs):
    """Return a fake input() that yields each string once."""
    iterator = iter(inputs)
    return lambda _prompt="": next(iterator)


def test_main_exit_immediately(capsys):
    with patch("builtins.input", _feed("0")):
        main()
    out = capsys.readouterr().out
    assert "Goodbye!" in out


def test_hire_driver_menu(capsys):
    company = TransportCompany("Fast")
    with patch("builtins.input", _feed("Alice")):
        _hire_driver(company)
    assert len(company.employees) == 1
    assert company.employees[0].name == "Alice"


def test_buy_vehicle_menu(capsys):
    company = TransportCompany("Fast")
    with patch("builtins.input", _feed("XYZ-123")):
        _buy_vehicle(company)
    assert len(company.fleet) == 1
    assert company.fleet[0].plate_number == "XYZ-123"


def test_create_order_menu(capsys):
    company = TransportCompany("Fast")
    with patch("builtins.input", _feed("ORD-99")):
        _create_order(company)
    assert len(company.orders) == 1
    assert company.orders[0].order_id == "ORD-99"


def test_process_next_order_empty(capsys):
    company = TransportCompany("Fast")
    _process_next_order(company)
    out = capsys.readouterr().out
    assert "No pending orders" in out


def test_main_invalid_choice(capsys):
    with patch("builtins.input", _feed("99", "0")):
        main()
    out = capsys.readouterr().out
    assert "Invalid choice" in out


def test_process_next_order_no_driver(capsys):
    company = TransportCompany("Fast")
    company.buy_vehicle(Vehicle(plate_number="ABC"))
    company.orders.append(Order(order_id="1"))
    _process_next_order(company)
    out = capsys.readouterr().out
    assert "Processing failed" in out


def test_process_next_order_generic_exception(capsys):
    from src.exceptions import TransportException

    company = TransportCompany("Fast")
    company.orders.append(Order(order_id="1"))
    # Monkeypatch process_order to raise a TransportException
    company.process_order = lambda o: (_ for _ in ()).throw(
        TransportException("Test")
    )
    _process_next_order(company)
    out = capsys.readouterr().out
    assert "Processing failed: Test" in out