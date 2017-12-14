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


def send_query(url, query, headers):
    """Send a query.

    With GraphQL and Python requests, a `post` is used when querying, instead
    of a `get`. The `post` is used since the `query` must be sent to the
    GraphQL endpoint. This differs from REST where the API endpoint has the
    query in its url structure.

    Returns:
        result: query result

    """

    result = requests.post(url=url, json={'query': query}, headers=headers)
    return result


def print_query_response(response):
    """print the query response"""
    pprint.pprint(json.loads(response.text))


if __name__ == '__main__':

    # get api token and set authorization
    api_token = os.environ['GITHUB_API_TOKEN']
    headers = {'Authorization': f'token {api_token}'}

    # set url to a GraphQL endpoint
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

    response = send_query(url, query, headers)
    print_query_response(response)

