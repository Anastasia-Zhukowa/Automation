import requests
import pytest

from employee_Api import EmployeeApi


url = "https://x-clients-be.onrender.com"
api = EmployeeApi(url)

def test_create_new_employee():
    user = 'flora'
    password = 'nature-fairy'
    api.get_token(user, password)
    name = "Имя"
    description = "Описание"
    company_id = api.create_new_company(name, description)
    employee_before = api.get_employee(company_id)
    new_employee = api.add_employee(
        id="999",
        first_name="Ivan",
        last_name="Susanin",
        middle_name="Fedorovich",
        company_id=company_id,
        mail="test@skypro.ru",
        employee_url="https://example.com",
        phone="89012345678",
        birthdate="1954-05-01T11:16:23.575Z",
        is_active=True
)
    employee_after = api.get_employee(company_id)
    assert len(employee_before) < len(employee_after)
    assert employee_after[-1]["id"] == new_employee["id"]
    assert employee_after[-1]["firstName"] == 'Ivan'
    assert employee_after[-1]["lastName"] == 'Susanin'
    assert employee_after[-1]["middleName"] == 'Fedorovich'
    assert employee_after[-1]["companyId"] == company_id
    assert employee_after[-1]["email"] == "test@skypro.ru"
    assert employee_after[-1]["avatar_url"] == "https://example.com"
    assert employee_after[-1]["phone"] == "89012345678"
    assert employee_after[-1]["birthdate"] == "1954-05-01"
    assert employee_after[-1]["isActive"] == True

def test_get_employee_id():
    user = 'musa'
    password = 'music-fairy'
    api.get_token(user, password)
    name = "Huggy-vaggy"
    description = "Чтоб мне так жить"
    company_id = api.create_new_company(name, description)
    returned_id = api.add_employee(
        id="54546",
        first_name="Kasper",
        last_name="Cat",
        middle_name="Catovich",
        company_id=company_id,
        mail="kasper@test.ru",
        employee_url="https://zoo.com",
        phone="89099099900",
        birthdate="1978-10-11T11:16:23.575Z",
        is_active=True
)
    employee_id = api.get_employee_id(returned_id)
    assert employee_id["id"] == returned_id["id"]
    assert employee_id["firstName"] == "Kasper"
    assert employee_id["lastName"] == "Cat"
    assert employee_id["middleName"] == "Catovich"
    assert employee_id["companyId"] == company_id
    assert employee_id["email"] == "kasper@test.ru"
    assert employee_id["phone"] == "89099099900"
    assert employee_id["birthdate"] == "1978-10-11"
    assert employee_id["isActive"] == True

def test_update_employee():
    user =  'stella'
    password = 'sun-fairy'
    api.get_token(user, password)
    name = "Ромалы"
    description = "Гадаю недорого карты-таро"
    company_id = api.create_new_company(name, description)
    employee = api.add_employee(
        id="6699",
        first_name="Roza",
        last_name="Badoni",
        middle_name="Abramovna",
        company_id=company_id,
        mail="GypsiesRussia@mail.ru",
        employee_url="https://Gypsies of Russia.com",
        phone="89062544759",
        birthdate="1992-11-11T11:16:23.575Z",
        is_active=True
)
    api.change_employee(
        id=employee,
        change_lastName="Govani",
        change_email="GypsiesArmenia@mail.am",
        change_url="https://Gypsies of Armenia.com",
        change_phone="83745658955",
        change_active=False
)
    id_update_employee = api.get_employee_id(employee)
    assert id_update_employee["isActive"] == False
    assert id_update_employee["email"] == "GypsiesArmenia@mail.am"
    assert id_update_employee["avatar_url"] == "https://Gypsies of Armenia.com"