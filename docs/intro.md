# Introduction

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
