# Social IDs

[![Build Status](https://travis-ci.org/guillermo-carrasco/social_ids.svg?branch=master)](https://travis-ci.org/guillermo-carrasco/social_ids)[![PyPI version](https://badge.fury.io/py/social_ids.svg)](https://badge.fury.io/py/social_ids)

## What?
Get user ids from social network handlers

## Why?
If you're a developer and work with social networks you'll know that getting the user ID is not straightforward. Usually
you have to use some sort of SDK and configure access tokens to get that information.

Inspired in [ids_please][ids_please] package for Ruby I created this Python tool so that you can
use it as a CLI tool or import it in your code. No need for tokens or SDKs, it does search for the ID
within the page source.

## How?

`pip install social_ids`

#### As CLI tool
Quite simple:

```
~> socialid --help
Usage: socialid [OPTIONS] NETWORK HANDLER

Options:
  --help  Show this message and exit.
```

#### As a package to import in your code
Simple as well

```python
# Import the networks you want
from social_ids.networks import facebook

# Then use the get_id method with the handler
_id = facebook.get_id('zuck')
```

## Networks

Right now social_ids works with:

* Facebook
* Twitter
* Instagram


[ids_please]: https://github.com/gazay/ids_please
