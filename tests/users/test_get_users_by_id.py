from jsonschema import ValidationError, validate
import pytest

from routes.users.get_users_by_id_route import get_users_by_id_route
from schemas.users.users_by_id_schema import success_users_by_id_schema

def test_success_get_users_without_params(setup):
    """
    Fetches a resource list without any param
    """
    id = 1
    
    response = get_users_by_id_route(setup, id)
    assert response.status_code == 200
    response_json = response.json()
    
    try:
        validate(instance=response_json, schema=success_users_by_id_schema)
    except ValidationError as exception:
        pytest.fail(f"Error to Post Qualified: {exception}")