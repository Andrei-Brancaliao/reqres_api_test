from jsonschema import ValidationError, validate
import pytest
from routes.get_resource_route import get_resource_route
from schemas.resource_schema import success_resource_schema


def test_success_get_resource_without_params(setup):

    response = get_resource_route(setup)
    assert response.status_code == 200
    response_json = response.json()
    try:
        validate(instance=response_json, schema=success_resource_schema)
    except ValidationError as exception:
        pytest.fail(f"Error to Post Qualified: {exception}")


def test_success_get_resource_with_page_param(setup):
    
    page = 1
    
    response = get_resource_route(setup, page)
    assert (
        response.status_code == 200
    ), f"Status code expected: 200, but got {response.status_code}"
    
    response_json = response.json()
    assert response_json["page"] == page
    try:
        validate(instance=response_json, schema=success_resource_schema)
    except ValidationError as exception:
        pytest.fail(f"Error to Post Qualified: {exception}")

def test_success_get_resource_with_page_and_per_page_param(setup):
    
    page = 3
    per_page = 2
    
    response = get_resource_route(setup, page, per_page)
    assert (
        response.status_code == 200
    ), f"Status code expected: 200, but got {response.status_code}"
    
    response_json = response.json()
    assert response_json["page"] == page
    assert response_json["per_page"] == per_page
    try:
        validate(instance=response_json, schema=success_resource_schema)
    except ValidationError as exception:
        pytest.fail(f"Error to Post Qualified: {exception}")