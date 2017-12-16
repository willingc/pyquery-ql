"""pyquery-ql.py

Send a graphql query to GitHub
and pretty print output.

Usage:

    python3 pyquery-ql.py

Supports Python 3.6+

"""
import json
import logging
import os
import pprint

import requests

logger = logging.getLogger(__name__)


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
    if result.status_code == 200:
        return result
    else:
        logger.warning(f"Request received error code: {result.status_code}")


def pretty_print_query_response(response):
    """print the query response"""
    if response.text is not None:
        pprint.pprint(json.loads(response.text))
    else:
        logger.warning('Response not valid.')


def print_query_response(response):
    """print the query response"""
    if response.text is not None:
        print(json.loads(response.text))
    else:
        logger.warning('Response not valid.')


def create_auth_header(api_token):
    """create a dictionary for authorization header"""
    return {'Authorization': f'token {api_token}'}


if __name__ == '__main__':

    # get api token
    api_token = os.environ['GITHUB_API_TOKEN']

    # Add authorization to headers
    headers = {}
    headers.update(create_auth_header(api_token))

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

    pretty_print_query_response(response)
    print_query_response(response)

