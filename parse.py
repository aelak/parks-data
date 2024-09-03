from dotenv import load_dotenv
import requests
import os
from cachetools import cached, TTLCache

load_dotenv()

cache = TTLCache(maxsize=100, ttl=3600)

@cached(cache)
def get_data():
    raw = requests.get('https://nam12.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdeveloper.nps.gov%2Fapi%2Fv1%2Factivities%2Fparks%3Fapi_key%3Dq3rOnLMk9ojhMdKRdF8nQeR1UsREJwdHMRgv05Ws&data=05%7C02%7Crnagaraja%40911memorial.org%7Cfa5c0add637444c7cdde08dc533ec73e%7Cdbb7ee03320b4cb1bb52906ed2752b03%7C0%7C0%7C638476776317888591%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=%2FAQIupJQWp6HjxBmleqkh0bRZQvIs5TywmSQLkYn3QY%3D&reserved=0')
    parsed = raw.json()
    return parsed

'''
All available options for displaying_col:
    keys for parsed:  dict_keys(['total', 'limit', 'start', 'data'])
    keys for 1st item in data:  dict_keys(['id', 'name', 'parks'])
    keys for 1st item in parks:  dict_keys(['states', 'parkCode', 'designation', 'fullName', 'url', 'name'])
'''
def displaying_col():
    return {
        'Category': 'name',
        'Category ID': 'id',           
        'Park Name': 'name',           
        'Park Code': 'parkCode',        
        'Park Designation': 'designation',  
        'Park Full Name': 'fullName',    
        'Park URL': 'url',              
        'States': 'states'            
    }

def include_count():
    return True

if __name__ == "__main__":
    print("displaying data")
