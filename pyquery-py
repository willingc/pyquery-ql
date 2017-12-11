"""pyquery-ql.py

Send a graphql query to GitHub
and pretty print output.

Usage:

    python3 pyquery-ql.py

Supports Python 3.6+

"""
import json
import os
import pprint

import requests


# get api token and set authorization
api_token = os.environ['GITHUB_API_TOKEN']
headers = {'Authorization': f'token {api_token}'}

# set url to a graphql endpoint
url = 'https://api.github.com/graphql'

# add a json query
query = """
{
  organization(login: "jupyterhub") {
    repositories(first: 26) {
      totalCount
      edges {
        node {
          name
          url
          issues(states: OPEN) {
            totalCount
          }
          pullRequests(states: OPEN) {
            totalCount
          }
        }
      }
    }
  }
}
"""

# submit the request
r = requests.post(url=url, json={'query': query}, headers=headers)

pprint.pprint(json.loads(r.text))
