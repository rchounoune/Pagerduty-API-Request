"""
Deleting PagerDuty Users from csv file
"""

import requests
import json
import pandas as pd

# Api Key
API_KEY = ''

def delete_users():
    url = 'https://api.pagerduty.com/users/'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY)
    }

    # Reading CSV
    file = pd.read_csv('pd_ids.csv')
    df_id = pd.DataFrame(file)

    # Loop through the Id Column
    for i in df_id['id']:
        r = requests.delete(url+i, headers=headers)
        if r.status_code == 204:
            print("User" + " " + i + " "+ "Deleted")


if if __name__ == '__main__':
    delete_users()

