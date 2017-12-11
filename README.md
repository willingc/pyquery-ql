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

4. Activate the environment

    source activate pyquery

## Usage

To run:

    python3 pyquery-ql.py

## License

MIT
