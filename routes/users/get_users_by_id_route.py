
import requests

ROUTE = "users/"

def get_users_by_id_route(setup, id):
    """
    Fetches a user by id
    """
    
    response = requests.get(setup["data"]["base_url"] + ROUTE + str(id))
    return response