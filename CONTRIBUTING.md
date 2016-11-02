# How to contribute

## Have you found a bug?
If so, [open an issue](https://github.com/guillermo-carrasco/social_ids/issues/new) explaining the issue.

Please try to add as much information about the issue as possible, such as Python version and stack trace.

## Want to add another network?
That's awesome and these contributions are very much welcome :-D! The only requirement is that it **must not**
introduce a dependency with that network's SDK or require any kind of token.

To add your own network:

1. Create `social_ids/networks/<new_network>.py` and implement the method `get_id(handle)`
2. Add the new network to the dictionary `networks` in `social_ids/cli/get_ids.py`. Key must be the
network name in lowercase and value must be that network's module implementation
3. Write tests for the new network and the CLI
4. Increase the minor version number in `setup.py` . That is, for example from 1.0.1 to 1.1.0

Now just [create a pull request](https://github.com/guillermo-carrasco/social_ids/pull/new) with your changes :)

Thanks!
