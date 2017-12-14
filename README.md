# pyquery-ql

Query [GitHub API v4](https://developer.github.com/v4/) using a lightweight
[GraphQL](http://graphql.org) client

## What is pyquery-ql?

It's a repository for examples and tips when querying GraphQL APIs using
*Python* and the popular *Jupyter notebook*. It provides examples on using the
elegant *requests* library and *pandas* to do data collection and interactive
data exploration.

**pyquery-ql** is also a very early prototype for a lightweight Python
GraphQL client. It's based on Python 3.6 or higher and takes advantage of
f-strings (if you haven't tried them yet, please do).

## Why create a lightweight GraphQL client for Python?

In data science and scientific programming, we do lots of queries for data
from different sources. With the increased use of GraphQL, it's helpful to
have a lightweight client to do quick queries.

With Jupyter and nteract notebooks, it's critical to one's workflow to be
able to prototype and iterate from within the notebook. While full featured
clients, like [Apollo Client](https://www.apollographql.com/client/), and
explorers, such as [GitHub's GraphQL Explorer](https://developer.github.com/v4/explorer/),
are wonderful, the user must leave the notebook to see their benefits.

Using the Jupyter or nteract notebooks, a user explores data, and GraphQL is
fun to use since it's very easy to introspect the data source. A lightweight
Python client provides a simple way to bridge the data and
the Python scientific stack, especially pandas, from within the interactive
notebook.

## Installation

Supports Python 3.6+

1. Clone the repo.

        git clone https://github.com/willingc/pyquery-ql.git

2. Set up your GitHub API token to avoid rate limit and export to your
   environment:

        export GITHUB_API_TOKEN = '......'

### pip installation instructions

3. From the root of the cloned repo:

        pip install -r requirements.txt

###  conda installation instructions

3. Create the conda environment:

        conda env create -f environment.yml

4. Activate the environment:

        source activate pyquery

## Usage

To run:

    python3 pyquery-ql.py

## License

MIT

---

## GraphQL info

- [GraphQL](http://graphql.org)
    - describe your data
    - ask for what you want
    - get predictable results

- A [GraphQL service](http://graphql.org/learn/queries/) defines **types**
  and **fields** on those types. A function is created for each field on
  each type.

    - **field** can be a specific type (like String) or an Object
    - **arguments** can be passed to fields when making a query
        ```
        {
          human(id: "1000") {
            name
            height
          }
        }

- GraphQL schema and types
    ```
    type Character {
      name: String!
      appearsIn: [Episode]!
    }
    ```

    - GraphQL Object type `Character`
    - fields `name` and `appearsIn`
    - Scalar type `String`
    - `!` non-nullable (will always return a value when queried)
    - array `[Episode]`

- Arguments

    - every field can have 0 or more arguments
    - all arguments are named
    - all arguments are passed by name specifically (unlike JS or Python
      where functions take a list of ordered arguments
    - required or optional

-  Scalar types

    - fields that resolve to real data
    - leaves of the query
    - default scalar types:
        - `Int`
        - `Float`
        - `String`
        - `Boolean`
        - `ID` unique identifier
     - custom scalar types are possible i.e. `Date`
     - `Enums`

- Modifiers: Non-Null and List (array)
    - List [] can be null
    - a member of the list can not be null or it will generate an error
    - []! the actual list can not be null though a member can be null

- [**Introspection**](http://graphql.org/learn/introspection/) is a beautiful
  thing; ask for `__schema` for all the good stuff on the types

## GraphQL Client - deeper dive

- [Pagination](http://graphql.org/learn/introspection/)
    - plurals
    - slicing
    - pagination and edges
    - Connections
- [Caching](http://graphql.org/learn/caching/)
    - ID
    - pros and cons of globally unique IDs
    - server defined or client derived are both options

## GraphQL spec

- [The Spec](http://facebook.github.io/graphql/October2016/)
- [Response Format](http://facebook.github.io/graphql/October2016/#sec-Response-Format)
- [Grammar Summary](http://facebook.github.io/graphql/October2016/#sec-Appendix-Grammar-Summary)