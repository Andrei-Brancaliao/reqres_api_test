import json
import os
import pytest

# Define the path to the configuration files
# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/'))
test_data_path = os.path.join(data_path, 'test_data.json')
response_body_data_path = os.path.join(data_path, 'response_body_data.json')

# Load test data
with open(test_data_path, 'r', encoding='utf-8') as f:
    test_data = json.load(f)
    
# Load test data
with open(response_body_data_path, 'r', encoding='utf-8') as f:
    response_body_data = json.load(f)

# Combine general configurations with test data

@pytest.fixture(name="setup")
def setup_success_fixture():
    """Initialize the configuration for success scenarios"""

    return {
        "data": test_data,
        "response_body" : response_body_data
    }