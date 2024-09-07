from jsonschema import ValidationError, validate
import pytest

from routes.get_users_route import get_users_route
from schemas.users_schema import success_users_schema


def test_success_get_users_without_params(setup):
    """
    Fetches a resource list without any param
    """
    
    response = get_users_route(setup)
    assert response.status_code == 200
    response_json = response.json()
    try:
        validate(instance=response_json, schema=success_users_schema)
    except ValidationError as exception:
        pytest.fail(f"Error to Post Qualified: {exception}")


def test_success_get_users_with_page_param(setup):
    """
    Fetches a resource list with page param
    """
    
    page = 1
    
    response = get_users_route(setup, page)
    assert (
        response.status_code == 200
    ), f"Status code expected: 200, but got {response.status_code}"
    
    response_json = response.json()
    assert response_json["page"] == page
    try:
        validate(instance=response_json, schema=success_users_schema)
    except ValidationError as exception:
        pytest.fail(f"Error to Post Qualified: {exception}")

def test_success_get_users_with_page_and_per_page_param(setup):
    """
    Fetches a resource list with page and per page param
    """
    
    page = 3
    per_page = 2
    
    response = get_users_route(setup, page, per_page)
    assert (
        response.status_code == 200
    ), f"Status code expected: 200, but got {response.status_code}"
    
    response_json = response.json()
    assert response_json["page"] == page
    assert response_json["per_page"] == per_page
    try:
        validate(instance=response_json, schema=success_users_schema)
    except ValidationError as exception:
        pytest.fail(f"Error to Post Qualified: {exception}")