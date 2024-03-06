import requests
import json

def pwbi_auth_token():
    
    user = 'XXXXXXX' #REPLACE WITH YOURS
    password = 'XXXXXXX' #REPLACE WITH YOURS
    client_id = 'XXXXXXX' #REPLACE WITH YOURS
    redirect_uri = 'https://login.microsoftonline.com/common/oauth2/token'
    resource = f'https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi'
    scope = 'openid'
    redirect_uri = 'https://login.microsoftonline.com/common/oauth2/token'
    cookie = 'XXXXXXX'  #REPLACE WITH YOURS

    payload = f"""client_id={client_id}&grant_type=password&resource={resource}&username={user}&password={password}&scope={scope}"""

    auth_headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': cookie
    }
    # define funcao de login pra pegar token
    res_auth = requests.request('POST', redirect_uri, headers=auth_headers, data=payload)
    access_token = res_auth.json()['access_token']

    return access_token

# def extract_data(query: str):
def extract_data(table_name: str, query: str):
    
    print(f'{table_name} - Started extracting')

    dataset_id = 'XXXXXXX' #REPLACE WITH YOURS
    token = pwbi_auth_token()
    
    bearer_token_header = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    url = f'https://api.powerbi.com/v1.0/myorg/datasets/{dataset_id}/executeQueries'

    body = {
        "queries": [
            {
                "query": query
            }
        ],
        "serializerSettings": {
            "includeNulls": True
        }
    }
    payload = json.dumps(body)
    response = requests.request('POST', url, headers=bearer_token_header, data=payload)
    data = response.content

    print(f'{table_name} - Finished extracting')

    return data