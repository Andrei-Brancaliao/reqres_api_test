

import requests

ROUTE = "{resource}"

def get_resource_route(setup, page = "", per_page = "",):
    if page != "" or per_page != "":
        params = {
            "page": page, 
            "per_page" : per_page
            }
    else:
        params = ""
        
    response = requests.get(setup["data"]["base_url"] + ROUTE, params=params)
    return response