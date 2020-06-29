"""
Get all pagerduty users from API
"""

import requests
import pandas as pd

# API Key
API_KEY = ''


def list_users():

    # Pagination, 100 users per requests for 320 users
    # Change middle numbers depending on the amount of users
    for offset in range(0, 320, 100):   
        url = 'https://api.pagerduty.com/users?limit=100&offset={0}'.format(offset)
        headers = {
            'Accept': 'application/vnd.pagerduty+json;version=2',
            'Authorization': 'Token token={token}'.format(token=API_KEY)
        }
        
        r = requests.get(url, headers=headers)
        data = r.json()
        
        # Empty Dict to hold emails and id numbers
        users = {}
        
        # Looping through json dump to get emails and id numbers
        for user in (data['users'][0:]):
            users['email'] = user['email']
            users['id'] = user['id']
            
            # Creating Dataframe with users dictionnary and appending to csv file
            df = pd.DataFrame([users], columns=users.keys()).drop_duplicates()
            df.to_csv('pd_users.csv', mode='a', header=False, index=False)


if if __name__ == '__main__':
    list_users()
