import pytest
import requests
from employee_Api import EmployeeApi
from CompanyApi import CompanyApi


@pytest.fixture
def employee_api():
    return EmployeeApi("https://x-clients-be.onrender.com")

def test_get_token(employee_api):
    token = employee_api.get_token()
    assert isinstance(token, str)

def test_create_new_company(employee_api):
    company_id = employee_api.create_new_company("This is a new Company", "Description of new company")
    assert isinstance(company_id, int)

def test_get_employee(employee_api):
    company_id = employee_api.create_new_company("This is a new Company", "Description of new company")
    employees = employee_api.get_employee(company_id)
    assert isinstance(employees, list)

def test_add_employee(employee_api):
    company_id = employee_api.create_new_company("This is a new Company", "Description of new company")
    employee_id = employee_api.add_employee(1, company_id, "Ivan", "Petrov", "Test", "test@test.com", "http://example.com", "1234567890", "1990-01-01", True)
    assert isinstance(employee_id, dict)

def test_get_employee_id(employee_api):
    company_id = employee_api.create_new_company("This is a new Company", "Description of new company")
    employee_id = employee_api.add_employee(1, company_id, "Ivan", "Petrov", "Test", "test@test.com", "http://example.com", "1234567890", "1990-01-01", True)
    employee = employee_api.get_employee_id(employee_id)
    assert isinstance(employee, dict)

def test_change_employee(employee_api):
    company_id = employee_api.create_new_company("This is a new Company", "Description of new company")
    employee_id = employee_api.add_employee(1, company_id, "John", "Petrovv", "Test", "im.john.now@example.com", "http://example.com", "1234567890", "1990-01-01", True)
    updated_employee = employee_api.change_employee(employee_id, "Updated", "updated@example.com", "http://updated.com", "0987654321", False)
    assert isinstance(updated_employee, dict)

