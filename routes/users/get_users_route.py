
import requests

ROUTE = "users"

def get_users_route(setup, page = "", per_page = "",):
    """
    Fetches a user list
    """
    
    if page != "" or per_page != "":
        params = {
            "page": page, 
            "per_page" : per_page
            }
    else:
        params = ""
        
    response = requests.get(setup["data"]["base_url"] + ROUTE, params=params)
    return response