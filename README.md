# pyquery-ql

Query [GitHub API v4](https://developer.github.com/v4/) using [GraphQL](http://graphql.org)

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